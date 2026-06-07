import flet as ft
from dao.event_dao import EventDAO


def build_calendar():

    dao = EventDAO()

    events = dao.get_all()

    controls = []

    for event in events:

        controls.append(
            ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Column([
                        ft.Text(event["titre"]),
                        ft.Text(event["date"])
                    ])
                )
            )
        )

    return ft.Column(controls)

    def build_etudiants():

    return ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Matricule")),
            ft.DataColumn(ft.Text("Nom")),
            ft.DataColumn(ft.Text("Prénom")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("2025001")),
                    ft.DataCell(ft.Text("TABU")),
                    ft.DataCell(ft.Text("Olivier"))
                ]
            )
        ]
    )
import flet as ft

from dao.event_dao import EventDAO


def build_calendar():

    dao = EventDAO()

    events = dao.get_all()

    cards = []

    for event in events:

        cards.append(
            ft.Card(
                content=ft.Container(
                    padding=15,
                    content=ft.Column(
                        [
                            ft.Text(
                                event[1],
                                size=18,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(f"Date : {event[2]}"),
                            ft.Text(f"Heure : {event[3]} - {event[4]}"),
                            ft.Text(f"Salle : {event[5]}")
                        ]
                    )
                )
            )
        )

    return ft.Column(cards)    