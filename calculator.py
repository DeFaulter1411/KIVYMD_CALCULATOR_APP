from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'

        MDTextField:
            id: display
            text: "0"
            halign: "right"
            font_size: "49sp"
            readonly: True

        GridLayout:
            cols: 4
            spacing: "5dp"
            padding: "10dp"

            #Buttons
            MDRectangleFlatButton:
                text: "7"
                on_release: app.on_button_press("7")
            MDRectangleFlatButton:
                text: "8"
                on_release: app.on_button_press("8")
            MDRectangleFlatButton:
                text: "9"
                on_release: app.on_button_press("9")
            MDRectangleFlatButton:
                text: "/"
                on_release: app.on_button_press("/")
    
            MDRectangleFlatButton:
                text: "4"
                on_release: app.on_button_press("4")
            MDRectangleFlatButton:
                text: "5"   
                on_release: app.on_button_press("5")
            MDRectangleFlatButton:
                text: "6"  
                on_release: app.on_button_press("6")
            MDRectangleFlatButton:
                text: "*"  
                on_release: app.on_button_press("*")
    
            MDRectangleFlatButton:
                text: "1"
                on_release: app.on_button_press("1")
            MDRectangleFlatButton:
                text: "2"
                on_release: app.on_button_press("2")
            MDRectangleFlatButton:
                text: "3"
                on_release: app.on_button_press("3")
            MDRectangleFlatButton:
                text: "-"
                on_release: app.on_button_press("-")
    
            MDRectangleFlatButton:
                text: "C"
                on_release: app.clear_display()
            MDRectangleFlatButton:
                text: "0"
                on_release: app.on_button_press("0")
            MDRectangleFlatButton:
                text: "="
                on_release: app.calculate_result()
            MDRectangleFlatButton:
                text: "+"
                on_release: app.on_button_press("+")                    
'''


class CalculatorApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_button_press(self, value):
        display = self.root.ids.display
        if display.text == "0":
            display.text = value
        else:
            display.text += value

    def calculate_result(self):
        display = self.root.ids.display
        try:
            display.text = str(eval(display.text))
        except:
            display.text = "Error"

    def clear_display(self):
        self.root.ids.display.text = "0"


if __name__ == '__main__':
    CalculatorApp().run()
