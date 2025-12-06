"""
Point d'entrée principal du projet LLM - Module de scraping.

Ce fichier permet de scraper plusieurs sources web configurées dans scraping_sources.py

Pour ajouter de nouvelles sources à scraper:
- Éditez le fichier scraping_sources.py
"""

from web_scraper import WebScraper
from scraping_sources_3 import SOURCES_CONFIG


def main():
    """
    Lance le scraping de toutes les sources configurées.

    Les sources sont définies dans scraping_sources.py.
    Les fichiers seront sauvegardés dans src/data/
    """
    print("=" * 60)
    print("🔄 SCRAPING DE SOURCES WEB")
    print("=" * 60)
    print(f"\n📋 {len(SOURCES_CONFIG)} source(s) configurée(s)\n")

    # Création du scraper et lancement
    scraper = WebScraper(output_dir="src/data")
    resultats = scraper.scrape_multiple_sources(SOURCES_CONFIG)

    return resultats


if __name__ == "__main__":
    main()
