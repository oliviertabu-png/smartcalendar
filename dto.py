from dataclasses import dataclass
from enum import Enum
from datetime import datetime, date


class TypeSeance(Enum):
    COURS_MAGISTRAL = "COURS_MAGISTRAL"
    TD = "TD"
    TP = "TP"
    EXAMEN = "EXAMEN"
    AUTRE_EVENEMENT = "AUTRE_EVENEMENT"


@dataclass
class UserDTO:
    id: int
    email: str
    role: str
    google_linked: bool


@dataclass
class EtudiantDTO:
    id_etudiant: int
    matricule: str
    nom: str
    prenom: str
    email: str


@dataclass
class EnseignantDTO:
    id_enseignant: int
    nom: str
    prenom: str
    email: str


@dataclass
class PromotionDTO:
    id_promotion: int
    nom_promo: str
    annee_academique: str


@dataclass
class UniteEnseignementDTO:
    id_ue: int
    code_ue: str
    intitule: str
    credits_ects: int


@dataclass
class CoursDTO:
    id_cours: int
    intitule_cours: str
    volume_horaire: int


@dataclass
class NotificationDTO:
    id_notif: int
    type: str
    destinataires: list[str]
    message: str
    date_envoi: datetime


@dataclass
class EventDTO:
    id_seance: int
    titre: str
    date: date
    heure_debut: str
    heure_fin: str
    salle: str
    statut_synchro: str
    type: TypeSeance