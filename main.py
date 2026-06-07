import flet as ft

def main(page: ft.Page):

    page.title = "SmartCalendar"
    page.window.width = 1400
    page.window.height = 800

    # Menu latéral
    menu = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.HOME,
                label="Accueil"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.CALENDAR_MONTH,
                label="Calendrier"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SCHOOL,
                label="Cours"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PEOPLE,
                label="Étudiants"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PERSON,
                label="Enseignants"
            ),
        ]
    )

    # Cartes statistiques
    stats = ft.Row(
        [
            ft.Card(
                content=ft.Container(
                    width=220,
                    padding=20,
                    content=ft.Column([
                        ft.Text("Étudiants", size=20),
                        ft.Text("120", size=30)
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    width=220,
                    padding=20,
                    content=ft.Column([
                        ft.Text("Enseignants", size=20),
                        ft.Text("15", size=30)
                    ])
                )
            ),
            ft.Card(
                content=ft.Container(
                    width=220,
                    padding=20,
                    content=ft.Column([
                        ft.Text("Cours", size=20),
                        ft.Text("35", size=30)
                    ])
                )
            ),
        ]
    )

    # Liste des séances
    seances = ft.Column(
        [
            ft.Card(
                content=ft.ListTile(
                    leading=ft.Icon(ft.Icons.EVENT),
                    title=ft.Text("Programmation Python"),
                    subtitle=ft.Text("08:00 - 10:00 | Salle A1")
                )
            ),
            ft.Card(
                content=ft.ListTile(
                    leading=ft.Icon(ft.Icons.EVENT),
                    title=ft.Text("Base de Données"),
                    subtitle=ft.Text("10:00 - 12:00 | Salle B2")
                )
            ),
        ]
    )

    contenu = ft.Column(
        [
            ft.Text(
                "SMARTCALENDAR",
                size=35,
                weight=ft.FontWeight.BOLD
            ),
            ft.Divider(),
            stats,
            ft.Text(
                "Séances du jour",
                size=24,
                weight=ft.FontWeight.BOLD
            ),
            seances
        ],
        expand=True
    )

    page.add(
        ft.Row(
            [
                menu,
                ft.VerticalDivider(width=1),
                contenu
            ],
            expand=True
        )
    )

ft.app(target=main)