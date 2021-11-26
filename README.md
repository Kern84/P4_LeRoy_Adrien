# P4_LeRoy_Adrien

Projet 4

    Configuration pour execution du programme.

1 - Pour créer et activer l'environnement virtuel.

Créer un dossier pour le projet à l'endroit souhaité dans votre arborescence et s'y placer dans le terminal. Entrer la
ligne de commande : "python -m venv env". Entrer la ligne de commande : "source env/bin/activate" ; pour activer
l'environnement virtuel. Entrer la ligne de commande : "pip install -r requirements.txt" ; pour installer
automatiquement les packages requis à l'exécution du programme. Entrer la ligne de commande : "deactivate" ; pour
désactiver l'environnement virtuel, quand vous avez fini de consulter le projet.

2 - Pour exécuter le code d'application.

Dans le terminal, après avoir configuré l'environnement virtuel, se placer à la racine du répertoire du projet. Entrer
la ligne de commande : "python3 main.py" pour exécuter le script.

3 - Pour executer un nouveau rapport flake8.

Le repository contient un rapport flake8 qui n'affiche aucunes erreurs. Un nouveau rapport peut être généré en entrant
dans le terminal a la racine du dossier du projet, la ligne de commande : "flake8 --max-line-length=119 --format=html
--htmldir=flake-rapport --exclude=env/". Cette ligne de commande générera un nouveau rapport en accord avec les
caractéristiques demandées pour le projet.