from classwork.SKsTasks.diaries import Diaries

class MainDiaryApplication:
    def __init__(self):
        self.diaries = Diaries()

    def main(self):
        self.diary_menu()

    def diary_menu(self):
        print("Welcome to Gloria's Diary Application")
        print("""
        Accounts Management System
        1. Sign up for a new diary account
        2. Sign in to your account
        Diary Management System
        3. Find diary account by username
        4. View diary accounts
        5. Delete diary account
        Entries Management System
        6. Create new entry
        7. Update an existing entry
        8. Find entry by ID
        9. Find all entries
        10. Delete entry by ID
        11. Sign out
        """)
