import os
import plantuml
from glob import glob

# Initialiser le serveur PlantUML (local ou en ligne)
server = plantuml.PlantUML(url='http://www.plantuml.com/plantuml/svg/')

# Convertir un seul fichier
def convert_file(puml_file):
    svg_file = os.path.splitext(puml_file)[0] + '.svg'
    with open(puml_file, 'r') as f:
        puml_content = f.read()

    # Générer le SVG
    svg = server.processes(puml_content)

    # Écrire le fichier SVG
    with open(svg_file, 'wb') as f:
        f.write(svg)

    print(f"Converti: {puml_file} -> {svg_file}")

# Traiter tous les fichiers .puml d'un dossier
def convert_directory(directory):
    for puml_file in glob(f"{directory}/*.puml"):
        convert_file(puml_file)

# Utilisation
if __name__ == "__main__":
    convert_directory("./diagrammes")
