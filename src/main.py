"""
Point d'entrée principal du projet LLM.
Pipeline automatique: Scraping (3) → Nettoyage (4) → Dataset (5)

Usage: python3 ./src/main.py
"""

from web_scraper import WebScraper
from scraping_sources_3 import SOURCES_CONFIG
import clean_text_4
import create_dataset_5


def main():
    """Pipeline complet: 3 → 4 → 5."""
    print("\n" + "=" * 60)
    print("PIPELINE LLM: Scraping → Nettoyage → Dataset")
    print("=" * 60 + "\n")

    # Étape 3: Scraping
    print("[1/3] Scraping des sources...")
    print("=" * 60)
    scraper = WebScraper(output_dir="src/data")
    res = scraper.scrape_multiple_sources(SOURCES_CONFIG)

    if res["succes"] == 0:
        print("\n❌ Scraping échoué. Arrêt du pipeline.\n")
        return False

    # Étape 4: Nettoyage
    print("\n[2/3] Nettoyage du texte...")
    print("=" * 60)
    try:
        corpus = clean_text_4.load_and_clean("src/data")
        clean_text_4.save_corpus(corpus)
        print("✅ Nettoyage terminé\n")
    except FileNotFoundError as e:
        print(f"\n❌ {e}")
        print("Arrêt du pipeline.\n")
        return False

    # Étape 5: Création du dataset
    print("[3/3] Création du dataset...")
    print("=" * 60)
    try:
        dataset = create_dataset_5.create_dataset()
        print("✅ Dataset créé\n")
    except FileNotFoundError as e:
        print(f"\n❌ {e}")
        print("Arrêt du pipeline.\n")
        return False

    # Succès
    print("=" * 60)
    print("✅ PIPELINE TERMINÉ AVEC SUCCÈS")
    print("=" * 60)
    print("\nFichiers générés:")
    print("  - src/data/*.txt (fichiers scrapés)")
    print("  - src/data/cleaned_corpus.txt (corpus nettoyé)")
    print("  - src/dataset/ (dataset Hugging Face)")
    print("\n💡 Prochaine étape: Tokenisation et fine-tuning\n")

    return True


if __name__ == "__main__":
    main()
