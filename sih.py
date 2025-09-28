from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

class WelcomeScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.go_to_next, 3)
    
    def go_to_next(self, dt):
        self.manager.current = 'login'

class LoginScreen(Screen):
    def login_user(self):
        username = self.ids.name_input.text.strip()
        password = self.ids.password_input.text.strip()
        
        # Clear previous error
        self.ids.error_label.text = ""
        
        # Simple validation
        if not username:
            self.ids.error_label.text = "Please enter your name"
            return
        
        if not password:
            self.ids.error_label.text = "Please enter password"
            return
        
        if len(password) < 4:
            self.ids.error_label.text = "Password must be at least 4 characters"
            return
        
        # Success - go to menu
        menu_screen = self.manager.get_screen('menu')
        menu_screen.ids.user_welcome.text = f"Welcome back, {username}!"
        self.manager.current = 'menu'
    
    def go_to_signup(self):
        self.manager.current = 'registration'

class RegistrationScreen(Screen):
    def register_user(self):
        name = self.ids.name_input.text.strip()
        email = self.ids.email_input.text.strip()
        password = self.ids.password_input.text.strip()
        dob = self.ids.dob_input.text.strip()
        
        # Clear previous error
        self.ids.error_label.text = ""
        
        # Validation
        if not name:
            self.ids.error_label.text = "Name is required"
            return
        
        if not email or "@" not in email:
            self.ids.error_label.text = "Valid email is required"
            return
        
        if not password or len(password) < 6:
            self.ids.error_label.text = "Password must be at least 6 characters"
            return
        
        if not dob:
            self.ids.error_label.text = "Date of birth is required"
            return
        
        # Success - go to menu
        menu_screen = self.manager.get_screen('menu')
        menu_screen.ids.user_welcome.text = f"Welcome, {name}!"
        self.manager.current = 'menu'
    
    def go_to_login(self):
        self.manager.current = 'login'

class MenuScreen(Screen):
    def logout(self):
        # Clear form fields and go back to login
        login_screen = self.manager.get_screen('login')
        login_screen.ids.name_input.text = ""
        login_screen.ids.password_input.text = ""
        login_screen.ids.error_label.text = ""
        
        reg_screen = self.manager.get_screen('registration')
        reg_screen.ids.name_input.text = ""
        reg_screen.ids.email_input.text = ""
        reg_screen.ids.password_input.text = ""
        reg_screen.ids.dob_input.text = ""
        reg_screen.ids.error_label.text = ""
        
        self.manager.current = 'login'

class NivaarApp(App):
    def build(self):
        return Builder.load_file('k.kv')

NivaarApp().run()
