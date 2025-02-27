from classwork.SKsTasks.entry import Entry

class Diary:
    def __init__(self, username, password):
        self._is_locked = True
        self._username = username
        self._password = password
        self._entries : list[Entry] = []
        self._entry_count = 0

    def __str__(self):
        return f"Username: {self._username}, Password: {self._password}"

    def __repr__(self):
        return f"Username: {self._username}, Password: {self._password}"

    def set_password(self, password):
        self._password = password
    def set_username(self, username):
        self._username = username
    def get_username(self):
        return self._username
    def get_password(self):
        return self._password

    def create_entry(self, title, content):
        entry_id = self.get_id()
        try:
            entry : Entry = Entry(entry_id, title, content)
            self._entries.append(entry)
            self._entry_count += 1
        except Exception as e:
            print(f"Entry not created: {e}")

    def get_id(self):
        entry_id = self._entry_count + 1
        return entry_id

    def delete_entry(self, entry_id):
        try:
            if self._entries[entry_id - 1] is not None:
                self._entries.pop(entry_id - 1)
                self._entry_count -= 1
        except Exception as e:
            print(f"Entry not deleted: {e}")

    def get_entry(self):
        try:
            if len(self._entries) != 0:
                entry = self._entries[self._entry_count - 1]
                return entry
        except Exception as e:
            print(f"No entry found: {e}")

    def find_entry_by_id(self, entry_id):
        try:
            for entry in self._entries:
                if entry_id > 0:
                    entry = self._entries[entry_id - 1]
                return entry
        except Exception as e:
            print(f"Entry not found: {e}")

    def update_entry(self, entry_id, title, content):
        try:
            entry = self.find_entry_by_id(entry_id)
            if entry is not None and content is not None:
                entry.set_entry_title(title)
                entry.set_entry_content(content)
            else:
                print("No entry present")
        except Exception as e:
            print(f"Entry not found: {e}")

    def lock_diary(self):
        self._is_locked = True

    def is_locked(self):
        if self._is_locked:
            print("Diary is locked")
        return self._is_locked

    def unlock_diary(self, password):
        if password is self._password:
            self._is_locked = False
            print("Diary unlocked")

    def view_entries(self):
        return self._entries

