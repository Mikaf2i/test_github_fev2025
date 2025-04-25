

import streamlit as st
from transformers import BertForSequenceClassification, BertTokenizer
from safetensors.torch import load_file
import torch
import re
import sys

# Define clean_text function outside of load_model and main for pickling
def clean_text(text):
    text = re.sub(r'@\w+|#|http\S+|[^\w\s]', '', text.lower())
    return text.strip()

def main():
    # Configuration
    MODEL_DIR = "bert_streamlit_ready"
    
    # Chargement du modèle
    @st.cache_resource
    def load_model():
        try:
            # 1. Load the model structure from the directory
            model = BertForSequenceClassification.from_pretrained(MODEL_DIR, num_labels=2)
            
            # 2. Load the state dict
            model.load_state_dict(load_file(f"{MODEL_DIR}/model.safetensors"))
            
            tokenizer = BertTokenizer.from_pretrained(MODEL_DIR)
            # Use safe_globals to allow clean_text when loading metadata
            with torch.serialization.safe_globals([clean_text]):
                metadata = torch.load(f"{MODEL_DIR}/metadata.pth", map_location='cpu')  
            return model, tokenizer, metadata
        except Exception as e:
            st.error(f"Erreur de chargement du modèle : {str(e)}")
            return None, None, None  # Return None values on error

    # Interface
    st.set_page_config(page_title="Prédiction de Tweets Viraux", layout="wide")
    st.title("🔮 Prédiction de Tweets Viraux")
    
    model, tokenizer, metadata = load_model()

    # Check if model loaded successfully before proceeding
    if model is not None and tokenizer is not None and metadata is not None:
        with st.form("prediction_form"):
            user_input = st.text_area("Entrez un tweet :")
            submitted = st.form_submit_button("Prédire")
            
            if submitted and user_input:
                with st.spinner("Analyse en cours..."):
                    try:
                        # Nettoyage et tokenisation
                        text = metadata['clean_text_fn'](user_input)
                        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
                        
                        # Prédiction
                        with torch.no_grad():
                            outputs = model(**inputs)
                            probs = torch.softmax(outputs.logits, dim=1)
                        
                        # Affichage
                        viral_prob = probs[0][1].item()
                        st.metric("Probabilité d'être viral", f"{viral_prob:.1%}")
                        st.progress(viral_prob)
                        
                        if viral_prob > 0.7:
                            st.success("🔥 Tweet viral potentiel !")
                        else:
                            st.info("💤 Peu susceptible de devenir viral")
                            
                    except Exception as e:
                        st.error(f"Erreur lors de la prédiction : {str(e)}")
    else:
        st.error("Le modèle n'a pas pu être chargé. Veuillez vérifier les logs d'erreur.")



if __name__ == "__main__":
    if "streamlit" in sys.modules:
        main()
    else:
        print("⚠️ Veuillez exécuter avec : streamlit run app.py")
        print("   Ou via Jupyter : !streamlit run app.py")

