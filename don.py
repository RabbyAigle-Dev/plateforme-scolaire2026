import streamlit as st
import sqlite3
import pandas as pd
st.set_page_config(page_title="Plateforme Scolaire.",page_icon="🎓",layout="wide")
conn = sqlite3.connect("school.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    postnom TEXT,
    prenom TEXT,
    sexe TEXT,
    classe TEXT,
    age INTEGER)""")
conn.commit()

st.image("XVIF6216.jpg",width=50)
st.sidebar.markdown("<h1 style='color:blue;'>🎓 Plateforme Scolaire</h1>", unsafe_allow_html=True)
menu = st.sidebar.radio("MENU",["Accueil","Ajouter un étudiant","Liste des étudiants","À propos"])
if menu == "Accueil":
    st.markdown("<h1 style='color:blue;'>Plateforme de Gestion Scolaire</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Étudiants", cursor.execute(
            "SELECT COUNT(*) FROM students").fetchone()[0])
    with col2:
        st.metric("Enseignants", "25")

    with col3:
        st.metric("Cours", "18")
    st.success("Bienvenue dans la plateforme scolaire. Développée par l'ingenieur Don Urbain Mutima!")
elif menu == "Ajouter un étudiant":
    st.header("Ajouter un étudiant")
    nom = st.text_input("Nom")
    postnom = st.text_input("Postnom")
    prenom = st.text_input("Prénom")
    sexe = st.selectbox("Sexe",["Masculin", "Féminin"])
    classe = st.selectbox("Classe",["L1","L2","L3","M1","M2"])
    age = st.number_input("Âge",15,60)
    if st.button("Enregistrer"):
        cursor.execute("""
        INSERT INTO students
        (nom,postnom,prenom,sexe,classe,age)
        VALUES(?,?,?,?,?,?)
        """,
        (nom,postnom,prenom,sexe,classe,age))
        conn.commit()
        st.success("Étudiant enregistré avec succès.")
elif menu == "Liste des étudiants":

    st.header("Liste des étudiants")

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    if len(data) == 0:
        st.warning("Aucun étudiant enregistré.")
    else:
        df = pd.DataFrame(data,columns=["ID","Nom","Postnom","Prénom","Sexe","Classe","Âge"])
        st.dataframe(df, use_container_width=True)

elif menu=="À propos":

    st.markdown("<h1 style='color:blue;'>À propos</h1>", unsafe_allow_html=True)

    st.write("""
    **Plateforme de Gestion Scolaire**

    Version 1.0 (2026)

    Créée pour faciliter la gestion des établissements scolaires.

    Développée par l'ingenieur Don Urbain Mutima

    Université de Lubumbashi

    Faculté des Sciences et Technologies

    E-mail: mutimadonurbain@gmail.com

    Tel: +243 802795223
    """)
st.sidebar.image("XVIF6216.jpg", width=170)
