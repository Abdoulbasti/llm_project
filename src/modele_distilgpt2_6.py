"""
Étape 6: Charger le modèle DistilGPT2.
"""

from transformers import AutoTokenizer, AutoModelForCausalLM


def load_model(model_name: str = "distilgpt2"):
    """Charge le modèle et tokenizer, configure le padding."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # GPT2 n'a pas de pad_token par défaut
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = tokenizer.eos_token_id

    print(f"✅ Modèle chargé: {model.num_parameters():,} paramètres")
    return tokenizer, model


def main():
    print("=" * 60)
    print("ÉTAPE 6: Modèle DistilGPT2")
    print("=" * 60)

    tokenizer, model = load_model()
    print("✅ Étape 6 terminée\n")
    return tokenizer, model


if __name__ == "__main__":
    main()
