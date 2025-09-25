from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import json
from kivy.uix.screenmanager import Screen
import os
import random
from kivy.storage.jsonstore import JsonStore
from datetime import datetime
import re

from kivy.animation import Animation

class DataManager:
    def __init__(self):
        # Create storage files
        self.user_store = JsonStore('user_data.json')
        self.quiz_store = JsonStore('quiz_scores.json')
        self.app_store = JsonStore('app_settings.json')
        
        
        # Initialize default settings
        self.init_default_settings()


class WelcomeScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.go_to_next, 3)
    
    def go_to_next(self, dt):
        self.manager.current = 'registration'

class RegistrationScreen(Screen):
    def _init_(self, **kwargs):
        super().__init__(**kwargs)
        # Simple local storage without database
        self.user_storage = JsonStore('user_data.json')
    
    def submit_form(self):
        # Get form data
        name = self.ids.name_input.text.strip()
        email = self.ids.email_input.text.strip()
        age = self.ids.age_input.text.strip()
        phone = self.ids.phone_input.text.strip()
        
        # Clear previous error
        self.ids.error_label.text = ""
        
        # Validate form
        if not self.validate_form(name, email, age, phone):
            return
        
        # Save user data locally
        self.save_user_data(name, email, age, phone)
        
        # Show success animation
        self.show_success_animation()
        
        # Navigate to menu
        Clock.schedule_once(lambda dt: self.go_to_menu(), 1.5)
    
    def validate_form(self, name, email, age, phone):
        """Validate all form fields"""
        
        # Name validation
        if not name:
            self.show_error("👤 Full name is required")
            return False
        
        if len(name) < 2:
            self.show_error("👤 Name must be at least 2 characters")
            return False
        
        # Email validation (if provided)
        if email:
            if not self.is_valid_email(email):
                self.show_error("📧 Please enter a valid email address")
                return False
        
        # Age validation
        if not age:
            self.show_error("🎂 Age is required")
            return False
        
        try:
            age_int = int(age)
            if age_int < 5 or age_int > 120:
                self.show_error("🎂 Age must be between 5 and 120")
                return False
        except ValueError:
            self.show_error("🎂 Please enter a valid age")
            return False
        
        # Phone validation (if provided)
        if phone:
            if len(phone) != 10:
                self.show_error("📱 Phone number must be exactly 10 digits")
                return False
        
        return True
    
    def is_valid_email(self, email):
        """Simple email validation"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def show_error(self, message):
        """Display error message with animation"""
        self.ids.error_label.text = message
        
        # Add shake animation to error label
        anim = Animation(x=self.ids.error_label.x + 10, duration=0.1)
        anim += Animation(x=self.ids.error_label.x - 10, duration=0.1)
        anim += Animation(x=self.ids.error_label.x + 5, duration=0.1)
        anim += Animation(x=self.ids.error_label.x, duration=0.1)
        anim.start(self.ids.error_label)
    
    def save_user_data(self, name, email, age, phone):
        """Save user data to local storage"""
        try:
            from datetime import datetime
            
            user_data = {
                'name': name,
                'email': email if email else 'Not provided',
                'age': int(age),
                'phone': phone if phone else 'Not provided',
                'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'app_version': '1.0'
            }
            
            # Save to local storage
            self.user_storage.put('current_user', **user_data)
            
            print(f"✅ User registered successfully: {name}")
            
        except Exception as e:
            print(f"❌ Error saving user data: {e}")
            self.show_error("❌ Error saving data. Please try again.")
    
    def show_success_animation(self):
        """Show success feedback"""
        self.ids.error_label.text = "✅ Registration successful! Welcome to DISASTRA!"
        self.ids.error_label.color = (0.2, 0.8, 0.2, 1)  # Green color
        
        # Scale animation for button
        button = self.ids.get('submit_button', None)
        if button:
            anim = Animation(size=(button.width * 1.1, button.height * 1.1), duration=0.2)
            anim += Animation(size=(button.width, button.height), duration=0.2)
            anim.start(button)
    
    def go_to_menu(self):
        """Navigate to menu screen"""
        self.manager.current = 'menu'
    
    def get_user_data(self):
        """Get current user data"""
        try:
            if self.user_storage.exists('current_user'):
                return dict(self.user_storage.get('current_user'))
            return None
        except Exception as e:
            print(f"❌ Error getting user data: {e}")
            return None
    
    def is_user_registered(self):
        """Check if user is already registered"""
        return self.user_storage.exists('current_user')
class MenuScreen(Screen):
    pass




class DisastersScreen(Screen):
    pass 
 
class EmergencyHelplinesScreen(Screen):
    pass


    def on_pre_enter(self):
        # Load JSON file
        json_path = os.path.join(os.path.dirname(__file__), 'emergency_messages.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        def format_section(title, items):
            return title + ':\n' + '\n'.join(f"- {item}" for item in items) + '\n'

        for disaster in data['disasters']:
            text = ''
            text += format_section("Warnings", disaster['warnings'])
            text += format_section("Alerts", disaster['alerts'])
            text += format_section("Safety Protocols", disaster['safety_protocols'])
            text += format_section("Advice", disaster['advice'])

            if disaster['type'] == 'Cyclone':
                self.cyclone_text = text
            elif disaster['type'] == 'Fire':
                self.fire_text = text
            elif disaster['type'] == 'Flood':
                self.flood_text = text
            elif disaster['type'] == 'Earthquake':
                self.earthquake_text = text
            elif disaster['type'] == 'Cyber Attack':
                self.cyber_text = text

#ADD THESE NEW QUIZ CLASSES:
class QuizLevelScreen(Screen):
    def start_quiz(self, level):
        quiz_screen = self.manager.get_screen('quiz')
        quiz_screen.setup_quiz(level)
        self.manager.transition.direction = 'left'
        self.manager.current = 'quiz'

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.user_answers = []
        
    def setup_quiz(self, level):
        app = App.get_running_app()
        all_questions = app.get_quiz_questions()
        
        # Filter questions by level and get random 10
        level_questions = [q for q in all_questions if q['level'] == level]
        self.questions = random.sample(level_questions, min(10, len(level_questions)))
        
        self.current_question = 0
        self.score = 0
        self.user_answers = []
        self.load_question()
    
    def load_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            
            self.ids.progress_label.text = f"Question {self.current_question + 1} of {len(self.questions)}"
            self.ids.question_label.text = q['Question']
            self.ids.option1.text = q['Options'][0]
            self.ids.option2.text = q['Options'][1]
            self.ids.option3.text = q['Options'][2]
            self.ids.option4.text = q['Options'][3]
            
            # Reset colors
            for option in [self.ids.option1, self.ids.option2, self.ids.option3, self.ids.option4]:
                option.background_color = (1, 1, 1, 1)
            
            self.ids.hint_label.text = ""
        else:
            self.finish_quiz()
    
    def select_answer(self, option_index):
        q = self.questions[self.current_question]
        selected_answer = q['Options'][option_index]
        correct_answer = q['Answer']
        
        self.user_answers.append(selected_answer)
        
        if selected_answer == correct_answer:
            self.score += 1
            
        Clock.schedule_once(lambda dt: self.next_question(), 1)
    
    def next_question(self):
        self.current_question += 1
        self.load_question()
    
    def show_hint(self):
        q = self.questions[self.current_question]
        self.ids.hint_label.text = f"Hint: {q['Hint']}"
    
    def finish_quiz(self):
        result_screen = self.manager.get_screen('quiz_result')
        result_screen.show_result(self.score, len(self.questions))
        self.manager.transition.direction = 'left'
        self.manager.current = 'quiz_result'

class QuizResultScreen(Screen):
    def show_result(self, score, total):
        self.ids.score_label.text = f"Your Score: {score}/{total}"
        
        percentage = (score / total) * 100
        if percentage >= 80:
            message = "Excellent! You're well prepared for disasters! 🌟"
        elif percentage >= 60:
            message = "Good job! Keep learning more about disaster safety! 👍"
        elif percentage >= 40:
            message = "Not bad! Study more to improve your disaster preparedness! 📚"
        else:
            message = "Keep learning! Disaster awareness is very important! 💪"
        
        self.ids.result_message.text = message

class MyApp(App):
    def build(self):
        self.load_disasters_data()
        self.load_quiz_data()
        return Builder.load_file('DISASTRA.kv')
    
    def load_disasters_data(self):
        json_path = os.path.join(os.path.dirname(__file__), 'emergency_messages.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            self.disasters_data = json.load(f)

    def load_quiz_data(self):
        json_path = os.path.join(os.path.dirname(__file__), 'quiz_questions.json') #iz file name
        with open(json_path, 'r', encoding='utf-8') as f:
            self.quiz_data = json.load(f)

    def get_disaster_text(self, disaster_type):
        for disaster in self.disasters_data['disasters']:
            if disaster['type'] == disaster_type:
                text = ''
                text += 'Warnings:\n' + '\n'.join(f"- {item}" for item in disaster['warnings']) + '\n\n'
                text += 'Alerts:\n' + '\n'.join(f"- {item}" for item in disaster['alerts']) + '\n\n'
                text += 'Safety Protocols:\n' + '\n'.join(f"- {item}" for item in disaster['safety_protocols']) + '\n\n'
                text += 'Advice:\n' + '\n'.join(f"- {item}" for item in disaster['advice'])
                return text
        return "No data available"
    
    def get_quiz_questions(self):
        return self.quiz_data  # Return the loaded quiz data
       

MyApp().run()
