"""
Étapes 8-9: Fine-tuning et sauvegarde du modèle.
"""

import torch
from transformers import Trainer, TrainingArguments


def data_collator(features):
    """Collator pour LM causal."""
    batch = {
        "input_ids": torch.stack([torch.tensor(f["input_ids"]) for f in features]),
        "attention_mask": torch.stack([torch.tensor(f["attention_mask"]) for f in features])
    }
    batch["labels"] = batch["input_ids"].clone()
    return batch


def fine_tune(train_dataset, eval_dataset, model, tokenizer, output_dir="src/model/mini-gpt-finetuned"):
    """Lance le fine-tuning et sauvegarde le modèle."""

    # Arguments d'entraînement
    training_args = TrainingArguments(
        output_dir=output_dir,
        # evaluation_strategy="epoch",
        eval_strategy="epoch",
        learning_rate=5e-5,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_steps=10,
        save_strategy="epoch",
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=data_collator,
    )

    # Entraînement
    print("🚀 Démarrage du fine-tuning...")
    trainer.train()

    # Sauvegarde
    print(f"\n💾 Sauvegarde du modèle dans '{output_dir}'...")
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)

    print(f"✅ Modèle fine-tuné sauvegardé")

    return trainer