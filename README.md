🎤 Vocal Assistant - F.R.I.D.A.Y.

Bienvenue dans F.R.I.D.A.Y., votre assistant vocal intelligent qui vous permet de contrôler votre ordinateur simplement avec votre voix ! 📱💻

Ce script Python transforme votre PC en un assistant numérique personnel, capable de faire des actions comme :

Lancer des vidéos 🎬

Contrôler le volume 🔊

Effectuer des recherches sur Google 🔍

Jouer de la musique 🎶

Verrouiller votre écran 🔒

Et plus encore ! Il suffit de parler à votre ordinateur, et il exécutera vos commandes automatiquement. 😎

📦 Prérequis

Installer les dépendances

Vous pouvez installer toutes les dépendances nécessaires en une seule commande. Ouvrez votre terminal/bash et entrez :

pip install pyttsx3 speechrecognition pycaw sounddevice transformers


Les modules suivants seront installés :

pyttsx3 : Pour la synthèse vocale (répondre à vos commandes).

speechrecognition : Pour la reconnaissance vocale.

pycaw : Pour gérer le volume audio du système.

sounddevice : Pour gérer le microphone.

transformers : Si vous souhaitez ajouter des capacités avancées en NLP (facultatif).

🚀 Utilisation

Cloner ou télécharger le projet
Si vous ne l'avez pas encore fait, clonez ce projet via Git :

git clone https://github.com/votre-repository/vocal-assistant.git
cd vocal-assistant


Lancer le script

Une fois les modules installés, lancez le script Python. Vous n'avez qu'à exécuter le fichier .py :

python F.R.I.D.A.Y.py


Le script démarrera automatiquement et attendra vos commandes vocales. 🗣️

🎙️ Fonctionnalités principales

Voici quelques-unes des commandes vocales que vous pouvez utiliser pour interagir avec votre assistant vocal :

1. Contrôler le Volume

Baisser le volume : "Baisse le son" 🔉

Augmenter le volume : "Monte le son" 🔊

Couper le son : "Mute le son" 🚫🔊

2. Lancer un film 🎬

Pour lancer un film spécifique sur votre PC, vous pouvez dire :

"Lance [Nom du film]" 🎥

Exemple : "Lance Titanic" 🛳️

3. Recherche sur Google 🔍

Pour faire une recherche instantanée sur Google, dites simplement :

"Cherche [terme de recherche]" 🕵️‍♂️

Exemple : "Cherche les dernières nouvelles" 📰

4. Lecture de musique 🎶

Votre assistant peut jouer une chanson à l'aide de commandes vocales comme :

"Papa est rentré" 🎸

Cela lancera la musique Thunderstruck en guise de bienvenue ! ⚡

5. Verrouillage de l'écran 🔒

Si vous voulez sécuriser rapidement votre PC, dites simplement :

"Verrouille mon écran" 🛡️

💻 Structure du Code

Le script utilise plusieurs fonctions pour exécuter diverses commandes :

lister_fichiers_video(): Liste les vidéos disponibles sur votre PC.

lister_fichiers_exe_autres(): Lister les programmes exécutables (comme les raccourcis).

full_system_checkup(): Vérifie l'intégrité du système.

rechercher_et_lancer(): Lance un film ou une vidéo.

say(): Utilise la synthèse vocale pour répondre à l'utilisateur.

listen_continuous(): Écoute en permanence les commandes vocales.

⚙️ Options avancées (facultatives)
Vérification complète du système

Pour effectuer une vérification complète du système, vous pouvez utiliser la commande :

python F.R.I.D.A.Y.py --check-system


Cela va exécuter la commande sfc /scannow et vérifier l'intégrité des fichiers système. 🔧

🧑‍💻 Contribuer

Vous êtes invité à contribuer au projet ! Si vous avez des idées d'amélioration ou des fonctionnalités à ajouter, vous pouvez créer une Pull Request ou soumettre un issue.

Comment contribuer ?

Si vous voulez apporter des modifications au projet, voici les étapes à suivre avec Git.

Forkez le repo sur GitHub (cliquez sur le bouton "Fork" en haut à droite de la page du projet).

Clonez votre fork localement :

git clone https://github.com/votre-utilisateur/vocal-assistant.git
cd vocal-assistant


Créez une nouvelle branche pour votre fonctionnalité :

git checkout -b feature/ma-nouvelle-fonctionnalité


Faites vos modifications : Ajoutez ou modifiez les fichiers comme bon vous semble.

Committez vos changements :

git add .
git commit -m "Ajout de ma nouvelle fonctionnalité"


Pushez vos modifications vers GitHub :

git push origin feature/ma-nouvelle-fonctionnalité


Ouvrez une Pull Request sur GitHub en cliquant sur "New Pull Request".

📜 Licence

Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.

💬 Aide

Si vous avez des questions ou des problèmes avec le code, n'hésitez pas à ouvrir une issue sur GitHub ou à me contacter directement. 😄

📢 Exemple de commande bash (lancer le script)
# Assurez-vous que le script est dans le bon répertoire
cd /chemin/vers/votre/projet

# Exécuter le script
python F.R.I.D.A.Y.py

🎉 Amusez-vous bien avec votre nouvel assistant vocal !
