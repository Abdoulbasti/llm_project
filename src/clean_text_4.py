"""
Étape 4: Nettoyage et préparation du texte.

Ce module charge tous les fichiers scrapés depuis src/data/,
nettoie le texte et le prépare pour l'étape 5 (création du dataset).
"""

import os
import re


def clean_text(text: str) -> str:
    """
    Nettoie un texte en:
    - Retirant les multiples espaces
    - Retirant les caractères bizarres (espaces insécables, etc.)
    - Supprimant les espaces en début et fin

    Args:
        text: Le texte à nettoyer

    Returns:
        Le texte nettoyé
    """
    # Retirer les multiples espaces, tabs, retours à la ligne
    text = re.sub(r"\s+", " ", text)

    # Retirer certains caractères bizarres
    text = text.replace("\xa0", " ")  # Espace insécable
    text = text.replace("\u200b", "")  # Zero-width space
    text = text.replace("\r", "")      # Carriage return

    # Enlever les espaces au début et à la fin
    return text.strip()


def load_scraped_files(data_dir: str = "src/data") -> list:
    """
    Charge tous les fichiers .txt depuis le dossier data.

    Args:
        data_dir: Chemin vers le dossier contenant les fichiers scrapés

    Returns:
        Liste de dictionnaires contenant 'filename' et 'content'
    """
    if not os.path.exists(data_dir):
        print(f"❌ Erreur: Le dossier '{data_dir}' n'existe pas.")
        return []

    texts = []

    print(f"📂 Chargement des fichiers depuis '{data_dir}'...\n")

    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(data_dir, filename)

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    texts.append({
                        "filename": filename,
                        "content": content
                    })
                print(f"✅ {filename} - {len(content)} caractères")

            except Exception as e:
                print(f"❌ Erreur lors de la lecture de {filename}: {e}")

    print(f"\n📊 Total: {len(texts)} fichier(s) chargé(s)")
    return texts


def clean_all_texts(texts: list) -> list:
    """
    Applique le nettoyage sur tous les textes.

    Args:
        texts: Liste de dictionnaires avec 'filename' et 'content'

    Returns:
        Liste de dictionnaires avec le contenu nettoyé
    """
    print(f"\n🧹 Nettoyage de {len(texts)} fichier(s)...\n")

    cleaned_texts = []

    for item in texts:
        cleaned_content = clean_text(item["content"])
        cleaned_texts.append({
            "filename": item["filename"],
            "content": cleaned_content,
            "original_length": len(item["content"]),
            "cleaned_length": len(cleaned_content)
        })

        reduction = len(item["content"]) - len(cleaned_content)
        print(f"✅ {item['filename']} - Réduction: {reduction} caractères")

    return cleaned_texts


def create_full_corpus(cleaned_texts: list) -> str:
    """
    Fusionne tous les textes nettoyés en un seul corpus.

    Args:
        cleaned_texts: Liste de dictionnaires avec le contenu nettoyé

    Returns:
        Le corpus complet fusionné
    """
    print(f"\n🔗 Fusion de {len(cleaned_texts)} texte(s) en un corpus...\n")

    # Extraire uniquement le contenu de chaque texte
    text_contents = [item["content"] for item in cleaned_texts]

    # Fusionner avec 2 retours à la ligne entre chaque texte
    full_corpus = "\n\n".join(text_contents)

    print(f"📏 Longueur totale du corpus: {len(full_corpus)} caractères")
    print(f"📝 Nombre de mots (approximatif): {len(full_corpus.split())}")

    return full_corpus


def save_corpus(corpus: str, output_file: str = "src/data/cleaned_corpus.txt") -> bool:
    """
    Sauvegarde le corpus nettoyé dans un fichier.

    Args:
        corpus: Le corpus à sauvegarder
        output_file: Chemin du fichier de sortie

    Returns:
        True si la sauvegarde a réussi, False sinon
    """
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(corpus)

        print(f"\n💾 Corpus sauvegardé dans '{output_file}'")
        return True

    except Exception as e:
        print(f"\n❌ Erreur lors de la sauvegarde: {e}")
        return False


def main():
    """Fonction principale pour l'étape 4."""

    print("=" * 60)
    print("🧹 ÉTAPE 4: NETTOYAGE ET PRÉPARATION DU TEXTE")
    print("=" * 60)
    print()

    # 1. Charger tous les fichiers scrapés
    texts = load_scraped_files("src/data")

    if not texts:
        print("\n⚠️ Aucun fichier à traiter. Lancez d'abord le scraping (src/main.py)")
        return

    # 2. Nettoyer tous les textes
    cleaned_texts = clean_all_texts(texts)

    # 3. Créer le corpus complet
    full_corpus = create_full_corpus(cleaned_texts)

    # 4. Sauvegarder le corpus
    save_corpus(full_corpus, "src/data/cleaned_corpus.txt")

    # Afficher un aperçu
    print("\n" + "=" * 60)
    print("📄 APERÇU DU CORPUS (premiers 1000 caractères)")
    print("=" * 60)
    print(full_corpus[:1000])
    print("...")
    print("\n" + "=" * 60)
    print("✅ Étape 4 terminée avec succès!")
    print("=" * 60)
    print("\n💡 Prochaine étape: Créer le dataset (étape 5)")
    print()


if __name__ == "__main__":
    main()
