from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.spinner import MDSpinner
from kivy.uix.boxlayout import BoxLayout
import pickle
import numpy as np

KV = '''
ScreenManager:
    PersonalDetailScreen:
        name: "personal_detail"
    SecondPageScreen:
        name: "second_page"
    ThirdPageScreen:
        name: "third_page"
    FinalPageScreen:
        name: "final_page"
    FeedbackScreen:
        name: "feedback"

<PersonalDetailScreen>:
    name: "personal_detail"
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(15)
        adaptive_height: True
        size_hint_y: None
        height: self.minimum_height

        MDLabel:
            text: "Personal Details"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Primary"

        MDTextField:
            id: gender
            hint_text: "Gender"
            mode: "rectangle"
            icon_left: "gender-male-female"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter 0 for Female or 1 for Male."
            helper_text_mode: "on_focus"

        MDTextField:
            id: age
            hint_text: "Age"
            mode: "rectangle"
            input_filter: "int"
            icon_left: "account"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter your age (numeric value)."
            helper_text_mode: "on_focus"

        MDTextField:
            id: height
            hint_text: "Height (in meters)"
            mode: "rectangle"
            icon_left: "height"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter your height in meters (e.g., 1.75)."
            helper_text_mode: "on_focus"

        MDTextField:
            id: weight
            hint_text: "Weight (in kg)"
            mode: "rectangle"
            icon_left: "weight"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter your weight in kilograms."
            helper_text_mode: "on_focus"

        MDRaisedButton:
            text: "Next"
            pos_hint: {"center_x": 0.5}
            on_release: app.switch_screen("second_page")
            size_hint: None, None
            size: "200dp", "50dp"
            elevation: 10
            md_bg_color: app.theme_cls.primary_color
            text_color: "white"

<SecondPageScreen>:
    name: "second_page"
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(15)
        adaptive_height: True
        size_hint_y: None
        height: self.minimum_height

        MDLabel:
            text: "Diet and Family History"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Secondary"

        MDTextField:
            id: family_history
            hint_text: "Family history of overweight?"
            mode: "rectangle"
            icon_left: "family"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter 1 if yes, 0 if no."
            helper_text_mode: "on_focus"

        MDTextField:
            id: favc
            hint_text: "Do you eat high caloric food frequently?"
            mode: "rectangle"
            icon_left: "food"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter 1 if yes, 0 if no."
            helper_text_mode: "on_focus"

        MDTextField:
            id: fcvc
            hint_text: "How often do you eat vegetables?"
            mode: "rectangle"
            icon_left: "carrot"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter 1 for Nothing, 2 for Sometimes, 3 for Everytime."
            helper_text_mode: "on_focus"

        MDTextField:
            id: ncp
            hint_text: "Number of main meals daily"
            mode: "rectangle"
            icon_left: "food-steak"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter the number of meals you have per day."
            helper_text_mode: "on_focus"

        MDRaisedButton:
            text: "Next"
            pos_hint: {"center_x": 0.5}
            on_release: app.switch_screen("third_page")
            size_hint: None, None
            size: "200dp", "50dp"
            elevation: 10
            md_bg_color: app.theme_cls.primary_color
            text_color: "white"

<ThirdPageScreen>:
    name: "third_page"
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(15)
        adaptive_height: True
        size_hint_y: None
        height: self.minimum_height

        MDLabel:
            text: "Lifestyle and Monitoring"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Secondary"

        MDTextField:
            id: caec
            hint_text: "Do you eat any food between meals?"
            mode: "rectangle"
            icon_left: "food"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter 0 for Always, 1 for Frequently, 2 for Sometimes, 3 for No."
            helper_text_mode: "on_focus"

        MDTextField:
            id: smoke
            hint_text: "Do you smoke?"
            mode: "rectangle"
            icon_left: "smoking"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter 1 if yes, 0 if no."
            helper_text_mode: "on_focus"

        MDTextField:
            id: ch2o
            hint_text: "How much water do you drink daily?"
            mode: "rectangle"
            icon_left: "water"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter 1 for Rarely, 2 for Not Much, 3 for Healthy Amount."
            helper_text_mode: "on_focus"

        MDTextField:
            id: scc
            hint_text: "Do you monitor calories?"
            mode: "rectangle"
            icon_left: "calorie"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter 1 if yes, 0 if no."
            helper_text_mode: "on_focus"

        MDRaisedButton:
            text: "Next"
            pos_hint: {"center_x": 0.5}
            on_release: app.switch_screen("final_page")
            size_hint: None, None
            size: "200dp", "50dp"
            elevation: 10
            md_bg_color: app.theme_cls.primary_color
            text_color: "white"

<FinalPageScreen>:
    name: "final_page"
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(15)
        adaptive_height: True
        size_hint_y: None
        height: self.minimum_height

        MDLabel:
            text: "Physical Activity and Transport"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Secondary"

        MDTextField:
            id: faf
            hint_text: "How often do you have physical activity?"
            mode: "rectangle"
            icon_left: "run"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter a value from 0 for Rarely, 1 for Sometimes, 2 for On The Weekends, 3 for Always."
            helper_text_mode: "on_focus"

        MDTextField:
            id: tue
            hint_text: "How much time do you use technology daily?"
            mode: "rectangle"
            icon_left: "cellphone"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter 0 for Not Much, 1 for Sometimes, 2 for Everytime."
            helper_text_mode: "on_focus"

        MDTextField:
            id: calc
            hint_text: "How often do you drink alcohol?"
            mode: "rectangle"
            icon_left: "alcohol"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter 0 for Always, 1 for Frequently, 2 for Sometimes, 3 for Never."
            helper_text_mode: "on_focus"

        MDTextField:
            id: mtrans
            hint_text: "What transportation do you use?"
            mode: "rectangle"
            icon_left: "bus"
            icon_left_color: app.theme_cls.primary_color
            helper_text: "Enter 0 for Automobile, 1 for Bike, 2 For MotorBike, 3 for Public Transportation, 4 for Walking."
            helper_text_mode: "on_focus"

        MDRaisedButton:
            text: "Predict Obesity Level"
            pos_hint: {"center_x": 0.5}
            on_release: app.predict_obesity()
            size_hint: None, None
            size: "200dp", "50dp"
            elevation: 10
            md_bg_color: app.theme_cls.primary_color
            text_color: "white"

<FeedbackScreen>:
    name: "feedback"
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "We'd Love Your Feedback!"
            font_style: "H5"
            halign: "center"
            theme_text_color: "Primary"

        MDTextField:
            id: feedback
            hint_text: "Your feedback here..."
            mode: "rectangle"
            multiline: True
            size_hint_y: 0.4
            helper_text: "Tell us what you think!"
            helper_text_mode: "on_focus"
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Submit Feedback"
            pos_hint: {"center_x": 0.5}
            size_hint: None, None
            size: "200dp", "50dp"
            elevation: 10
            md_bg_color: app.theme_cls.primary_color
            text_color: "white"
            on_release: app.submit_feedback()
'''

class PersonalDetailScreen(Screen):
    pass

class SecondPageScreen(Screen):
    pass

class ThirdPageScreen(Screen):
    pass

class FinalPageScreen(Screen):
    pass

class FeedbackScreen(Screen):
    pass

class ObesityPredictionApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.dialog = None  # Store the dialog instance
        return Builder.load_string(KV)

    def switch_screen(self, screen_name):
        self.root.current = screen_name

    def show_alert_dialog(self, title, text):
        self.dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDFlatButton(text="Close", on_release=self.close_dialog),
            ],
        )
        self.dialog.open()

    def close_dialog(self, obj):
        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None  # Reset the dialog reference

    def predict_obesity(self):
        # Extracting all inputs
        gender = int(self.root.get_screen("personal_detail").ids.gender.text)
        age = int(self.root.get_screen("personal_detail").ids.age.text)
        height = float(self.root.get_screen("personal_detail").ids.height.text)
        weight = float(self.root.get_screen("personal_detail").ids.weight.text)

        family_history = int(self.root.get_screen("second_page").ids.family_history.text)
        favc = int(self.root.get_screen("second_page").ids.favc.text)
        fcvc = int(self.root.get_screen("second_page").ids.fcvc.text)
        ncp = int(self.root.get_screen("second_page").ids.ncp.text)

        caec = int(self.root.get_screen("third_page").ids.caec.text)
        smoke = int(self.root.get_screen("third_page").ids.smoke.text)
        ch2o = int(self.root.get_screen("third_page").ids.ch2o.text)
        scc = int(self.root.get_screen("third_page").ids.scc.text)

        faf = int(self.root.get_screen("final_page").ids.faf.text)
        tue = int(self.root.get_screen("final_page").ids.tue.text)
        calc = int(self.root.get_screen("final_page").ids.calc.text)
        mtrans = int(self.root.get_screen("final_page").ids.mtrans.text)

        # Preprocessing inputs into the appropriate format for prediction
        input_data = np.array([
            gender, age, height, weight,
            family_history, favc, fcvc, ncp,
            caec, smoke, ch2o, scc,
            faf, tue, calc, mtrans
        ]).reshape(1, -1)  # Reshaping to match the expected input shape for the model

        # Load model and predict (using a pre-trained model)
        model = pickle.load(open("obesity_pipeline.pkl", "rb"))
        prediction = model.predict(input_data)

        # Display result
        obesity_level = ["Insufficient_Weight", "Normal_Weight", "Obesity_Type_I", "Obesity_Type_II", 
                         "Obesity_Type_III", "Overweight_Level_I", "Overweight_Level_II"]
        result = obesity_level[prediction[0]]

        self.show_alert_dialog("Obesity Level", f"Prediction: {result}")
        self.root.current = "feedback"

    def submit_feedback(self):
        feedback_text = self.root.get_screen("feedback").ids.feedback.text
        print(f"Feedback: {feedback_text}")
        self.show_alert_dialog("Feedback Submitted", "Thank you for your feedback!")
        self.root.current = "personal_detail"  # Go back to the first screen

ObesityPredictionApp().run()
