import requests
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.clock import Clock 
from kivy.uix.spinner import Spinner
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.metrics import dp

API_BASE = "https://not-quite-prototype-3.onrender.com"

Screen(name="signup")

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'welcome'
        
        # Background
        with self.canvas.before:
            Color(0.1, 0.3, 0.6, 1)
            self.bg = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=lambda x, y: setattr(self.bg, 'size', y), pos=lambda x, y: setattr(self.bg, 'pos', y))
        
        # Main layout
        main = BoxLayout(orientation='vertical', spacing=dp(30), padding=dp(40))
        
        # Logo
        logo = Image(source='logo.png', size_hint=(1, 0.4))
        main.add_widget(logo)
        
        # App name
        app_name = Label(text='DISASTRA', font_size='40sp', bold=True, color=[1, 1, 1, 1], size_hint=(1, 0.3))
        main.add_widget(app_name)
        
        # Tagline
        tagline = Label(text='Your Disaster Awareness Friend', font_size='18sp', color=[0.9, 0.9, 0.9, 1], size_hint=(1, 0.3))
        main.add_widget(tagline)
        
        self.add_widget(main)
    
    def on_enter(self):
        Clock.schedule_once(self.go_to_next, 3)
    
    def go_to_next(self, dt):
        self.manager.current = 'login'

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'login'
        
        # Background
        with self.canvas.before:
            Color(0.05, 0.15, 0.25, 1)
            self.bg = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=lambda x, y: setattr(self.bg, 'size', y), pos=lambda x, y: setattr(self.bg, 'pos', y))
        
        # Main layout
        main = BoxLayout(orientation='vertical', padding=[dp(20), dp(30)], spacing=dp(30))
        
        # Logo section
        logo_section = BoxLayout(orientation='vertical', size_hint=(1, 0.25), spacing=dp(15))
        logo_box = BoxLayout(size_hint_y=0.25, orientation='vertical')
        
        logo = Image(source='logo.png', size_hint=(None, None), size=(dp(100), dp(100)), pos_hint={'center_x': 0.5})
        logo_box.add_widget(logo)
        logo_section.add_widget(logo_box)
        main.add_widget(logo_section)
        
        # Login form section
        form_section = BoxLayout(orientation='vertical', size_hint=(1, None), height=dp(450))
        
        # Login card
        card = BoxLayout(orientation='vertical', padding=[dp(30), dp(35)], spacing=dp(20), 
                        size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # Card background
        with card.canvas.before:
            Color(0.95, 0.95, 0.97, 1)
            self.card_bg = RoundedRectangle(pos=card.pos, size=card.size, radius=[dp(20)])
        card.bind(size=lambda x, y: setattr(self.card_bg, 'size', y), pos=lambda x, y: setattr(self.card_bg, 'pos', y))
        
        # Header
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(70), spacing=dp(5))
        header.add_widget(Label(text='Login', font_size='26sp', bold=True, color=[0.1, 0.1, 0.1, 1], size_hint_y=None, height=dp(35)))
        header.add_widget(Label(text='Sign in to continue.', font_size='14sp', color=[0.4, 0.4, 0.4, 1], size_hint_y=None, height=dp(25)))
        card.add_widget(header)
        
        # Input fields
        inputs = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(140), spacing=dp(15))
        
        # Name input
        name_field = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(60), spacing=dp(5))
        name_label = Label(text='NAME', font_size='11sp', color=[0.4, 0.4, 0.4, 1], size_hint_y=None, height=dp(15), halign='left')
        name_label.bind(size=name_label.setter('text_size'))
        name_field.add_widget(name_label)
        
        self.name_input = TextInput(hint_text='Enter your name', multiline=False, font_size='15sp', size_hint_y=None, height=dp(40),
                                   background_color=[0.85, 0.85, 0.85, 1], foreground_color=[0.1, 0.1, 0.1, 1],
                                   cursor_color=[0.1, 0.3, 0.6, 1], padding=[dp(12), dp(8)])
        name_field.add_widget(self.name_input)
        inputs.add_widget(name_field)
        
        # Password input
        pass_field = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(60), spacing=dp(5))
        pass_label = Label(text='PASSWORD', font_size='11sp', color=[0.4, 0.4, 0.4, 1], size_hint_y=None, height=dp(15), halign='left')
        pass_label.bind(size=pass_label.setter('text_size'))
        pass_field.add_widget(pass_label)
        
        self.password_input = TextInput(hint_text='Enter your password', password=True, multiline=False, font_size='15sp', 
                                       size_hint_y=None, height=dp(40), background_color=[0.85, 0.85, 0.85, 1],
                                       foreground_color=[0.1, 0.1, 0.1, 1], cursor_color=[0.1, 0.3, 0.6, 1], padding=[dp(12), dp(8)])
        pass_field.add_widget(self.password_input)
        inputs.add_widget(pass_field)
        
        card.add_widget(inputs)
        
        # Error label
        self.error_label = Label(text='', color=[0.8, 0.2, 0.2, 1], font_size='11sp', size_hint_y=None, height=dp(20), halign='center')
        self.error_label.bind(size=self.error_label.setter('text_size'))
        card.add_widget(self.error_label)
        
        # Login button
        login_btn = Button(text='Log in', font_size='17sp', bold=True, size_hint_y=None, height=dp(45),
                          background_color=[0.05, 0.15, 0.25, 1], color=[1, 1, 1, 1])
        login_btn.bind(on_press=lambda x: self.login_user())
        card.add_widget(login_btn)
        
        # Footer
        footer = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(45), spacing=dp(3))
        footer.add_widget(Label(text='Forgot Password?', font_size='11sp', color=[0.4, 0.4, 0.4, 1], size_hint_y=None, height=dp(18)))
        
        signup_btn = Button(text='Signup !', font_size='11sp', color=[0.1, 0.3, 0.6, 1], size_hint_y=None, height=dp(24),
                           background_color=[0, 0, 0, 0])
        signup_btn.bind(on_press=lambda x: self.go_to_signup())
        footer.add_widget(signup_btn)
        
        card.add_widget(footer)
        form_section.add_widget(card)
        main.add_widget(form_section)
        
        self.add_widget(main)
    
    def login_user(self):
        username = self.name_input.text.strip()
        password = self.password_input.text.strip()
        
        self.error_label.text = ""
        
        if not username:
            self.error_label.text = "Please enter your name"
            return
        
        if not password:
            self.error_label.text = "Please enter password"
            return
        
        if len(password) < 4:
            self.error_label.text = "Password must be at least 4 characters"
            return
        
        # API call for login (Optional - can be dummy for now)
        try:
            # Uncomment for real API integration
            # response = requests.post(f"{API_BASE}/login", json={"username": username, "password": password})
            # if response.status_code == 200:
            self.manager.current = 'dashboard'
            # else:
            #     self.error_label.text = "Invalid credentials"
        except:
            # Fallback to dummy login
            self.manager.current = 'dashboard'
    
    def go_to_signup(self):
        self.manager.current = 'registration'

class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'registration'
        
        # Background
        with self.canvas.before:
            Color(0.2, 0.8, 0.8, 1)
            self.bg = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=lambda x, y: setattr(self.bg, 'size', y), pos=lambda x, y: setattr(self.bg, 'pos', y))
        
        main = RelativeLayout()
        
        # Back button
        back_btn = Button(text='<-', font_size='22sp', bold=True, size_hint=(None, None), 
                         size=(dp(45), dp(45)), pos_hint={'x': 0.03, 'top': 0.96},
                         background_color=[0.05, 0.15, 0.25, 0.8], color=[1, 1, 1, 1])
        back_btn.bind(on_press=lambda x: self.go_to_login())
        main.add_widget(back_btn)
        
        # Scrollable form
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True, pos_hint={'center_x': 0.5, 'center_y': 0.48}, size_hint=(0.9, 0.9))
        form = BoxLayout(orientation='vertical', size_hint_y=None, padding=[dp(25), dp(30)], spacing=dp(18))
        form.bind(minimum_height=form.setter('height'))
        
        # Card background
        with form.canvas.before:
            Color(0.95, 0.95, 0.97, 1)
            self.form_bg = RoundedRectangle(pos=form.pos, size=form.size, radius=[dp(20)])
        form.bind(size=lambda x, y: setattr(self.form_bg, 'size', y), pos=lambda x, y: setattr(self.form_bg, 'pos', y))
        
        # Top spacing
        form.add_widget(Widget(size_hint_y=None, height=dp(20)))
        
        # Logo and title
        logo = Image(source='logo.png', size_hint=(None, None), size=(dp(100), dp(100)), pos_hint={'center_x': 0.5})
        form.add_widget(logo)
        
        app_name = Label(text='DISASTRA', font_size='18sp', bold=True, color=[0.1, 0.1, 0.1, 1], size_hint_y=None, height=dp(25))
        form.add_widget(app_name)
        
        # Title
        title_section = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(60), spacing=dp(3))
        title_section.add_widget(Label(text='Create new Account', font_size='22sp', bold=True, color=[0.1, 0.1, 0.1, 1], size_hint_y=None, height=dp(30)))
        title_section.add_widget(Label(text='Already Registered? Log in here.', font_size='12sp', color=[0.4, 0.4, 0.4, 1], size_hint_y=None, height=dp(20)))
        form.add_widget(title_section)
        
        # Form fields
        fields_section = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(280), spacing=dp(15))
        
        # Create input fields
        field_data = [
            ('NAME', 'Jiara Martins', False),
            ('EMAIL', 'hello@reallygreatsite.com', False),
            ('PASSWORD', '••••••', True),
            ('DATE OF BIRTH', 'DD/MM/YYYY', False)
        ]
        
        self.inputs = {}
        for label_text, hint_text, is_password in field_data:
            field_box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(60), spacing=dp(5))
            
            label = Label(text=label_text, font_size='11sp', color=[0.4, 0.4, 0.4, 1], size_hint_y=None, height=dp(15), halign='left')
            label.bind(size=label.setter('text_size'))
            field_box.add_widget(label)
            
            text_input = TextInput(hint_text=hint_text, password=is_password, multiline=False, font_size='15sp',
                                  size_hint_y=None, height=dp(40), background_color=[0.85, 0.85, 0.85, 1],
                                  foreground_color=[0.1, 0.1, 0.1, 1], padding=[dp(10), dp(6)])
            field_box.add_widget(text_input)
            fields_section.add_widget(field_box)
            
            # Store input references
            attr_name = label_text.lower().replace(' ', '_')
            self.inputs[attr_name] = text_input
        
        form.add_widget(fields_section)
        
        # Error label
        self.error_label = Label(text='', color=[0.8, 0.2, 0.2, 1], font_size='11sp', size_hint_y=None, height=dp(25), halign='center')
        self.error_label.bind(size=self.error_label.setter('text_size'))
        form.add_widget(self.error_label)
        
        # Sign up button
        signup_btn = Button(text='Sign up', font_size='17sp', bold=True, size_hint_y=None, height=dp(45),
                           background_color=[0.05, 0.15, 0.25, 1], color=[1, 1, 1, 1])
        signup_btn.bind(on_press=lambda x: self.register_user())
        form.add_widget(signup_btn)
        
        # Bottom spacing
        form.add_widget(Widget(size_hint_y=None, height=dp(30)))
        
        scroll.add_widget(form)
        main.add_widget(scroll)
        self.add_widget(main)
    
    def register_user(self):
        name = self.inputs['name'].text.strip()
        email = self.inputs['email'].text.strip()
        password = self.inputs['password'].text.strip()
        dob = self.inputs['date_of_birth'].text.strip()
        
        self.error_label.text = ""
        
        if not name:
            self.error_label.text = "Name is required"
            return
        
        if not email or "@" not in email:
            self.error_label.text = "Valid email is required"
            return
        
        if not password or len(password) < 6:
            self.error_label.text = "Password must be at least 6 characters"
            return
        
        if not dob:
            self.error_label.text = "Date of birth is required"
            return
        
        # API call for registration (Optional)
        try:
            # Uncomment for real API integration
            # response = requests.post(f"{API_BASE}/register", json={"name": name, "email": email, "password": password, "dob": dob})
            # if response.status_code == 201:
            popup = Popup(title='Account Created', content=Label(text='Success! Please login.'), size_hint=(None, None), size=(300, 200))
            popup.open()
            Clock.schedule_once(lambda dt: self.go_to_login(), 2)
            # else:
            #     self.error_label.text = "Registration failed"
        except:
            # Fallback success
            popup = Popup(title='Account Created', content=Label(text='Success! Please login.'), size_hint=(None, None), size=(300, 200))
            popup.open()
            Clock.schedule_once(lambda dt: self.go_to_login(), 2)
    
    def go_to_login(self):
        self.manager.current = 'login'

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


class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'dashboard'
        
        # Background
        with self.canvas.before:
            Color(0.1, 0.3, 0.6, 1)
            self.bg = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=lambda x, y: setattr(self.bg, 'size', y), pos=lambda x, y: setattr(self.bg, 'pos', y))
        
        main = BoxLayout(orientation='vertical', padding=[dp(25), dp(30)], spacing=dp(20))
        
        # Header section
        header = BoxLayout(orientation='vertical', size_hint_y=0.25, spacing=dp(8))
        header.add_widget(Widget(size_hint_y=0.15))
        
        logo = Image(source='logo.png', size_hint=(None, None), size=(dp(100), dp(100)), pos_hint={'center_x': 0.5})
        header.add_widget(logo)
        
        app_name = Label(text='DISASTRA', font_size='22sp', bold=True, color=[1, 1, 1, 1], size_hint_y=0.3)
        header.add_widget(app_name)
        
        self.user_welcome = Label(text='Welcome!', font_size='14sp', color=[0.9, 0.9, 0.9, 1], size_hint_y=0.2)
        header.add_widget(self.user_welcome)
        
        main.add_widget(header)
        
        # Menu options
        options = BoxLayout(orientation='vertical', size_hint_y=0.75, spacing=dp(12))
        
        # Dashboard button (current screen indicator)
        dashboard_btn = Button(text='DASHBOARD', font_size='15sp', bold=True, size_hint_y=0.15,
                              background_color=[0.8, 0.4, 0.2, 1], color=[1, 1, 1, 1])
        options.add_widget(dashboard_btn)
        
        # Quiz button
        quiz_btn = Button(text='QUIZ', font_size='15sp', bold=True, size_hint_y=0.15,
                         background_color=[0.5, 0.3, 0.8, 1], color=[1, 1, 1, 1])
        quiz_btn.bind(on_press=self.goto_quiz)
        options.add_widget(quiz_btn)
        
        # Emergency Messages button
        emergency_btn = Button(text='EMERGENCY MESSAGES', font_size='15sp', bold=True, size_hint_y=0.15,
                              background_color=[0.3, 0.6, 0.9, 1], color=[1, 1, 1, 1])
        emergency_btn.bind(on_press=self.goto_emergency)
        options.add_widget(emergency_btn)
        
        # Profile button
        profile_btn = Button(text='PROFILE', font_size='15sp', bold=True, size_hint_y=0.15,
                            background_color=[0.9, 0.3, 0.3, 1], color=[1, 1, 1, 1])
        profile_btn.bind(on_press=self.goto_profile)
        options.add_widget(profile_btn)
        
        # LOGOUT BUTTON (Prominent and Clearly Visible)
        logout_btn = Button(text='LOGOUT', font_size='16sp', bold=True, size_hint_y=0.18,
                           background_color=[0.7, 0.2, 0.2, 1], color=[1, 1, 1, 1])
        logout_btn.bind(on_press=lambda x: self.logout())
        options.add_widget(logout_btn)
        
        # Small spacer
        options.add_widget(Widget(size_hint_y=0.22))
        
        main.add_widget(options)
        self.add_widget(main)
    
    def goto_quiz(self, instance):
        self.manager.get_screen("quiz").load_quiz()
        self.manager.current = "quiz"
    
    def goto_emergency(self, instance):
        self.manager.current = "emergency"

    def goto_profile(self, instance):
        self.manager.get_screen("profile").load_progress()
        self.manager.current = "profile"
    
    def logout(self):
        # Clear login form data
        login_screen = self.manager.get_screen('login')
        login_screen.name_input.text = ""
        login_screen.password_input.text = ""
        login_screen.error_label.text = ""
        
        # Clear registration form data
        try:
            reg_screen = self.manager.get_screen('registration')
            for input_field in reg_screen.inputs.values():
                input_field.text = ""
            reg_screen.error_label.text = ""
        except:
            pass
        
        # Go back to login screen
        self.manager.current = 'login'

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'quiz'
        
        # SAME BACKGROUND AS DASHBOARD/MENU
        with self.canvas.before:
            Color(0.1, 0.3, 0.6, 1)  # Same blue background as dashboard
            self.bg = Rectangle(pos=self.pos, size=self.size)
        self.bind(size=lambda x, y: setattr(self.bg, 'size', y), pos=lambda x, y: setattr(self.bg, 'pos', y))
        
        # Main vertical layout
        main_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Question and options section
        quiz_content = BoxLayout(orientation='vertical', size_hint_y=0.8, spacing=dp(10))
        
        # Question label
        self.q_label = Label(
            text="Quiz will appear here", 
            font_size='18sp', 
            color=[1, 1, 1, 1],  # White text for visibility on blue background
            text_size=(None, None),
            halign='center',
            valign='middle',
            size_hint_y=0.2
        )
        self.q_label.bind(size=self.q_label.setter('text_size'))
        quiz_content.add_widget(self.q_label)
        
        # Hint label
        self.hint_label = Label(
            text="", 
            font_size='14sp',
            color=[1, 0.8, 0.4, 1],  # Yellow-orange hint color for visibility
            text_size=(None, None),
            halign='center',
            size_hint_y=0.1
        )
        self.hint_label.bind(size=self.hint_label.setter('text_size'))
        quiz_content.add_widget(self.hint_label)
        
        # Options buttons
        options_layout = BoxLayout(orientation='vertical', size_hint_y=0.7, spacing=dp(8))
        self.option_inputs = []
        
        for i in range(4):
            btn = Button(
                text="", 
                font_size='14sp',
                text_size=(None, None),
                halign='center',
                valign='middle',
                size_hint_y=0.25,
                background_color=[0.9, 0.9, 0.9, 1],  # Light gray for options
                color=[0.1, 0.1, 0.1, 1]  # Dark text on light background
            )
            btn.bind(on_press=self.submit_answer)
            btn.bind(size=btn.setter('text_size'))
            self.option_inputs.append(btn)
            options_layout.add_widget(btn)
        
        quiz_content.add_widget(options_layout)
        main_layout.add_widget(quiz_content)
        
        # CUSTOM CONTROL BUTTONS LAYOUT
        controls_container = BoxLayout(orientation='vertical', size_hint_y=0.2, spacing=dp(5))
        
        # Main controls layout with 3 sections
        controls_main = BoxLayout(orientation='horizontal', size_hint_y=0.7, spacing=dp(10))
        
        # LEFT SECTION: Reset and Restart (vertical)
        left_section = BoxLayout(orientation='vertical', size_hint_x=0.25, spacing=dp(5))
        
        self.reset_btn = Button(
            text="RESET",
            font_size='12sp',
            bold=True,
            background_color=[0.5, 0.8, 1.0, 1],  # Sky Blue
            color=[1, 1, 1, 1]
        )
        self.reset_btn.bind(on_press=self.reset_quiz)
        left_section.add_widget(self.reset_btn)
        
        self.restart_btn = Button(
            text="RESTART", 
            font_size='12sp',
            bold=True,
            background_color=[0.5, 1.0, 0.8, 1],  # Aquamarine
            color=[1, 1, 1, 1]
        )
        self.restart_btn.bind(on_press=self.restart_quiz)
        left_section.add_widget(self.restart_btn)
        
        controls_main.add_widget(left_section)
        
        # CENTER SECTION: Next button
        center_section = BoxLayout(orientation='vertical', size_hint_x=0.5)
        
        # Spacer for centering
        center_section.add_widget(Widget(size_hint_y=0.25))
        
        self.next_btn = Button(
            text="NEXT",
            font_size='14sp',
            bold=True,
            size_hint_y=0.5,
            background_color=[0.2, 0.8, 0.2, 1],  # Green
            color=[1, 1, 1, 1]
        )
        self.next_btn.bind(on_press=self.next_question)
        center_section.add_widget(self.next_btn)
        
        # Spacer
        center_section.add_widget(Widget(size_hint_y=0.25))
        
        controls_main.add_widget(center_section)
        
        # RIGHT SECTION: Progress and Quit (vertical)
        right_section = BoxLayout(orientation='vertical', size_hint_x=0.25, spacing=dp(5))
        
        self.progress_btn = Button(
            text="PROGRESS",
            font_size='12sp',
            bold=True,
            background_color=[0.6, 0.4, 0.9, 1],  # Purplish-Blue
            color=[1, 1, 1, 1]
        )
        self.progress_btn.bind(on_press=self.show_progress)
        right_section.add_widget(self.progress_btn)
        
        self.quit_btn = Button(
            text="QUIT",
            font_size='12sp',
            bold=True,
            background_color=[0.9, 0.2, 0.2, 1],  # Red
            color=[1, 1, 1, 1]
        )
        self.quit_btn.bind(on_press=self.quit_quiz)
        right_section.add_widget(self.quit_btn)
        
        controls_main.add_widget(right_section)
        
        controls_container.add_widget(controls_main)
        
        # Small spacer at bottom
        controls_container.add_widget(Widget(size_hint_y=0.3))
        
        main_layout.add_widget(controls_container)
        self.add_widget(main_layout)

        # Quiz data variables
        self.questions = []
        self.current_idx = 0
        self.score = 0
        self.current_question = None
        self.answered = False

    def load_quiz(self):
        try:
            res = requests.get(f"{API_BASE}/quiz_questions?level=Basic")
            data = res.json()
            if data:
                self.questions = data
                self.current_idx = 0
                self.score = 0
                self.show_current_question()
            else:
                self.q_label.text = "No quiz available."
                self.hint_label.text = ""
                for btn in self.option_inputs:
                    btn.text = ""
                self.current_question = None
        except:
            self.q_label.text = "Unable to load quiz. Check connection."
            self.hint_label.text = ""
            for btn in self.option_inputs:
                btn.text = ""

    def show_current_question(self):
        if self.current_idx < len(self.questions):
            self.current_question = self.questions[self.current_idx]
            self.q_label.text = self.current_question.get('Question', 'No question')
            self.hint_label.text = ""
            for idx, opt in enumerate(['A', 'B', 'C', 'D']):
                self.option_inputs[idx].background_color = [0.9, 0.9, 0.9, 1]
                self.option_inputs[idx].color = [0.1, 0.1, 0.1, 1]
                self.option_inputs[idx].text = f"{opt}: {self.current_question['Options'][idx]}"
            self.answered = False
        else:
            self.current_question = None
            self.q_label.text = "Quiz finished!"
            self.hint_label.text = ""

    def submit_answer(self, instance):
        if self.current_question is None or self.answered:
            return
        selected = instance.text.split(":")[0]
        correct_letter = None
        for idx, opt_letter in enumerate(['A', 'B', 'C', 'D']):
            if self.current_question['Options'][idx] == self.current_question['Answer']:
                correct_letter = opt_letter
                break
        if selected == correct_letter:
            self.hint_label.text = ""
            self.q_label.text = "Correct!"
            instance.background_color = [0, 0.8, 0, 1]  # Green for correct
            instance.color = [1, 1, 1, 1]
            self.score += 1
            self.answered = True
            Clock.schedule_once(lambda dt: self.next_question(), 1)
        else:
            self.q_label.text = self.current_question.get('Question', 'No question')
            self.hint_label.text = f"Hint: {self.current_question.get('Hint', '')}"
            instance.background_color = [0.8, 0.2, 0.2, 1]  # Red for incorrect
            instance.color = [1, 1, 1, 1]
            self.answered = True

    def next_question(self, instance=None):
        if self.current_idx < len(self.questions) - 1:
            self.current_idx += 1
            self.show_current_question()
        else:
            self.current_question = None
            popup = Popup(title='Finished', content=Label(text=f'Quiz finished!\nScore: {self.score}/{len(self.questions)}'), size_hint=(0.5, 0.5))
            popup.open()

    def reset_quiz(self, instance):
        self.show_current_question()

    def restart_quiz(self, instance):
        self.current_idx = 0
        self.score = 0
        self.show_current_question()

    def quit_quiz(self, instance):
        self.manager.current = "dashboard"

    def show_progress(self, instance):
        popup = Popup(title='Progress', content=Label(text=f'Current Score: {self.score}\nQuestion: {self.current_idx + 1} / {len(self.questions)}'), size_hint=(0.5, 0.5))
        popup.open()


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.box = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.title_label = Label(
            text="[b]User Profile[/b]",
            markup=True,
            font_size="24sp",
            size_hint_y=None,
            height=40
        )
        self.profile_name = Label(
            text="User ID: ",
            font_size="18sp"
        )
        self.profile_quizzes = Label(
            text="Quizzes Completed: ",
            font_size="18sp"
        )
        self.profile_avg = Label(
            text="Average Score: ",
            font_size="18sp"
        )
        self.back_btn = Button(
            text="Back to Dashboard",
            size_hint_y=None,
            height=40,
            on_release=self.back_to_dashboard
        )

        self.box.add_widget(self.title_label)
        self.box.add_widget(self.profile_name)
        self.box.add_widget(self.profile_quizzes)
        self.box.add_widget(self.profile_avg)
        self.box.add_widget(self.back_btn)
        self.add_widget(self.box)

    def load_progress(self):
        res = requests.get(f"{API_BASE}/progress?user_id=testuser")
        data = res.json()
        self.profile_name.text = f"User ID: {data.get('user_id', 'Unknown')}"
        self.profile_quizzes.text = f"Quizzes Completed: {data.get('progress', {}).get('quizzes_completed', 0)}"
        self.profile_avg.text = f"Average Score: {data.get('progress', {}).get('average_score', 0)}"

    def back_to_dashboard(self, instance):
        self.manager.current = "dashboard"

class EmergencyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.box = BoxLayout(orientation='vertical')
        self.disasters = ['Earthquake', 'Fire', 'Flood', 'Cyclone', 'Cyber Attack']
        self.spinner = Spinner(text='Select Disaster', values=self.disasters, size_hint=(1, None), height=44)
        self.box.add_widget(self.spinner)
        self.show_btn = Button(text="View Messages")
        
        #type: ignore
        #self.show_btn.bind(on_press=self.show_messages)

        self.show_btn.bind(on_press=self.show_messages)
        self.box.add_widget(self.show_btn)
        back_btn = Button(text='Back', size_hint=(1, None), height=44)
        back_btn.bind(on_press=self.go_back)
        self.box.add_widget(back_btn)

        self.msg_label = Label(text="")
        self.box.add_widget(self.msg_label)
        self.add_widget(self.box)
    
    def go_back(self, instance):
        self.manager.current = 'dashboard'

    def show_messages(self, instance):
        disaster = self.spinner.text.strip()
        try:
            response = requests.get(f"{API_BASE}/emergency_messages?disaster={disaster}")
            data = response.json()

            if not data or data == {}:
                self.msg_label.text = f"No {disaster} messages found"
                return

            parts = []
            for section in ['warnings', 'alerts', 'safety_protocols', 'advice']:
                if data.get(section):
                   items = "\n".join(f"- {item}" for item in data[section])
                   parts.append(f"{section.capitalize()}:\n{items}")
            self.msg_label.text = "\n\n".join(parts) if parts else f"No messages for {disaster}"

        except Exception as e:
            self.msg_label.text = f"Error: {str(e)}"

class DisasterApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(RegistrationScreen(name="registration"))
        self.sm.add_widget(DashboardScreen(name="dashboard"))
        self.sm.add_widget(QuizScreen(name="quiz"))
        self.sm.add_widget(ProfileScreen(name="profile"))
        self.sm.add_widget(EmergencyScreen(name="emergency"))
        return self.sm
        return Builder.load_file('k.kv')

if __name__ == "__main__":
    DisasterApp().run()
