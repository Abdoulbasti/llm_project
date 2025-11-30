# LLM Mini-Project

Création d'un modèle génératif spécialisé par fine-tuning de distilgpt2.

## Installation

```bash
# Créer et activer l'environnement virtuel
python3 venv_builder.py
source .venv/bin/activate

# Ou installation manuelle
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Structure

```
llm_project/
├── .venv/                    # Environnement virtuel
├── data/                     # Fichiers texte (.txt)
├── mini-gpt-finetuned/      # Modèle entraîné (généré)
├── venv_builder.py          # Script de setup
├── example_data_loader.py   # Exemple de chargement de données
└── requirements.txt         # Dépendances
```

## Utilisation

### 1. Préparer les données
```bash
mkdir data
# Ajouter vos fichiers .txt dans data/
python example_data_loader.py
```

### 2. Entraîner le modèle
```python
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import Dataset

# Charger le modèle de base
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Configurer padding
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.eos_token_id

# Fine-tuning (voir InstructionMiniProjet.pdf)
```

### 3. Générer du texte
```python
from transformers import pipeline

generator = pipeline("text-generation", model="./mini-gpt-finetuned")
output = generator("Votre prompt ici", max_length=100)
print(output[0]["generated_text"])
```

## Commandes utiles

```bash
# Activer l'environnement
source .venv/bin/activate

# Désactiver
deactivate

# Vérifier l'installation
python -c "import transformers; print(transformers.__version__)"
python -c "import torch; print(torch.__version__)"
```

## Dépendances principales

- transformers
- datasets
- torch
- accelerate
- sentencepiece

## Référence

Voir [InstructionMiniProjet.pdf](InstructionMiniProjet.pdf) pour le guide complet.
