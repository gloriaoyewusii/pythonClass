from classwork.SKsTasks.diary import Diary
from classwork.SKsTasks.entry import Entry


class Diaries:
    def __init__(self):
        self._diaries : list[Diary] = []

    def __str__(self):
        return str(self._diaries)

    def add(self, username, password):
        self._diaries.append(Diary(username, password))

    def check_size(self):
        return len(self._diaries)

    def find_diary_by(self, username):
        for diary in self._diaries:
            if diary.get_username() == username:
                return diary

    def delete(self, username, password):
        for diary in self._diaries:
            if diary.get_username() == username and diary.get_password() == password:
                self._diaries.remove(diary)