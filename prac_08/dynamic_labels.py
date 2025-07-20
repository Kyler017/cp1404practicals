from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", 123, "Dora"]

    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root




