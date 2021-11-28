import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.inside = GridLayout()
        self.cols = 2
        self.add_widget(Label(text="First Name: "))
        self.firstname = TextInput(multiline=False)
        self.add_widget(self.firstname)

        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline=False)
        self.add_widget(self.lastname)

        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        self.submit = Button(text="submit", font_size=40)
        self.add_widget(self.submit)

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    MyApp().run()
