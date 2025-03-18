# Guide de contribution

Merci de votre intérêt pour contribuer à PUML to SVG Converter ! Voici quelques directives pour vous aider.

## Comment contribuer

1. **Signaler des bugs**
   - Vérifiez d'abord si le bug n'a pas déjà été signalé
   - Utilisez le modèle de rapport de bug pour fournir des informations détaillées

2. **Proposer des fonctionnalités**
   - Décrivez clairement la fonctionnalité et son utilité
   - Si possible, proposez une approche pour l'implémentation

3. **Soumettre des pull requests**
   - Assurez-vous que votre code suit le style du projet
   - Incluez des tests pour les nouvelles fonctionnalités
   - Référencez les issues pertinentes

## Configuration de l'environnement de développement

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votreusername/puml-to-svg.git
   cd puml-to-svg
   ```

2. Installez les dépendances de développement :
   ```bash
   pip install -r requirements-dev.txt
   # ou
   uv pip install -r requirements-dev.txt
   ```

## Style de code

- Suivez PEP 8 pour le style Python
- Utilisez des noms de variables et fonctions descriptifs
- Commentez votre code si nécessaire

## Tests

- Ajoutez des tests pour les nouvelles fonctionnalités
- Exécutez les tests avant de soumettre une PR :
  ```bash
  pytest
  ```

## Merci pour votre contribution !
