class EventDAO:

    def get_all(self):

        return [
            {
                "titre": "Programmation Python",
                "date": "2026-06-10"
            },
            {
                "titre": "Base de données",
                "date": "2026-06-11"
            }
        ]

from database.db import get_connection


class EventDAO:

    def __init__(self):
        self.conn = get_connection()

    def get_all(self):

        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT id_seance,
                   titre,
                   date,
                   heure_debut,
                   heure_fin,
                   salle
            FROM seance
        """)

        return cursor.fetchall()

    def add_event(
        self,
        titre,
        date,
        heure_debut,
        heure_fin,
        salle
    ):

        cursor = self.conn.cursor()

        cursor.execute("""
            INSERT INTO seance(
                titre,
                date,
                heure_debut,
                heure_fin,
                salle
            )
            VALUES (?, ?, ?, ?, ?)
        """,
        (
            titre,
            date,
            heure_debut,
            heure_fin,
            salle
        ))

        self.conn.commit()        
from dao.event_dao import EventDAO

dao = EventDAO()

dao.add_event(
    "Python",
    "2026-06-10",
    "08:00",
    "10:00",
    "B1"
)

dao.add_event(
    "Base de données",
    "2026-06-11",
    "10:00",
    "12:00",
    "B2"
)        