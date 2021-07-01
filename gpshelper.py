from kivy.app import App
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog

class GpsHelper():
    has_centered_map=False
    def run(self):

        #Start Blinking
        #Get a reference to GpsBlinker, than call blink()
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker  #it referes to root widget, which is main.kv and then it reffers to blinker widget in gpsblinker.kv        #Request permissions on android
        gps_blinker.blink()
        #request permissons on Android
        if platform == 'android':
            from android.permissions import Permission, request_permissions
            def callback(permission, results):
                if all([res for res in results]):
                    print("Got all permissions")
                    from plyer import gps
                    gps.configure(on_location=self.update_blinker_position,
                                  on_status=self.on_auth_status)
                    gps.start(minTime=1000, minDistance=0)
                else:
                    print("did not get all permissions")






            request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION], callback)

        #Configure GPS
        if platform == 'android' or platform =='ios':
            from plyer import gps
            gps.configure(on_location=self.update_blinker_position, on_status=self.on_auth_status)
            gps.start(minTime=1000, minDistance=0)

    def update_blinker_position(self, *args, **kwargs):
        my_lat= kwargs['lat']
        my_lon= kwargs['lon']
        print("GPS POSITION", my_lat, my_lon)
        #update GPSBLINKER POSITION
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker  #it referes to root widget, which is main.kv and then it reffers to blinker widget in gpsblinker.kv        #Request permissions on android
        gps_blinker.lat=my_lat
        gps_blinker.lon=my_lon
        #Center map on gps
        if not self.has_centered_map:

            map = App.get_running_app().root.ids.mapview
            map.center_on(my_lat, my_lon)
            self.has_centered_map=True



    def on_auth_status(self, general_status, status_message): #checking wheter GPS is allowed
        if general_status=='provider-enabled':
            pass
        else:
            self.open_gps_access_popup()

    def open_gps_access_popup(self):
        dialog = MDDialog(title="GPS Error", text='Allow me to get your damn GPS')
        dialog.size_hint=[.8, .8]
        dialog.pos_hint={'center_x': .5, 'center_y': .5}
        dialog.open()
