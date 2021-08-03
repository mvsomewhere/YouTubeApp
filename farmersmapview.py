from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from marketmarker import MarketMarker


image="marker1.png"#marker image

class FarmersMapView(MapView):
    market_names=[]
    getting_markets_timer = None

    def start_getting_markets_in_fov(self):
        #After one seconds get the markets in the fov
        try:
            self.getting_markets_timer.cancel()
        except:
            pass

        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def get_markets_in_fov(self, *args):

        #get reference to main app and database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()#returns main app when running
        sql_statement = "SELECT * FROM markets WHERE x > %s AND x < %s AND y > %s AND y < %s "%(min_lon, max_lon, min_lat, max_lat)#sql_stmnt is just a variable
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()#Returns a list from app.cursor
        print(markets)

        for market in markets:
            name = market[1]
            if name in self.market_names:
                continue
            else:
                self.add_market(market)

    def add_market(self, market):

        # create MarketMarker
        lat, lon = market[21], market[20]#each market is a list of info where lat located at index 21 and lon at index 20
        marker = MarketMarker(lat=lat, lon=lon, source=image)
        marker.size=(55,55)

        marker.market_data=market#wtf is going on here

        #add MarketMarker to the map
        self.add_widget(marker)


        #Keep track of the MarketMarker's name (to avoid duplicates)
        name = market[1]
        self.market_names.append(name)
