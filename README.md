# PUML to SVG Converter

Un outil graphique simple pour convertir des diagrammes PlantUML (.puml) en images vectorielles SVG.

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Python](https://img.shields.io/badge/Python-3.13+-green)

## 📋 Description

Ce convertisseur permet de transformer facilement vos fichiers PlantUML en fichiers SVG grâce à une interface graphique intuitive. Il utilise le service web PlantUML pour générer des diagrammes SVG de haute qualité.

### Fonctionnalités

- Interface graphique simple avec Tkinter
- Sélection multiple de fichiers
- Conversion en lot
- Barre de progression
- Journalisation des opérations
- Gestion automatique des encodages de fichiers

## 📥 Installation

### Prérequis

- Python 3.13 ou supérieur
- uv

### Avec uv

```bash
uv sync
```

## 🚀 Utilisation

### Lancement de l'application

```bash
uv run puml_to_svg.py
```

### Conversion de fichiers

1. Cliquez sur "Sélectionner fichier(s) PUML" pour choisir un ou plusieurs fichiers .puml
2. Cliquez sur "Convertir en SVG" pour démarrer la conversion
3. Suivez la progression dans la barre de progression et les logs
4. Les fichiers SVG sont générés dans le même dossier que les fichiers PUML d'origine

## 🔧 Dépendances

- plantuml
- tkinter (inclus dans la bibliothèque standard Python)

## 👨‍💻 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
