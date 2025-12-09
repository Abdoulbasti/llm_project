"""
Étape 5: Créer un dataset pour le fine-tuning.
Découpe le corpus par phrases, puis regroupe 3-5 phrases pour garder la cohérence.
"""

import os
import re
from datasets import Dataset


def split_into_sentence_groups(corpus: str, sentences_per_group: int = 4) -> list:
    """
    Découpe le corpus en phrases, puis regroupe N phrases ensemble.

    Args:
        corpus: Texte complet
        sentences_per_group: Nombre de phrases par groupe (défaut: 4)

    Returns:
        Liste de groupes de phrases
    """
    # Découper en phrases (., !, ?)
    sentences = re.split(r'(?<=[.!?])\s+', corpus)
    sentences = [s.strip() for s in sentences if s.strip()]

    # Regrouper N phrases ensemble
    groups = []
    for i in range(0, len(sentences), sentences_per_group):
        group = " ".join(sentences[i:i+sentences_per_group])
        if group:
            groups.append(group)

    return groups


def create_dataset(corpus_file: str = "src/data/cleaned_corpus.txt", output_dir: str = "src/dataset") -> Dataset:
    """Crée le dataset depuis le corpus en regroupant des phrases."""
    if not os.path.exists(corpus_file):
        raise FileNotFoundError(f"Fichier '{corpus_file}' introuvable. Lancez d'abord l'étape 4.")

    with open(corpus_file, "r", encoding="utf-8") as f:
        corpus = f.read()

    # Découper en groupes de phrases
    texts = split_into_sentence_groups(corpus, sentences_per_group=4)

    # Créer dataset
    dataset = Dataset.from_dict({"text": texts})

    # Sauvegarder
    os.makedirs(output_dir, exist_ok=True)
    dataset.save_to_disk(output_dir)

    print(f"✅ Dataset: {len(dataset):,} exemples (groupes de 4 phrases)")
    print(f"   Sauvegardé: {output_dir}")

    return dataset
