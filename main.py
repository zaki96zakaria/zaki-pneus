import flet as ft
import json
import os

# Références Iris (exemple)
IRIS_REFS = [
    {"nom": "Iris 195/65R15 AllSeason", "code": "6191234567890"},
    {"nom": "Iris 205/55R16 Sport", "code": "6191234567891"},
    {"nom": "Iris 225/45R17 Winter", "code": "6191234567892"},
    {"nom": "Iris 185/65R15 Eco", "code": "6191234567893"},
    {"nom": "Iris 215/60R16 SUV", "code": "6191234567894"}
]

class TireApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "ZAKI PNEU - Gestion"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.window_width = 400
        self.page.window_height = 800
        self.page.window_resizable = True
        
        # Éléments d'interface principaux
        self.main_menu = None
        self.vente_section = None
        self.achat_section = None
        self.stock_section = None
        self.magasin_section = None
        self.iris_section = None
        
        # Champs de formulaire
        self.vente_nom_field = None
        self.vente_qte_field = None
        self.achat_nom_field = None
        self.achat_qte_field = None
        self.stock_search_field = None
        
        # Messages
        self.vente_message = None
        self.achat_message = None
        
        # Listes
        self.stock_list = None
        self.iris_list = None
        
        self.setup_ui()
        self.show_menu()
        
    def setup_ui(self):
        # Titre principal
        title = ft.Text(
            "ZAKI PNEU",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.ORANGE,
        )
        
        # Menu principal
        self.main_menu = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.ElevatedButton(
                                "Vente",
                                on_click=lambda _: self.show_section("vente"),
                                width=200,
                                height=60,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                    bgcolor=ft.colors.BLUE_GREY_800,
                                    color=ft.colors.WHITE,
                                )
                            ),
                            ft.ElevatedButton(
                                "Achat",
                                on_click=lambda _: self.show_section("achat"),
                                width=200,
                                height=60,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                    bgcolor=ft.colors.BLUE_GREY_800,
                                    color=ft.colors.WHITE,
                                )
                            ),
                            ft.ElevatedButton(
                                "Stock",
                                on_click=lambda _: self.show_section("stock"),
                                width=200,
                                height=60,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                    bgcolor=ft.colors.BLUE_GREY_800,
                                    color=ft.colors.WHITE,
                                )
                            ),
                            ft.ElevatedButton(
                                "Magasin",
                                on_click=lambda _: self.show_section("magasin"),
                                width=200,
                                height=60,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                    bgcolor=ft.colors.BLUE_GREY_800,
                                    color=ft.colors.WHITE,
                                )
                            ),
                            ft.ElevatedButton(
                                "Références Iris",
                                on_click=lambda _: self.show_section("iris"),
                                width=200,
                                height=60,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=12),
                                    bgcolor=ft.colors.BLUE_GREY_800,
                                    color=ft.colors.WHITE,
                                )
                            ),
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        # Section Vente
        self.vente_nom_field = ft.TextField(label="Nom du pneu", width=300)
        self.vente_qte_field = ft.TextField(label="Quantité", keyboard_type=ft.KeyboardType.NUMBER, width=300)
        self.vente_message = ft.Text()
        
        self.vente_section = ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            ft.icons.ARROW_BACK,
                            on_click=lambda _: self.show_menu(),
                            icon_size=30
                        ),
                        ft.Text("Vente de pneu", size=24, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                self.vente_nom_field,
                self.vente_qte_field,
                ft.ElevatedButton(
                    "Valider la vente",
                    on_click=self.valider_vente,
                    width=200,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor=ft.colors.GREEN,
                        color=ft.colors.WHITE,
                    )
                ),
                self.vente_message,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        # Section Achat
        self.achat_nom_field = ft.TextField(label="Nom du pneu", width=300)
        self.achat_qte_field = ft.TextField(label="Quantité", keyboard_type=ft.KeyboardType.NUMBER, width=300)
        self.achat_message = ft.Text()
        
        self.achat_section = ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            ft.icons.ARROW_BACK,
                            on_click=lambda _: self.show_menu(),
                            icon_size=30
                        ),
                        ft.Text("Achat de pneu", size=24, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                self.achat_nom_field,
                self.achat_qte_field,
                ft.ElevatedButton(
                    "Ajouter au stock",
                    on_click=self.ajouter_achat,
                    width=200,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor=ft.colors.BLUE,
                        color=ft.colors.WHITE,
                    )
                ),
                self.achat_message,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        # Section Stock
        self.stock_search_field = ft.TextField(
            label="Rechercher un pneu",
            width=300,
            on_change=self.rechercher_stock
        )
        self.stock_list = ft.Column(scroll=ft.ScrollMode.AUTO)
        
        self.stock_section = ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            ft.icons.ARROW_BACK,
                            on_click=lambda _: self.show_menu(),
                            icon_size=30
                        ),
                        ft.Text("Stock actuel", size=24, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                self.stock_search_field,
                ft.ElevatedButton(
                    "Actualiser le stock",
                    on_click=lambda _: self.refresh_stock(),
                    width=200,
                ),
                self.stock_list,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        # Section Magasin
        self.magasin_section = ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            ft.icons.ARROW_BACK,
                            on_click=lambda _: self.show_menu(),
                            icon_size=30
                        ),
                        ft.Text("Magasin", size=24, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Text("Nom du magasin : Pneus Express", size=18),
                ft.Text("Adresse : 123 Avenue du Caoutchouc", size=18),
                ft.Text("Téléphone : 01 23 45 67 89", size=18),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        # Section Références Iris
        self.iris_list = ft.Column(scroll=ft.ScrollMode.AUTO)
        
        self.iris_section = ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            ft.icons.ARROW_BACK,
                            on_click=lambda _: self.show_menu(),
                            icon_size=30
                        ),
                        ft.Text("Références pneus Iris", size=24, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                self.iris_list,
                ft.Text(
                    "Appuyez sur un code-barres pour le copier dans le presse-papiers",
                    size=12,
                    color=ft.colors.GREY,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        # Ajout de tous les éléments à la page
        self.page.add(
            ft.Column(
                [
                    title,
                    self.main_menu,
                    ft.Container(content=self.vente_section, visible=False),
                    ft.Container(content=self.achat_section, visible=False),
                    ft.Container(content=self.stock_section, visible=False),
                    ft.Container(content=self.magasin_section, visible=False),
                    ft.Container(content=self.iris_section, visible=False),
                ],
                spacing=30,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        
        # Initialiser les données
        self.refresh_stock()
        self.render_iris_list()
        
    def show_menu(self):
        # Masquer toutes les sections
        for section in [self.vente_section, self.achat_section, self.stock_section, 
                       self.magasin_section, self.iris_section]:
            section.visible = False
            
        # Afficher le menu principal
        self.main_menu.visible = True
        self.page.update()
        
    def show_section(self, section_name):
        # Masquer le menu principal
        self.main_menu.visible = False
        
        # Masquer toutes les sections
        for section in [self.vente_section, self.achat_section, self.stock_section, 
                       self.magasin_section, self.iris_section]:
            section.visible = False
            
        # Afficher la section demandée
        if section_name == "vente":
            self.vente_section.visible = True
        elif section_name == "achat":
            self.achat_section.visible = True
        elif section_name == "stock":
            self.stock_section.visible = True
            self.refresh_stock()
        elif section_name == "magasin":
            self.magasin_section.visible = True
        elif section_name == "iris":
            self.iris_section.visible = True
            self.render_iris_list()
            
        self.page.update()
        
    def get_stock(self):
        # Utiliser le stockage de Flet au lieu de localStorage
        stock_data = self.page.client_storage.get("stock")
        if stock_data:
            return json.loads(stock_data)
        return {}
        
    def set_stock(self, stock):
        # Utiliser le stockage de Flet au lieu de localStorage
        self.page.client_storage.set("stock", json.dumps(stock))
        
    def valider_vente(self, e):
        nom = self.vente_nom_field.value.strip()
        try:
            qte = int(self.vente_qte_field.value)
        except ValueError:
            self.vente_message.value = "Veuillez entrer une quantité valide"
            self.vente_message.color = ft.colors.RED
            self.page.update()
            return
            
        if not nom:
            self.vente_message.value = "Veuillez entrer un nom de pneu"
            self.vente_message.color = ft.colors.RED
            self.page.update()
            return
            
        stock = self.get_stock()
        if nom not in stock or stock[nom] < qte:
            self.vente_message.value = "Stock insuffisant !"
            self.vente_message.color = ft.colors.RED
            self.page.update()
            return
            
        stock[nom] -= qte
        if stock[nom] == 0:
            del stock[nom]
        self.set_stock(stock)
        
        self.vente_message.value = "Vente enregistrée !"
        self.vente_message.color = ft.colors.GREEN
        self.vente_nom_field.value = ""
        self.vente_qte_field.value = ""
        self.page.update()
        
    def ajouter_achat(self, e):
        nom = self.achat_nom_field.value.strip()
        try:
            qte = int(self.achat_qte_field.value)
        except ValueError:
            self.achat_message.value = "Veuillez entrer une quantité valide"
            self.achat_message.color = ft.colors.RED
            self.page.update()
            return
            
        if not nom:
            self.achat_message.value = "Veuillez entrer un nom de pneu"
            self.achat_message.color = ft.colors.RED
            self.page.update()
            return
            
        if qte <= 0:
            self.achat_message.value = "La quantité doit être supérieure à 0"
            self.achat_message.color = ft.colors.RED
            self.page.update()
            return
            
        stock = self.get_stock()
        stock[nom] = stock.get(nom, 0) + qte
        self.set_stock(stock)
        
        self.achat_message.value = "Achat ajouté au stock !"
        self.achat_message.color = ft.colors.GREEN
        self.achat_nom_field.value = ""
        self.achat_qte_field.value = ""
        self.page.update()
        
    def refresh_stock(self):
        stock = self.get_stock()
        self.stock_list.controls.clear()
        
        if not stock:
            self.stock_list.controls.append(
                ft.Text("Stock vide", size=16, color=ft.colors.GREY)
            )
        else:
            for nom, quantite in stock.items():
                self.stock_list.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(nom, size=16, weight=ft.FontWeight.BOLD),
                                            ft.Text(f"Quantité: {quantite}", size=14, color=ft.colors.GREY),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            padding=10,
                        ),
                        elevation=2,
                    )
                )
        self.page.update()
        
    def rechercher_stock(self, e):
        search_term = self.stock_search_field.value.lower().strip()
        stock = self.get_stock()
        self.stock_list.controls.clear()
        
        if not stock:
            self.stock_list.controls.append(
                ft.Text("Stock vide", size=16, color=ft.colors.GREY)
            )
        else:
            found = False
            for nom, quantite in stock.items():
                if search_term in nom.lower():
                    self.stock_list.controls.append(
                        ft.Card(
                            content=ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Column(
                                            [
                                                ft.Text(nom, size=16, weight=ft.FontWeight.BOLD),
                                                ft.Text(f"Quantité: {quantite}", size=14, color=ft.colors.GREY),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                padding=10,
                            ),
                            elevation=2,
                        )
                    )
                    found = True
                    
            if not found:
                self.stock_list.controls.append(
                    ft.Text("Aucun résultat trouvé", size=16, color=ft.colors.GREY)
                )
        self.page.update()
        
    def render_iris_list(self):
        self.iris_list.controls.clear()
        
        for ref in IRIS_REFS:
            self.iris_list.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(ref["nom"], size=14, weight=ft.FontWeight.BOLD),
                                ft.Row(
                                    [
                                        ft.Text(ref["code"], size=12, font_family="monospace"),
                                        ft.ElevatedButton(
                                            "Copier",
                                            on_click=lambda e, code=ref["code"]: self.copy_code(code),
                                            height=30,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                            ],
                            spacing=5,
                        ),
                        padding=10,
                    ),
                    elevation=2,
                )
            )
        self.page.update()
        
    def copy_code(self, code):
        # Copier le code dans le presse-papiers
        self.page.set_clipboard(code)
        # Afficher un message de confirmation
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("Code-barres copié dans le presse-papiers !"),
            action="OK",
        )
        self.page.snack_bar.open = True
        self.page.update()

def main(page: ft.Page):
    TireApp(page)

# Point d'entrée pour l'application mobile
ft.app(target=main, view=ft.AppView.FLET_APP_WEB)
