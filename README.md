# Ordonnancement de Tâches en Temps Réel

Ce projet est une application web développée avec [Streamlit](https://streamlit.io/) pour visualiser l'ordonnancement de tâches en temps réel. Il permet de comparer quatre algorithmes courants d'ordonnancement : **FCFS** (First-Come, First-Served), **SJF** (Shortest Job First), **DM** (Deadline Monotonic), et **RM** (Rate Monotonic). L'application génère un diagramme de Gantt interactif pour visualiser les exécutions de tâches en fonction de l'algorithme choisi.

## Fonctionnalités

- **Saisie des Tâches** : L'utilisateur peut entrer plusieurs tâches avec les informations suivantes :
  - Nom de la tâche
  - Temps d'arrivée
  - Temps d'exécution
  - Date limite
  - Période
- **Choix de l'Algorithme d'Ordonnancement** : Sélection de l'algorithme pour trier les tâches :
  - **FCFS** : Tâche la plus ancienne en premier.
  - **SJF** : Tâche avec le plus court temps d'exécution en premier.
  - **DM** : Tâche avec la date limite la plus proche en premier.
  - **RM** : Tâche avec la plus petite période en premier.
- **Diagramme de Gantt** : Affichage d'un diagramme de Gantt pour visualiser l'ordonnancement des tâches.

## Prérequis

- Python 3.7 ou plus
- Streamlit
- Pandas
- Matplotlib
- Numpy

### Installation de l’Environnement
### Cloner le dépôt 
git clone https://github.com/adnan-khadija/RealTimeTaskScheduler.git
### Accéder au répertoire du projet
cd RealTimeTaskScheduler
### Active l’environnement virtuel
.\venv\Scripts\activate
### Installation des dépendances :
pip install -r requirements.txt

Ouvre le navigateur et accède à http://localhost:8501 pour utiliser l’application.

## Auteur 
[Khadija ADNAN](https://github.com/adnan-khadija)
