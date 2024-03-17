# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import json

class FormApp(App):
    def build(self):
        self.form_data = []

        layout = BoxLayout(orientation='vertical')
        self.name_input = TextInput(hint_text='Enter Name')
        self.age_input = TextInput(hint_text='Enter Age')
        save_button = Button(text='Save', on_press=self.save_data)
        search_button = Button(text='Search', on_press=self.search_data)
        self.search_input = TextInput(hint_text='Search Name')
        self.result_label = Label()

        layout.add_widget(Label(text='Fill out the form:'))
        layout.add_widget(self.name_input)
        layout.add_widget(self.age_input)
        layout.add_widget(save_button)
        layout.add_widget(Label(text='Search for a name:'))
        layout.add_widget(self.search_input)
        layout.add_widget(search_button)
        layout.add_widget(self.result_label)

        return layout

    def save_data(self, instance):
        name = self.name_input.text.strip()
        age = self.age_input.text.strip()
        if name and age:
            self.form_data.append({'name': name, 'age': age})
            with open('form_data.json', 'w') as f:
                json.dump(self.form_data, f)
            self.name_input.text = ''
            self.age_input.text = ''
            print("Data saved successfully!")
        else:
            print("Please fill out all fields.")

    def search_data(self, instance):
        search_name = self.search_input.text.strip()
        if search_name:
            with open('form_data.json', 'r') as f:
                data = json.load(f)
            found = False
            for entry in data:
                if entry['name'] == search_name:
                    self.result_label.text = f"Name: {entry['name']}, Age: {entry['age']}"
                    found = True
                    break
            if not found:
                self.result_label.text = "Name not found."
        else:
            print("Please enter a name to search.")

if __name__ == '__main__':
    FormApp().run()
