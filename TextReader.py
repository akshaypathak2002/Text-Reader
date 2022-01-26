import pyttsx3
import random #To randomly choice the voice
from kivy.app import  App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import  Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
Builder.load_file('TR.kv')#To import kivy graphics file




class TextRead(App):

    def build(self):
        #Main Layout of the window
        self.window=GridLayout()
        self.window.cols=1
        self.window.size_hint=(0.6,0.6)
        self.window.pos_hint={'center_x':0.5,'center_y':0.5}

        #To add the Label
        self.window.label=Label(text='Enter any line below to speak ')
        self.window.add_widget(self.window.label)
        #To add the text input
        self.window.input=TextInput(multiline=False)
        self.window.add_widget(self.window.input)
        #Now we are adding the button
        self.window.button=Button(text='Read')
        self.window.button.bind(on_press=self.speak)
        self.window.add_widget(self.window.button)

        return self.window

    def speak(self,kwargs):  # we are not passing the audio here instance(or any other keyword ) for internal working of kivy
        engine = pyttsx3.init('sapi5')  # Default software of the window to take voice
        voices = engine.getProperty('voices')
        engine.setProperty('voice', random.choice([voices[0].id, voices[1].id]))
        engine.say(self.window.input.text)
        engine.runAndWait()



if __name__=='__main__':
    TextRead().run()