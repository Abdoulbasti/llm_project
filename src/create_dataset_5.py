"""
Étape 5: Créer un dataset pour le fine-tuning.
Découpe le corpus en paragraphes pour éviter la perte de données.
"""

import os
from datasets import Dataset


def create_dataset(corpus_file: str = "src/data/cleaned_corpus.txt", output_dir: str = "src/dataset") -> Dataset:
    """Crée le dataset depuis le corpus en le découpant par paragraphes."""
    if not os.path.exists(corpus_file):
        raise FileNotFoundError(f"Fichier '{corpus_file}' introuvable. Lancez d'abord l'étape 4.")

    with open(corpus_file, "r", encoding="utf-8") as f:
        corpus = f.read()

    # Découper en paragraphes (évite la perte de données)
    texts = [p.strip() for p in corpus.split("\n\n") if p.strip()]

    # Créer dataset
    dataset = Dataset.from_dict({"text": texts})

    # Sauvegarder
    os.makedirs(output_dir, exist_ok=True)
    dataset.save_to_disk(output_dir)

    print(f"✅ Dataset: {len(dataset):,} exemples")
    print(f"   Sauvegardé: {output_dir}")

    return dataset


def main():
    print("=" * 60)
    print("ÉTAPE 5: Dataset")
    print("=" * 60)
    dataset = create_dataset()
    print("✅ Étape 5 terminée\n")
    return dataset


if __name__ == "__main__":
    main()
