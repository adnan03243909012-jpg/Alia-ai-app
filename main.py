from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class AliaApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=30, spacing=20, **kwargs)

        self.status_label = Label(
            text="🤖 Alia AI Assistant Ready!",
            font_size="22sp",
        )
        self.add_widget(self.status_label)

        self.btn = Button(
            text="🎙️ Tap to Speak",
            font_size="20sp",
            size_hint=(1, 0.3),
        )
        self.btn.bind(on_press=self.on_click)
        self.add_widget(self.btn)

    def on_click(self, instance):
        self.status_label.text = "🎙️ Listening..."


class AliaAI(App):
    def build(self):
        return AliaApp()


if __name__ == "__main__":
    AliaAI().run()