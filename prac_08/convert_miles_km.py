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

    def handle_calculate(self):
        miles = self.get_miles()
        km = miles * MILES_TO_KM
        self.result_text = str(km)

    def handle_increment(self, change):
        miles = self.get_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()


