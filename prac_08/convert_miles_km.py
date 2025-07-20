from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    result_text = StringProperty()

    def build(self):
        self.title = "Miles to KM"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.result_text = "0.0"

