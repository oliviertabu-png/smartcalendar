import sqlite3


def get_connection():
    return sqlite3.connect("smartcalendar.db")


def init_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        email TEXT NOT NULL,
        role TEXT NOT NULL,
        google_linked BOOLEAN DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS promotions(
        id_promotion INTEGER PRIMARY KEY,
        nom_promo TEXT NOT NULL,
        annee_academique TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS etudiants(
        id_etudiant INTEGER PRIMARY KEY,
        matricule TEXT UNIQUE,
        nom TEXT,
        prenom TEXT,
        email TEXT,
        id_promotion INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enseignants(
        id_enseignant INTEGER PRIMARY KEY,
        nom TEXT,
        prenom TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS unite_enseignement(
        id_ue INTEGER PRIMARY KEY,
        code_ue TEXT,
        intitule TEXT,
        credits_ects INTEGER,
        id_promotion INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cours(
        id_cours INTEGER PRIMARY KEY,
        intitule_cours TEXT,
        volume_horaire INTEGER,
        id_ue INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS seances(
        id_seance INTEGER PRIMARY KEY,
        titre TEXT,
        date TEXT,
        heure_debut TEXT,
        heure_fin TEXT,
        salle TEXT,
        statut_synchro TEXT,
        type TEXT,
        id_cours INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notifications(
        id_notif INTEGER PRIMARY KEY,
        type TEXT,
        destinataires TEXT,
        message TEXT,
        date_envoi TEXT
    )
    """)

    conn.commit()
    conn.close()