from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu


class MarketMarker(MapMarkerPopup):
    selfsize=[35,35]
    market_data=[]

    def on_release(self):
        #Open up the LoicationPopupMenu
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint=[.85, .9]
        menu.open()
