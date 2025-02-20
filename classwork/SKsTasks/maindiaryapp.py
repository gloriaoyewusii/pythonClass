import sys


from classwork.SKsTasks.diaries import Diaries
from classwork.SKsTasks.diary import Diary
from classwork.SKsTasks.entry import Entry

def sign_up():
    diaries = Diaries()
    username = input("Create a Username: ")
    password = input("Create a Password: ")

    if diaries is not None and diaries.find_diary_by(username) is not None and diaries.find_diary_by(
            password) is not None:
        if username == diaries.find_diary_by(username).get_username():
            print("Account already exists")
        sign_up()

    diary: Diary = Diary(username, password)

    if diaries is None:
        diaries = Diaries()
        diaries.add(diary.get_username(), diary.get_password())
        print("Diary successfully created")

def sign_in():
        print("\nEnter  your username and password to sign in: ")
        username = input("Username: ")
        password = input("Password: ")
        try:
            validate_diary(username, password)
        except ValueError as e:
            print(e)

def validate_diary(username, password):
        diaries = Diaries()
        diary = Diary(username, password)
        is_diary_name : bool = diary.get_username() == diaries.find_diary_by(username).get_username()
        is_diary_password : bool = diary.get_password() == diaries.find_diary_by(username).get_password()
        if diaries is not None and is_diary_name and is_diary_password:
            print("Diary found. Login successful")
        else:
            raise Exception("Diary not found. Login failed")
def find_diary_by_username():
        diaries = Diaries()
        name = input("Enter your username: ")
        if name == diaries.find_diary_by(name).get_username():
            diary = diaries.find_diary_by(name)
            print(diary.__str__())
        diary_menu()
def view_diaries():
    diaries = Diaries()
    print(diaries.__str__())
    diary_menu()

def diary_menu():
    diaries = Diaries()
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
            sign_up()
        case "2":
            sign_in()
        case "3":
            find_diary_by_username()
        case "4":
            view_diaries()
        case "5":
            delete_diary()
        case "6":
            create_entry()
        case "7":
            update_entry()
        case "8":
            find_entry_by_id()
        case "9":
            view_entries()
        case "10":
            delete_entry()
        case "11":
            sign_out()









    def delete_diary(self):
        if self.diaries is not None:
            self.diaries.delete(self._username, self.diaries.find_diary_by(self.username).get_password())

    def create_entry(self):
        entry_id = self.diaries.find_diary_by(self.username).get_id()
        title = input("Enter title: ")
        content = input("Enter content: ")

        if self.username is None and self.diaries is None:
            self.diaries = Diaries()
            self.username = self.diaries.find_diary_by(self.username).get_username()

            self.diaries.find_diary_by(self.username).create_entry(title, content)
            self.diaries.find_diary_by(self.username).get_entry().set_entry_id(entry_id)

        entry_is_null : bool = self.diaries.find_diary_by(self.username).get_entry() is None
        if self.diaries is not None and entry_is_null:
            self.diaries.find_diary_by(self.username).create_entry(title, content)
            self.diaries.find_diary_by(self.username).get_entry().set_entry_id(entry_id)

        if self.diaries is not None and not entry_is_null:
            self.diaries.find_diary_by(self.username).create_entry(title, content)

        self.diary_menu()

    def update_entry(self):
       entry_id =  self.diaries.find_diary_by(self._username).get_id()
       title = input("Enter title: ")
       content = input("Enter content: ")
       self.diaries.find_diary_by(self._username).update_entry(entry_id, title, content)

    def find_entry_by_id(self):
        entry_id = input("Enter entry ID: ")
        for index in range(0, self.diaries.check_size()):
            entry : Entry = self.diaries.find_diary_by(self._username).find_entry_by_id(entry_id)
            if entry is not None:
                print("Found entry with ID: " + entry_id)
                print(entry.__str__())

        self.diary_menu()

    def view_entries(self):
        print(self.diaries.find_diary_by(self._username).view_entries().__str__())


    def delete_entry(self):
        entry_id = input("Enter entry ID: ")
        self.diaries.find_diary_by(self._username).delete_entry(entry_id)
        print(f"Entry number {entry_id} has successfully been deleted")
        
        self.diary_menu()

    def sign_out(self):
        sys.exit(0)


    # if __name__ == "__main__":
    #     main()


