"""
Étape 7: Tokenisation du dataset.
"""

from datasets import load_from_disk
from modele_distilgpt2_6 import load_model

BLOCK_SIZE = 128


def tokenize_dataset(dataset_dir: str = "src/dataset", block_size: int = BLOCK_SIZE):
    """Tokenise le dataset et split train/test."""
    # Charger dataset et modèle
    dataset = load_from_disk(dataset_dir)
    tokenizer, _ = load_model()

    # Fonction de tokenisation
    def tokenize_function(examples):
        return tokenizer(
            examples["text"],
            truncation=True,
            max_length=block_size,
            padding="max_length",
        )

    # Tokeniser
    tokenized = dataset.map(tokenize_function, batched=True, remove_columns=["text"])

    # Split train/validation (90/10)
    split = tokenized.train_test_split(test_size=0.1)

    print(f"✅ Tokenisation: {len(tokenized):,} exemples")
    print(f"   Train: {len(split['train']):,}")
    print(f"   Test: {len(split['test']):,}")

    return split["train"], split["test"], tokenizer

