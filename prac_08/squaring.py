from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    def build(self):
        Window.size = (400, 150)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root


