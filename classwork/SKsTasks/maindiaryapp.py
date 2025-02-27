import re
import sys


from classwork.SKsTasks.diaries import Diaries
from classwork.SKsTasks.diary import Diary
from classwork.SKsTasks.entry import Entry


def validate_user_details(username, password):
    username_is_correct = username is not None and re.fullmatch('[A-Z][a-z]+\\S', username)
    password_is_correct = password is not None and re.fullmatch(r'[A-Za-z1-9_!@]{8}', password)
    if not username_is_correct or not password_is_correct:
        raise Exception("Invalid User Details")


def sign_out():
    sys.exit(0)


class MainDiary:
    def __init__(self):
        self._username = None
        self._password = None
        self.diaries = Diaries()

    def sign_up(self):
        self._username = input("Create a Username: ")
        self._password = input("Create a Password: ")

        # self._username = username
        # self._password = password

        if self.diaries is not None and self.diaries.find_diary_by(self._username) is not None:
            if self._username == self.diaries.find_diary_by(self._username).get_username():
                print("Account already exists")
            self.sign_up()
        # self.diaries = Diaries()

        try:
            validate_user_details(self._username, self._password)
            diary: Diary = Diary(self._username, self._password)
            if self.diaries is None: self.diaries = Diaries()
            self.diaries.add(diary.get_username(), diary.get_password())
            print("Diary successfully created")
            self.sign_in()
        except Exception as error:
            print("An error occurred: {}".format(error))
            self.sign_up()

            # self.diary_menu()

    def sign_in(self):
        print("\nEnter  your username and password to sign in: ")
        self._username = input("Username: ")
        self._password = input("Password: ")
        try:
            validate_user_details(self._username, self._password)
            self.validate_diary(self._username, self._password)
        except Exception as error:
            print(error)


    def validate_diary(self, name, pass_word):
        diary: Diary = Diary(name, pass_word)
        is_diary_name = diary.get_username() == self.diaries.find_diary_by(name).get_username()
        is_diary_password = diary.get_password() == self.diaries.find_diary_by(name).get_password()
        if self.diaries is not None and is_diary_name and is_diary_password:
            print("Diary found. You are logged in.")
            self.diary_menu()
        else:
            raise Exception("Diary not found")
        self.sign_in()

    def find_diary_by_username(self):
        name = input("Enter your username: ")
        if name == self._username:
            diary : Diary = self.diaries.find_diary_by(self._username)
            print(diary)
        self.diary_menu()

    def view_diaries(self):
        print(self.diaries)
        self.diary_menu()

    def delete_diary(self):
        username = input("Enter your username: ")
        if self.diaries is not None:
            self.diaries.delete(username, self.diaries.find_diary_by(username).get_password())
            print("Diary successfully deleted")
        else:
            raise Exception("Failed to delete diary")
        self.diary_menu()

    def create_entry(self):
        entry_id = self.diaries.find_diary_by(self._username).get_id()
        title = input("Enter title: ")
        content = input("Enter content: ")

        if self._username is None and self.diaries is None:
            self.diaries = Diaries()
            self._username = self.diaries.find_diary_by(self._username).get_username()

            self.diaries.find_diary_by(self._username).create_entry(title, content)
            self.diaries.find_diary_by(self._username).get_entry().set_entry_id(entry_id)

        entry_is_null = self.diaries.find_diary_by(self._username).get_entry() is None
        if self.diaries is not None and entry_is_null:
            self.diaries.find_diary_by(self._username).create_entry(title, content)
            self.diaries.find_diary_by(self._username).get_entry().set_entry_id(entry_id)

        if self.diaries is not None and not entry_is_null:
            self.diaries.find_diary_by(self._username).create_entry(title, content)

        self.diary_menu()
    def update_entry(self):
        entry_id = self.diaries.find_diary_by(self._username).get_id()
        title = input("Enter title: ")
        content = input("Enter content: ")
        self.diaries.find_diary_by(self._username).update_entry(entry_id, title, content)
        self.diary_menu()

    def find_entry_by_id(self):
        entry_id = int(input("Enter entry ID: "))
        for index in range(0, self.diaries.check_size()):
            entry: Entry = self.diaries.find_diary_by(self._username).find_entry_by_id(entry_id)
            if entry is not None:
                print("Found entry with ID: " + str(entry_id))
                print(entry)

        self.diary_menu()

    def view_entries(self):
        print(self.diaries.find_diary_by(self._username).view_entries())
        self.diary_menu()

    def delete_entry(self):
        entry_id = int(input("Enter entry ID: "))
        self.diaries.find_diary_by(self._username).delete_entry(entry_id)
        print(f"Entry number {entry_id} has successfully been deleted")

        self.diary_menu()

    def diary_menu(self):
        # diaries = Diaries()
        print("\n--- Diary Menu ---")
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

        diary_choice = input("Enter your choice: ")
        match diary_choice:
            case "1":
                self.sign_up()
            case "2":
                self.sign_in()
            case "3":
                self.find_diary_by_username()
            case "4":
                self.view_diaries()
            case "5":
                self.delete_diary()
            case "6":
                self.create_entry()
            case "7":
                self.update_entry()
            case "8":
                self.find_entry_by_id()
            case "9":
                self.view_entries()
            case "10":
                self.delete_entry()
            case "11":
                sign_out()




if __name__ == "__main__":
    menu = MainDiary()
    menu.diary_menu()













