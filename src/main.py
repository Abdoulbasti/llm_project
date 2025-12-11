"""
Point d'entrée principal du projet LLM.
Pipeline: Scraping (3) → Nettoyage (4) → Dataset (5) → Modèle (6) → Tokenisation (7) → Fine-tuning (8-9)

Usage: python3 ./src/main.py
"""

from web_scraper import WebScraper
from scraping_sources_3 import SOURCES_CONFIG
import clean_text_4
import create_dataset_5
import modele_distilgpt2_6
import tokenize_dataset_7
import prepare_fine_tuning_8_9
import run_trained_modele_10


def main():
    """Pipeline complet: 3 → 4 → 5 → 6 → 7 → 8-9."""
    print("\n" + "=" * 60)
    print("PIPELINE LLM COMPLET")
    print("=" * 60 + "\n")

    # Étape 3: Scraping
    print("[1/6] Scraping...")
    print("=" * 60)
    scraper = WebScraper(output_dir="src/data")
    res = scraper.scrape_multiple_sources(SOURCES_CONFIG)

    if res["succes"] == 0:
        print("\n❌ Scraping échoué\n")
        return False

    # Étape 4: Nettoyage
    print("\n[2/6] Nettoyage...")
    print("=" * 60)
    try:
        corpus = clean_text_4.load_and_clean("src/data")
        clean_text_4.save_corpus(corpus)
        print("✅ Nettoyage terminé\n")
    except FileNotFoundError as e:
        print(f"\n❌ {e}\n")
        return False

    # Étape 5: Dataset
    print("[3/6] Dataset...")
    print("=" * 60)
    try:
        dataset = create_dataset_5.create_dataset()
        print("✅ Dataset créé\n")
    except FileNotFoundError as e:
        print(f"\n❌ {e}\n")
        return False

    # Étape 6: Modèle
    print("[4/6] Modèle DistilGPT2...")
    print("=" * 60)
    tokenizer, model = modele_distilgpt2_6.load_model()
    print("✅ Modèle chargé\n")

    # Étape 7: Tokenisation
    print("[5/6] Tokenisation...")
    print("=" * 60)
    train, test, tokenizer = tokenize_dataset_7.tokenize_dataset()
    print("✅ Tokenisation terminée\n")

    # Étapes 8-9: Fine-tuning
    print("[6/7] Fine-tuning...")
    print("=" * 60)
    trainer = prepare_fine_tuning_8_9.fine_tune(train, test, model, tokenizer)
    print("✅ Fine-tuning terminé\n")

    # Étape 10: Chatbot avec modèle fine-tuné
    print("[7/7] Lancement du chatbot...")
    print("=" * 60)
    run_trained_modele_10.chatbot_finetuned()

    # Succès
    print("=" * 60)
    print("✅ PIPELINE COMPLET TERMINÉ")
    print("=" * 60)
    print("\nFichiers générés:")
    print("  - src/data/*.txt (fichiers scrapés)")
    print("  - src/data/cleaned_corpus.txt (corpus nettoyé)")
    print("  - src/dataset/ (dataset)")
    print("  - src/model/mini-gpt-finetuned/ (modèle fine-tuné)")
    print("\n💡 Lancez: python3 src/run_trained_modele_10.py\n")

    return True


if __name__ == "__main__":
    main()
