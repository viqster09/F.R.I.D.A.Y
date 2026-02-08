import subprocess
import os
import string
import pyttsx3
import ctypes
import sounddevice as sd
import numpy as np
from ctypes import windll
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from tkinter import Tk
import tkinter.ttk as ttk
from speech_recognition import Recognizer, Microphone
from webbrowser import open_new
import time

class VocalSearch:
    def __init__(self, window):
        self.engine = pyttsx3.init()  # Initialisation du moteur de synthèse vocale
        self.rate = self.engine.getProperty('rate')
        self.window = window
        self.window.geometry('145x135')
        self.window.resizable(0, 0)
        self.window.withdraw()

        with open('C:\\Users\\33629\\Documents\\retrans vocal python\\lang.txt') as f:
            for line in f:
                self.lang = line.strip()

        self.recognizer = Recognizer()
        self.microphone = Microphone()
        self.say("Initialisation des fichiers")
        self.lister_fichiers_video()
        self.lister_fichiers_exe_autres()
        self.full_system_checkup()
        self.main()

    def say(self, text):
        """Fonction de synthèse vocale avec pyttsx3"""
        self.engine.say(text)
        self.engine.runAndWait()

    def lister_fichiers_video(self):
        """Liste tous les fichiers vidéo sur le système"""
        disques = [drive + 'C:\\' for drive in string.ascii_uppercase if os.path.exists(drive + 'C:\\')]

        # Chemin d'accès au répertoire du script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fichier_video = os.path.join(script_dir, 'liste_videos.txt')
        fichier_autres = os.path.join(script_dir, 'liste_autres.txt')

        # Ouverture des fichiers en mode écriture
        with open(fichier_video, 'w', encoding='utf-8') as fichier_video, open(fichier_autres, 'w') as fichier_autres:
            for disque in disques:
                for dossier_parent, sous_repertoires, fichiers in os.walk(disque):
                    for nom_fichier in fichiers:
                        chemin_complet = os.path.join(dossier_parent, nom_fichier)
                        _, extension = os.path.splitext(nom_fichier)
                        if extension[1:].lower() in ['mp4', 'mkv', 'avi', 'mov', 'wmv']:
                            fichier_video.write(chemin_complet + '\n')
                        else:
                            fichier_autres.write(chemin_complet + '\n')

    def lister_fichiers_exe_autres(self):
        """Liste tous les fichiers exécutables et autres sur le système"""
        # Liste des disques disponibles sur le système
        disques = [drive + 'C:\\' for drive in string.ascii_uppercase if os.path.exists(drive + 'C:\\')]

        # Chemin d'accès au répertoire du script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fichier_exe = os.path.join(script_dir, 'liste_executable.txt')
        fichier_autres = os.path.join(script_dir, 'liste_autres_executable.txt')

        with open(fichier_exe, 'w', encoding='utf-8') as self.fichier_exe, open(fichier_autres, 'w', encoding='utf-8') as self.fichier_autres:
            # Parcours de chaque disque séparément
            for disque in disques:
                # Parcours de tous les dossiers et sous-dossiers du disque
                for dossier_parent, sous_repertoires, fichiers in os.walk(disque):
                    for nom_fichier in fichiers:
                        chemin_complet = os.path.join(dossier_parent, nom_fichier)
                        _, extension = os.path.splitext(nom_fichier)
                        if extension[1:] in ['lnk']:  # Si c'est un fichier exécutable
                            self.fichier_exe.write(chemin_complet + '\n')
                        else:
                            self.fichier_autres.write(chemin_complet + '\n')


    def full_system_checkup(self):
        """Vérifie si l'utilisateur est administrateur et lance un scan système"""
        if not self.is_admin():
            self.say("Pour effectuer la vérification complète du système, vous devez exécuter le script en tant qu'administrateur.")
            return

        self.say("Vérification complète du système en cours. Veuillez patienter.")
        try:
            subprocess.run(["sfc", "/scannow"], check=True, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.say("Vérification terminée. Aucun fichier système corrompu détecté.")
        except subprocess.CalledProcessError:
            self.say("Vérification terminée. Des fichiers système corrompus ont été détectés.")

    def is_admin(self):
        """Vérifie si l'utilisateur a des privilèges administrateur"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def rechercher_et_lancer(self, nom_film):
        """Recherche et lance un fichier vidéo"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fichier_video = os.path.join(script_dir, 'liste_videos.txt')

        with open(fichier_video, 'r') as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                chemin_film = ligne.strip()
                nom_fichier = os.path.basename(chemin_film)
                if nom_film.lower() in nom_fichier.lower():
                    os.system(f'start "" "{chemin_film}"')
                    self.main()

    def main(self): 
        """Lance le processus principal"""
        self.say("Bonjour monsieur")
        self.listen_continuous()

    def say_yes_sir(self):
        """Réponse affirmative avec synthèse vocale"""
        self.say("Oui monsieur")
        self.window.after(100, self.search)

    def search(self):
        """Recherche sur Google en fonction de la commande vocale"""
        self.recognizer = Recognizer()
        with Microphone() as source:
            self.audio = self.recognizer.listen(source)
        try:
            self.text = self.recognizer.recognize_google(self.audio, language=self.lang)
            self.link = "https://www.google.com/search?q=" + self.text.replace(' ', '+')
            open_new(self.link)
            self.main()
        except Exception as ex:
            self.say_no()

    def decrease(self):
        """Diminue le volume"""
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        current_volume = volume.GetMasterVolumeLevelScalar()
        new_volume = max(current_volume - 0.10, 0.0)
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        self.say("Volume de l'ordinateur diminué")

    def increase_volume(self):
        """Augmente le volume"""
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        current_volume = volume.GetMasterVolumeLevelScalar()
        new_volume = min(current_volume + 0.10, 1.0)
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        self.say("Volume de l'ordinateur augmenté")

    def say_no(self):
        """Réponse négative en cas de non compréhension"""
        self.say("Je n'ai pas compris monsieur")
        self.window.after(100, self.search)

    def restart_app(self):
        """Redémarre l'application"""
        self.window.destroy()
        root = Tk()
        app = VocalSearch(root)
        root.mainloop()

    def thanks(self):
        """Réponse de remerciement"""
        self.say("De rien Monsieur")
        self.main()

    def lock_screen(self):
        """Verrouille l'écran de l'ordinateur"""
        self.say("Verrouillage en cours")
        try:
            windll.user32.LockWorkStation()
        except Exception as ex:
            print(f"Erreur lors du verrouillage de l'écran : {ex}")

    def you_too(self):
        """Réponse complimentaire"""
        self.say("Vous aussi vous êtes le meilleur.")
        self.main()

    def open_spotify(self):
        """Ouvre un fichier audio spécifique"""
        self.say("Bonjour Monsieur")
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Thunderstruck.mp3")  # Fichier audio à lancer
        try:
            subprocess.Popen(["start", " ", file_path], shell=True)
            self.main()
        except Exception as ex:
            print(f"Erreur lors du lancement du fichier : {ex}")
            self.say_no()

    def no_volume(self):
        """Coupe le volume de l'ordinateur"""
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(0.0, None)
        self.say("Volume de l'ordinateur coupé")
        self.main()

    def run_exe(self, nom_programme):
        """Lance un programme exécutable en fonction du nom"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fichier_exe = os.path.join(script_dir, 'liste_executable.txt')

        with open(fichier_exe, 'r') as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                chemin_exe = ligne.strip()
                nom_fichier = os.path.basename(chemin_exe)
                if nom_programme.lower() in nom_fichier.lower():
                    os.system(f'start "" "{chemin_exe}"')
                    self.main()

        print(f"Le programme '{nom_programme}' n'a pas été trouvé.")
        return False

    def yes(self):
        """Réponse affirmative pour une action"""
        self.say("Oui monsieur ?")
        self.window.after(100, self.search)

    def listen_continuous(self):
        """Écoute en continu les commandes vocales"""
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            while True:
                try:
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio, language=self.lang).lower()

                    # Analyse de la commande vocale
                    if 'allume' in command:
                        self.run_exe(command)
                    elif 'mute' in command:
                        self.no_volume()
                    elif 'ma gueule' in command:
                        self.yes()
                    elif 'cherche' in command:
                        self.search()
                    elif 'papa est rentré' in command:
                        self.open_spotify()
                    elif 'baisse le son' in command:
                        self.decrease()
                    elif 'monte le son' in command:
                        self.increase_volume()
                    elif 'verrouille' in command:
                        self.lock_screen()
                    elif 'merci' in command:
                        self.say("De rien monsieur")
                    elif 'reboot' in command:
                        self.restart_app()
                    elif 'éteins' in command:
                        self.say("À bientôt !")
                        break  # Arrête l'écoute et termine le programme

                except Exception as ex:
                    print(f"Erreur dans la reconnaissance vocale : {ex}")
                    self.say("Je n'ai pas compris, pouvez-vous répéter ?")

    def restart_app(self):
        """Redémarre l'application"""
        self.window.destroy()
        root = Tk()
        app = VocalSearch(root)
        root.mainloop()


root = Tk()
app = VocalSearch(root)
root.mainloop()
