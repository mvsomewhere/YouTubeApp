import sqlite3
from kivymd.app import MDApp
from farmersmapview import FarmersMapView
from gpshelper import GpsHelper
from searchpopupmenu import SearchPopupMenu
import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()



class MainApp(MDApp):


    connection = None
    cursor = None
    search_menu = None
    def on_start(self):

        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.theme_style="Light"
        #Inititalize GPS
        GpsHelper().run()


        #Connect to database (DB file)
        self.connection=sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()

        #instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()


MainApp().run()

