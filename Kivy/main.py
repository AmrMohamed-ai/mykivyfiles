



from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


from kivy.properties import StringProperty



class WidgetsExample(BoxLayout):
    count = 0
    
    my_text = StringProperty(str(count))
    sourcet = StringProperty('Imgs/npressed.png')

    def on_button_click_1(self):
        self.count += 1
        self.my_text = str(self.count)
        self.sourcet = 'Imgs/pressed.png'

    def on_button_click_2(self):
        self.my_text = str(0)

    def not_pressed(self):
        self.sourcet = 'Imgs/npressed.png'





class TheLabApp(App):
    pass


TheLabApp().run()
