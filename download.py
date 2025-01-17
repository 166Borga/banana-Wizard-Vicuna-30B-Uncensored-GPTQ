# In this file, we define download_model
# It runs during container build time to get model weights built into the container

from transformers import AutoTokenizer, AutoModelForCausalLM

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    tokenizer = AutoTokenizer.from_pretrained("ehartford/Wizard-Vicuna-30B-Uncensored")
    model = AutoModelForCausalLM.from_pretrained("ehartford/Wizard-Vicuna-30B-Uncensored")

if __name__ == "__main__":
    download_model()
