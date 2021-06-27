from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest  import UrlRequest
from kivy.app import App

class SearchPopupMenu (MDInputDialog):
    title = 'Where do you want to go?'
    text_button_ok = 'ok'
    def __init__(self):
        super().__init__()
        self.size_hint=[.9,.3]
        self.background_color=(163/255, 199/255, 98/255, 1)
        self.events_callback=self.callback



    def callback(self, *args):
        address = self.text_field.text
        print(address)
        self.geocode_get_latlon(address)

    def geocode_get_latlon(self, address):
        app_id="h6s4z34R1OJchsBFaqEz"
        app_code="6fyP3z7k3ozHTRlp3MnClhghhCpWsc9YjR2ed4-yYOY"
        address = parse.quote(address)

        url = "https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext=%s&apiKey=%s"%(address, app_code)
        UrlRequest(url, on_success=self.success, on_failure = self.failure, on_error=self.error )

    def success(self, urlrequest, result):
        print(result)
        Latitude = (result['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude'])
        Longitude = (result['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude'])
        app = App.get_running_app()
        mapview= app.root.ids.mapview
        mapview.center_on(Latitude, Longitude)
        #print(Latitude,'   ', Longitude)
        print('success')

    def failure(self, urlrequest, result):
        print(result)
        print('failure')

    def error(self, urlrequest, result):
        print(result)
        print('error')