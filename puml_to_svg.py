import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
import threading
import plantuml

class PumlToSvgConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertisseur PUML vers SVG")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        self.selected_files = []
        self.server = plantuml.PlantUML(url='http://www.plantuml.com/plantuml/svg/')

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Style
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 10))
        style.configure('TLabel', font=('Arial', 11))

        # Boutons
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=5)

        self.select_btn = ttk.Button(
            buttons_frame,
            text="Sélectionner fichier(s) PUML",
            command=self.select_files
        )
        self.select_btn.pack(side=tk.LEFT, padx=5)

        self.convert_btn = ttk.Button(
            buttons_frame,
            text="Convertir en SVG",
            command=self.start_conversion,
            state=tk.DISABLED
        )
        self.convert_btn.pack(side=tk.LEFT, padx=5)

        # Label d'information
        self.info_label = ttk.Label(main_frame, text="Aucun fichier sélectionné")
        self.info_label.pack(fill=tk.X, pady=5)

        # Barre de progression
        self.progress = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.progress.pack(fill=tk.X, pady=5)

        # Zone de texte pour les logs
        self.log_frame = ttk.LabelFrame(main_frame, text="Logs")
        self.log_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.log_text = scrolledtext.ScrolledText(self.log_frame, wrap=tk.WORD, width=70, height=15)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.log_text.config(state=tk.DISABLED)

    def select_files(self):
        self.selected_files = filedialog.askopenfilenames(
            title="Sélectionner des fichiers PUML",
            filetypes=[("Fichiers PlantUML", "*.puml"), ("Tous les fichiers", "*.*")]
        )

        if self.selected_files:
            self.convert_btn.config(state=tk.NORMAL)
            self.info_label.config(text=f"{len(self.selected_files)} fichier(s) sélectionné(s)")

            self.log_text.config(state=tk.NORMAL)
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "Fichiers sélectionnés:\n")

            for file in self.selected_files:
                self.log_text.insert(tk.END, f"- {os.path.basename(file)}\n")

            self.log_text.config(state=tk.DISABLED)
        else:
            self.convert_btn.config(state=tk.DISABLED)
            self.info_label.config(text="Aucun fichier sélectionné")

    def start_conversion(self):
        """Démarrer la conversion dans un thread séparé pour ne pas bloquer l'interface."""
        self.convert_btn.config(state=tk.DISABLED)
        self.select_btn.config(state=tk.DISABLED)
        self.progress['value'] = 0
        self.progress['maximum'] = len(self.selected_files)

        # Vider les logs
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)

        # Lancer la conversion dans un thread séparé
        conversion_thread = threading.Thread(target=self.convert_files)
        conversion_thread.daemon = True
        conversion_thread.start()

    def convert_files(self):
        """Convertir tous les fichiers sélectionnés."""
        for i, puml_file in enumerate(self.selected_files):
            try:
                self.convert_file(puml_file)

                # Mettre à jour la barre de progression
                self.root.after(0, lambda val=i+1: self.update_progress(val))
            except Exception as e:
                self.add_log(f"Erreur lors de la conversion de {os.path.basename(puml_file)}: {str(e)}", error=True)

        self.root.after(0, self.conversion_completed)

    def convert_file(self, puml_file):
        """Convertir un fichier PUML en SVG."""
        svg_file = os.path.splitext(puml_file)[0] + '.svg'

        try:
            # Lire le contenu du fichier PUML
            with open(puml_file, 'r', encoding='utf-8') as f:
                puml_content = f.read()

            # Générer le SVG
            svg = self.server.processes(puml_content)

            # Écrire le fichier SVG
            with open(svg_file, 'wb') as f:
                f.write(svg)

            self.add_log(f"Converti: {os.path.basename(puml_file)} -> {os.path.basename(svg_file)}")

        except UnicodeDecodeError:
            # Essayer avec une autre encodage si utf-8 échoue
            with open(puml_file, 'r', encoding='latin-1') as f:
                puml_content = f.read()

            svg = self.server.processes(puml_content)

            with open(svg_file, 'wb') as f:
                f.write(svg)

            self.add_log(f"Converti (encodage latin-1): {os.path.basename(puml_file)} -> {os.path.basename(svg_file)}")

    def add_log(self, message, error=False):
        """Ajouter un message dans la zone de logs."""
        def _add():
            self.log_text.config(state=tk.NORMAL)
            if error:
                self.log_text.insert(tk.END, f"ERREUR: {message}\n", "error")
                self.log_text.tag_config("error", foreground="red")
            else:
                self.log_text.insert(tk.END, f"{message}\n")
            self.log_text.see(tk.END)  # Défiler jusqu'à la fin
            self.log_text.config(state=tk.DISABLED)

        self.root.after(0, _add)

    def update_progress(self, value):
        """Mettre à jour la barre de progression."""
        self.progress['value'] = value

    def conversion_completed(self):
        """Action à effectuer lorsque la conversion est terminée."""
        self.add_log("\nConversion terminée!")
        self.select_btn.config(state=tk.NORMAL)
        self.convert_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = PumlToSvgConverter(root)
    root.mainloop()
