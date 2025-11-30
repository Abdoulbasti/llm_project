from transformers import pipeline


def chatbot_without_specialisation():
    """
    Interactive chatbot using DistilGPT2 model.
    The user can type prompts and receive generated responses.
    Type 'exit' or 'quit' to end the conversation.
    """
    print("🚀 Starting DistilGPT2 Chatbot...")
    print("Loading model... Please wait.\n")

    # Load the fine-tuned model or use base distilgpt2
    # Change output_dir to "./mini-gpt-finetuned" if you have a fine-tuned model
    output_dir = "distilgpt2"  # Use base model for now

    try:
        generator = pipeline(
            "text-generation",
            model=output_dir,
            tokenizer=output_dir,
        )
        print("✅ Model loaded successfully!\n")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return

    print("=" * 60)
    print("You can now chat with the model!")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("=" * 60)
    print()

    while True:
        # Get user input
        prompt = input("You: ").strip()

        # Check for exit commands
        if prompt.lower() in ["exit", "quit"]:
            print("\n👋 Goodbye! Ending conversation.")
            break

        # Skip empty inputs
        if not prompt:
            print("⚠️  Please enter a valid prompt.\n")
            continue

        # Generate response with the specified parameters
        try:
            outputs = generator(
                prompt,
                max_new_tokens=150,          # Plus de tokens pour des réponses plus complètes
                num_return_sequences=1,      # Generate only 1 response for interactive chat
                do_sample=True,              # Créatif
                top_k=50,                    # Garde les 50 mots les plus logiques
                top_p=0.95,                  # Nucleus sampling
                temperature=0.9,             # Plus de créativité (0.7 → 0.9)
                repetition_penalty=1.3,      # Évite encore plus les répétitions
                pad_token_id=50256,          # Évite le warning
                truncation=True,             # Active explicitement la troncature
            )

            # Extract and print the generated text
            generated_text = outputs[0]["generated_text"]
            print(f"\nBot: {generated_text}\n")
            print("-" * 60)
            print()

        except Exception as e:
            print(f"❌ Error generating response: {e}\n")
