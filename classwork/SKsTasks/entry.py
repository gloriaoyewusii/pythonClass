class Entry:
    def __init__(self, entry_id, title, content):
        self._entry_id = entry_id
        self._title = title
        self._content = content

    def __str__(self):
        return f"ID: {self._entry_id}, Title: {self._title}, Content: {self._content}"

    def __repr__(self):
        return f"ID: {self._entry_id}, Title: {self._title}, Content: {self._content}"

    def get_entry_id(self):
        return self._entry_id

    def get_entry_title(self):
        return self._title

    def get_entry_body(self):
        return self._content

    def set_entry_title(self, new_title):
        self._title = new_title
    def set_entry_content(self, new_content):
        self._content = new_content
    def set_entry_id(self, new_entry_id):
        self._entry_id = new_entry_id



