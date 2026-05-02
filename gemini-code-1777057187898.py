import numpy as np

# --- MILESTONE 1: CORE CLASSES ---

class User:
    """Base class for system users[cite: 85, 133]."""
    def __init__(self, username, role="Viewer"):
        self.username = username
        self.role = role

    def login(self):
        print(f"\nUser {self.username} logged in as {self.role}.")

class DataSet:
    """Represents and stores the data[cite: 69]."""
    def __init__(self, name):
        self.dataset_name = name
        self.data = []

    def add_data(self, values):
        """Adds raw numerical data to the set[cite: 75]."""
        self.data = values
        print(f"Data added to '{self.dataset_name}'.")

class Analyzer:
    """Performs statistical calculations[cite: 77]."""
    def __init__(self, dataset_obj):
        self.dataset = dataset_obj.data

    def calculate_mean(self):
        return np.mean(self.dataset) if self.dataset else 0

    def find_max(self):
        return np.max(self.dataset) if self.dataset else 0

# --- MILESTONE 2: INTERACTION & LOGIC ---

class Admin(User):
    """Admin inherits User and has full permissions[cite: 135, 137]."""
    def __init__(self, username):
        super().__init__(username, role="Admin")

    def can_modify(self):
        return True # Conditional logic for permissions 

class Report:
    """Produces the final results based on user role (Polymorphism)[cite: 93, 146]."""
    def __init__(self, analyzer_obj, user_obj):
        self.analyzer = analyzer_obj
        self.user = user_obj

    def generate_report(self):
        """Polymorphism: Different output based on user role."""
        print(f"\n--- REPORT FOR {self.user.username} ---")
        if self.user.role == "Viewer":
            print("Access Limited: You can only see the average.")
            print(f"Average: {self.analyzer.calculate_mean()}")
        else:
            print(f"Full Analysis: Mean = {self.analyzer.calculate_mean()}, Max = {self.analyzer.find_max()}")

# --- SYSTEM EXECUTION (Object Interaction) ---

# 1. Setup Users
admin_user = Admin("Alice")
viewer_user = User("Bob", "Viewer")

# 2. Data Entry (DataSet)
my_data = DataSet("Student Marks")
my_data.add_data([70, 85, 90, 65, 100]) # Example data [cite: 30]

# 3. Processing (Analyzer)
engine = Analyzer(my_data)

# 4. Output (Report Interaction) [cite: 123]
admin_report = Report(engine, admin_user)
admin_report.generate_report()

viewer_report = Report(engine, viewer_user)
viewer_report.generate_report()