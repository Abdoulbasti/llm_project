"""
Module de scraping pour récupérer du contenu web.
"""
import requests
from bs4 import BeautifulSoup
import os
from typing import Optional


class WebScraper:
    """Classe pour gérer le scraping de pages web."""

    def __init__(self, output_dir: str = "src/data"):
        """
        Initialise le scraper.

        Args:
            output_dir: Dossier où sauvegarder les fichiers scrapés
        """
        self.output_dir = output_dir
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Créer le dossier de sortie s'il n'existe pas
        self._ensure_output_dir_exists()

    def _ensure_output_dir_exists(self):
        """Crée le dossier de sortie s'il n'existe pas."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            print(f"✅ Dossier '{self.output_dir}' créé.")

    def scrape_page(self, url: str, nom_fichier: str, description: Optional[str] = None) -> dict:
        """
        Récupère le contenu d'une page web et le sauvegarde dans un fichier.

        Args:
            url: URL de la page à scraper
            nom_fichier: Nom du fichier de sortie (relatif au output_dir)
            description: Description optionnelle de la source

        Returns:
            dict: {"success": bool, "skipped": bool}
        """
        print(f"\n{'='*60}")
        if description:
            print(f"📄 {description}")
        print(f"🔗 URL: {url}")
        print(f"💾 Fichier: {nom_fichier}")
        print(f"{'='*60}")

        # Vérifier si le fichier existe déjà
        chemin_fichier = os.path.join(self.output_dir, nom_fichier)
        if os.path.exists(chemin_fichier):
            print(f"⏭️  Fichier déjà existant, scraping ignoré")
            return {"success": True, "skipped": True}

        try:
            # 1. Récupération du contenu
            print("⏳ Connexion en cours...")
            reponse = requests.get(url, headers=self.headers, timeout=10)
            reponse.raise_for_status()

            # 2. Analyse du HTML
            print("🔍 Analyse du contenu...")
            soup = BeautifulSoup(reponse.content, 'html.parser')

            # 3. Extraction du texte (paragraphes)
            paragraphes = soup.find_all('p')
            print(f"📝 {len(paragraphes)} paragraphes trouvés")

            # 4. Sauvegarde dans le fichier
            with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
                # Contenu seulement (pas de métadonnées pour éviter le bruit)
                for p in paragraphes:
                    texte_propre = p.get_text().strip()
                    if texte_propre:
                        fichier.write(texte_propre + "\n\n")

            print(f"✅ Succès! Contenu sauvegardé dans '{chemin_fichier}'")
            return {"success": True, "skipped": False}

        except requests.exceptions.Timeout:
            print(f"❌ Erreur: Timeout lors de la connexion à {url}")
            return {"success": False, "skipped": False}
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur de connexion: {e}")
            return {"success": False, "skipped": False}
        except Exception as e:
            print(f"❌ Erreur inattendue: {e}")
            return {"success": False, "skipped": False}

    def scrape_multiple_sources(self, sources: list) -> dict:
        """
        Scrape plusieurs sources.

        Args:
            sources: Liste de dictionnaires avec les clés 'url', 'nom_fichier', 'description'

        Returns:
            Dictionnaire avec les statistiques du scraping
        """
        print(f"\n🚀 Démarrage du scraping de {len(sources)} source(s)...\n")

        resultats = {
            "total": len(sources),
            "succes": 0,
            "echecs": 0,
            "ignores": 0,
            "fichiers_crees": []
        }

        for i, source in enumerate(sources, 1):
            print(f"\n[{i}/{len(sources)}]")

            res = self.scrape_page(
                url=source["url"],
                nom_fichier=source["nom_fichier"],
                description=source.get("description")
            )

            if res["success"]:
                resultats["succes"] += 1
                if not res["skipped"]:
                    resultats["fichiers_crees"].append(source["nom_fichier"])
                else:
                    resultats["ignores"] += 1
            else:
                resultats["echecs"] += 1

        # Affichage du résumé
        print(f"\n{'='*60}")
        print("📊 RÉSUMÉ DU SCRAPING")
        print(f"{'='*60}")
        print(f"✅ Succès: {resultats['succes']}/{resultats['total']}")
        if resultats["ignores"] > 0:
            print(f"⏭️  Ignorés (déjà existants): {resultats['ignores']}/{resultats['total']}")
        print(f"❌ Échecs: {resultats['echecs']}/{resultats['total']}")
        if resultats["fichiers_crees"]:
            print(f"\n📁 Nouveaux fichiers créés dans '{self.output_dir}':")
            for fichier in resultats["fichiers_crees"]:
                print(f"   - {fichier}")
        print(f"{'='*60}\n")

        return resultats
