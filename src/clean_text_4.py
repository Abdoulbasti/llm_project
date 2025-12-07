"""
Étape 4: Nettoyage et préparation du texte.
Charge les fichiers scrapés, nettoie le texte et crée le corpus.
"""

import os
import re


def clean_text(text: str) -> str:
    """Nettoie un texte (espaces multiples, caractères bizarres)."""
    text = re.sub(r"\s+", " ", text)
    text = text.replace("\xa0", " ").replace("\u200b", "").replace("\r", "")
    return text.strip()


def load_and_clean(data_dir: str = "src/data") -> str:
    """
    Charge tous les .txt, les nettoie et crée le corpus fusionné.

    Returns:
        Corpus complet nettoyé
    """
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Dossier '{data_dir}' introuvable.")

    texts = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(data_dir, filename), "r", encoding="utf-8") as f:
                texts.append(clean_text(f.read()))

    if not texts:
        raise FileNotFoundError(f"Aucun fichier .txt dans '{data_dir}'.")

    corpus = "\n\n".join(texts)
    print(f"✅ {len(texts)} fichier(s) chargé(s) et nettoyé(s)")
    print(f"   {len(corpus):,} caractères, ~{len(corpus.split()):,} mots")

    return corpus


def save_corpus(corpus: str, output_file: str = "src/data/cleaned_corpus.txt") -> bool:
    """Sauvegarde le corpus nettoyé."""
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(corpus)
        print(f"   Sauvegardé dans: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False