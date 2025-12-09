"""
Étape 10: Générer du texte avec le modèle fine-tuné.
Chatbot interactif utilisant le modèle spécialisé.
"""

from transformers import pipeline


def chatbot_finetuned(model_dir: str = "src/model/mini-gpt-finetuned"):
    """Chatbot interactif avec le modèle fine-tuné."""
    print("🚀 Chargement du modèle fine-tuné...")

    try:
        generator = pipeline(
            "text-generation",
            model=model_dir,
            tokenizer=model_dir,
        )
        print(f"✅ Modèle chargé: {model_dir}\n")
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return

    print("=" * 60)
    print("Chatbot spécialisé prêt!")
    print("Tapez 'exit' ou 'quit' pour quitter")
    print("=" * 60 + "\n")

    while True:
        prompt = input("Vous: ").strip()

        if prompt.lower() in ["exit", "quit"]:
            print("\n👋 Au revoir!\n")
            break

        if not prompt:
            print("⚠️ Entrez un prompt valide\n")
            continue

        try:
            outputs = generator(
                prompt,
                max_new_tokens=100,
                num_return_sequences=1,
                do_sample=True,
                top_k=50,
                top_p=0.95,
                temperature=0.9,
                repetition_penalty=1.3,
                # pad_token_id=50256,
                truncation=True,
            )

            print(f"\nBot: {outputs[0]['generated_text']}\n")
            print("-" * 60 + "\n")

        except Exception as e:
            print(f"❌ Erreur: {e}\n")
            