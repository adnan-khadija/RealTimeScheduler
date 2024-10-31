import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Ordonnancement des tâches en temps réel")
st.header("Saisir les tâches")

# Entrée du nombre de tâches
num_tasks = st.number_input("Nombre de tâches", min_value=1, max_value=20, value=5)
tasks = []

# Saisie des tâches
for i in range(num_tasks):
    with st.expander(f'Tâche {i + 1}'):
        task_name = st.text_input(f'Nom de la tâche {i + 1}', f'Tâche {i + 1}')
        arrival_time = st.number_input(f'Temps d\'arrivée de la tâche {i + 1}', min_value=0)
        burst_time = st.number_input(f'Temps d\'exécution de la tâche {i + 1}', min_value=1)
        deadline = st.number_input(f'Date limite de la tâche {i + 1}', min_value=1)
        period = st.number_input(f'Période de la tâche {i + 1}', min_value=1)
        tasks.append((task_name, arrival_time, burst_time, deadline, period))

# Affichage des tâches dans un tableau
df_tasks = pd.DataFrame(tasks, columns=['Nom de la tâche', 'Temps d\'arrivée', 'Temps d\'exécution', 'Date limite', 'Période']) 
st.write(df_tasks)

# Sélection de l'algorithme d'ordonnancement
st.header("Choisir l'algorithme d'ordonnancement")
algorithm = st.selectbox('Algorithme', ['FCFS', 'SJF', 'DM', 'RM'])

# Fonction d'ordonnancement des tâches
def schedule_tasks(tasks, algorithm):
    if algorithm == 'FCFS':
        tasks.sort(key=lambda x: x[1])  # Trier par temps d'arrivée
    elif algorithm == 'SJF':
        tasks.sort(key=lambda x: x[2])  # Trier par temps d'exécution
    elif algorithm == 'DM':
        tasks.sort(key=lambda x: x[3])  # Trier par date limite
    elif algorithm == 'RM':
        tasks.sort(key=lambda x: x[4])  # Trier par période
    return tasks

# Ordonnancement selon l'algorithme choisi
scheduled_tasks = schedule_tasks(tasks, algorithm)

# Fonction pour tracer le diagramme de Gantt
def draw_gantt_chart(tasks):
    fig, gnt = plt.subplots()
    gnt.set_xlabel("Temps")
    gnt.set_ylabel("Tâches")
    
    # Configuration des axes
    yticks = np.arange(1, len(tasks) + 1)
    gnt.set_yticks(yticks)
    gnt.set_yticklabels([task[0] for task in tasks])
    
    # Tracé des barres pour chaque tâche
    for i, task in enumerate(tasks):
        start_time = task[1]  # Temps d'arrivée
        duration = task[2]    # Temps d'exécution
        gnt.broken_barh([(start_time, duration)], (yticks[i] - 0.4, 0.8), facecolors=('tab:blue'))
    
    st.pyplot(fig)

# Affichage du diagramme de Gantt
st.header("Diagramme de Gantt")
draw_gantt_chart(scheduled_tasks)




