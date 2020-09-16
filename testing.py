from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):

    def build(self):
        label = Label(text="working bitch")
        return label

TestApp().run()