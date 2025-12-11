# LLM Mini-Project

Création d'un modèle génératif spécialisé sur le golf par fine-tuning de DistilGPT2.

## Installation

```bash
# Créer et activer l'environnement virtuel et tous bu
./env.sh
```

## Pipeline complet

Pour exécuter tout le pipeline (scraping → fine-tuning → chatbot):
```bash
# Décommenter le code dans src/main.py puis:
python3 src/main.py
```

## Utilisation

### 1. Chatbot avec modèle de base (sans fine-tuning)

Utilise DistilGPT2 sans spécialisation:
```bash
python3 src/chatbot_without_specialisation.py
```

**Caractéristiques:**
- Modèle: `distilgpt2` (base)
- Réponses génériques, non spécialisées
- Utilisé comme référence pour comparaison

### 2. Chatbot avec fine-tuning (spécialisé golf)

Utilise le modèle fine-tuné sur le golf:
```bash
python3 src/main.py
```

**Caractéristiques:**
- Modèle: `src/model/mini-gpt-finetuned/`
- Réponses spécialisées sur le golf
- Fine-tuné sur corpus golf

### 3. Tester les deux modèles
Utilisez les prompts dans `prompt_input.txt` pour comparer les réponses des deux modèles:
```bash
# 30 prompts de test sur le golf:
# - Définitions & Concepts
# - Équipement
# - Parcours & Terrain
# - Histoire & Règles
# - Techniques & Stratégies
```

**Exemple de test:**
1. Lancez `chatbot_without_specialisation.py`
2. Testez avec: "What is golf?"
3. Notez la réponse
4. Lancez `main.py`
5. Testez avec le même prompt
6. Comparez les résultats


## Dépendances principales

- `transformers` - Modèles et pipelines Hugging Face
- `datasets` - Gestion des datasets
- `torch` - PyTorch (backend)
- `accelerate` - Accélération entraînement
- `sentencepiece` - Tokenisation
- `beautifulsoup4` - Web scraping
- `requests` - Requêtes HTTP

## Résultats attendus

**Comparaison modèle base vs fine-tuné:**
- **Modèle base**: Réponses génériques, peut dériver du sujet
- **Modèle fine-tuné**: Réponses spécialisées golf, vocabulaire technique