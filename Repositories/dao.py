# Exercice 1
## Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml

# Avec Python, les class Interfaces peuvent être implémentées comme des classes abstraites
# heritant de Protocol
import sqlite3
from typing import Protocol

from Models import EnseignantDTO, EtudiantDTO, UserDTO


class DAO:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._setup_db()

    def _setup_db(self):
        cursor = self.conn.cursor()

        # Réquêtes de création lors de l'initialisation des tables si elles n'existent pas
        # 1. Création de la table Users sur base de la classe UserDTO

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, role TEXT, email TEXT, google_linked BOOLEAN)"
        )

        # 2. Création de la table Etudiant
        cursor.execute("""
CREATE TABLE IF NOT EXISTS etudiant (
    id_etudiant INTEGER PRIMARY KEY,
    matricule TEXT,
    nom TEXT,
    prenom TEXT,
    email TEXT,
    id_promotion INTEGER
)
""")
        # 3. Création de la table Enseignant
        cursor.execute("""
CREATE TABLE IF NOT EXISTS enseignant (
    id_enseignant INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    email TEXT,
    id_ue INTEGER
)
""")
        # 4. Création de la table Promotion
        cursor.execute("""
CREATE TABLE IF NOT EXISTS promotion (
    id_promotion INTEGER PRIMARY KEY,
    nom_promo TEXT,
    annee_academique TEXT
)
""")

        # 5. Création de la table UniteEnseignement
        cursor.execute("""
CREATE TABLE IF NOT EXISTS unite_enseignement (
    id_ue INTEGER PRIMARY KEY,
    code_ue TEXT,
    intitule TEXT,
    credits_ects INTEGER,
    id_promotion INTEGER
)
""")
        # 6. Création de la table Cours
        cursor.execute("""
CREATE TABLE IF NOT EXISTS cours (
    id_cours INTEGER PRIMARY KEY,
    intitule_cours TEXT,
    volume_horaire INTEGER,
    id_ue INTEGER
)
""")
        # 7. Création de la table Seance
cursor.execute("""
CREATE TABLE IF NOT EXISTS seance (
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
        # Confirmation des réquêtes dans la transaction
        self.conn.commit()


class BaseDAO(Protocol):
    def get_by_id(self, id) -> DAO: ...

    def get_all(self) -> list[DAO]: ...

    def save(self, obj) -> None: ...

    def delete(self, id) -> None: ...


class UserDAO(DAO):
    def __init__(
        self,
    ):
        pass

    def get_by_id(self, id) -> UserDTO: ...

    def get_all(self) -> list[UserDTO]: ...

    def save(self, UserDTO) -> None: ...

    def delete(self, id: int) -> None: ...

    def get_by_email(self, email) -> UserDTO: ...


class EtudiantDAO(DAO):
    def __init__(self):
        pass

    def get_by_id(self, id) -> EtudiantDTO: ...

    def get_all(self) -> list[EtudiantDTO]: ...

    def save(self, UserDTO) -> None: ...

    def delete(self, id: int) -> None: ...

    def get_by_promotion(self, promotion_id) -> list[EtudiantDTO]: ...


class EnseignantDAO(DAO):
    def __init__(self):
        pass

    def get_by_id(self, id) -> EnseignantDTO: ...

    def get_all(self) -> list[EnseignantDTO]: ...

    def save(self, EnseignantDAO) -> None: ...

    def delete(self, id_enseignant) -> None: ...

    def get_by_ue(self, ue_id) -> list[EnseignantDTO]: ...


class PromotionDAO(DAO):
    def __init__(self) -> None:
        pass


class EventDAO(DAO):
    def __init__(
        self,
    ):
        pass
