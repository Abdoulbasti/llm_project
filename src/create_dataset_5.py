"""
Étape 5: Créer un dataset pour le fine-tuning.
Transforme le corpus nettoyé en Dataset Hugging Face (version 5.1: un seul long texte).
"""

import os
from datasets import Dataset


def load_cleaned_corpus(corpus_file: str = "src/data/cleaned_corpus.txt") -> str:
    """Charge le corpus nettoyé."""
    if not os.path.exists(corpus_file):
        raise FileNotFoundError(f"Fichier '{corpus_file}' introuvable. Lancez d'abord l'étape 4.")

    with open(corpus_file, "r", encoding="utf-8") as f:
        return f.read()


def create_dataset(corpus_file: str = "src/data/cleaned_corpus.txt", output_dir: str = "src/dataset") -> Dataset:
    """
    Crée et sauvegarde le dataset depuis le corpus.

    Returns:
        Dataset Hugging Face
    """
    # Charger corpus
    corpus = load_cleaned_corpus(corpus_file)

    # Créer dataset (version 5.1)
    dataset = Dataset.from_dict({"text": [corpus]})

    # Sauvegarder
    # dataset.save_to_disk(output_dir)

    # Crée un fichier mon_dataset.csv
    # dataset.to_csv("src/dataset/mon_dataset.csv")

    # Crée un fichier mon_dataset.parquet (Recommandé)
    # dataset.to_parquet("src/dataset/mon_dataset.parquet")

    # Stats
    print(f"✅ Dataset créé: {len(corpus):,} caractères, ~{len(corpus.split()):,} mots")
    print(f"   Sauvegardé dans: {output_dir}")

    return dataset