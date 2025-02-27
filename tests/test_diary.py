from unittest import TestCase

from classwork.SKsTasks.diary import Diary
from classwork.SKsTasks.entry import Entry


class TestDiary(TestCase):
    # def setUp(self):
    #     self.diary = Diary("name", "correctPassword")

    def test_that_diary_returns_name_and_correct_password(self):
        self.diary = Diary("name", "correctPassword")

        self.assertEqual("name", self.diary.get_username())
        self.assertEqual("correctPassword", self.diary.get_password())
    def test_that_entries_are_created_in_diary(self):
        self.diary = Diary("name", "correctPassword")

        self.diary.create_entry("New day", "It's a new day")

        entry : Entry = self.diary.get_entry()
        self.assertEqual(entry, self.diary.get_entry())
        print(self.diary.get_entry())
    def test_that_two_entries_are_added_to_diary_when_i_delete_one_entry_returns_one_entry(self):
        self.diary = Diary("name", "correctPassword")

        self.diary.create_entry("New day", "It's a new day")
        self.diary.create_entry("New month", "It's a new month")

        self.diary.delete_entry(1)
        entry : Entry = self.diary.get_entry()
        self.assertEqual(entry, self.diary.get_entry())
        print(entry)

    def test_to_find_entry_by_id_when_I_create_three_entries_returns_correct_entry(self):
        self.diary = Diary("name", "correctPassword")

        self.diary.create_entry("New day", "It's a new day")
        self.diary.create_entry("New month", "It's a new month")
        self.diary.create_entry("New year", "It's a new year")

        entry : Entry = self.diary.find_entry_by_id(1)
        print(self.diary.find_entry_by_id(2))
        print(self.diary.find_entry_by_id(3))
        print(entry)

    def test_that_entry_is_created_correctly_and_updated_when_i_add_to_it(self):
        self.diary = Diary("name", "correctPassword")
        self.diary.create_entry("New day", "It's a new day")

        self.diary.update_entry(1, "A New Day", "It''s a new day here")
        print(self.diary.find_entry_by_id(1))

    def test_that_created_diary_can_be_locked(self):
        self.diary = Diary("name", "correctPassword")

        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

    def test_that_diary_is_locked_when_i_unlock_diary_it_is_unlocked(self):
        self.diary = Diary("name", "correctPassword")
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

        self.diary.unlock_diary("correctPassword")
        self.assertFalse(self.diary.is_locked())

    def test_that_diary_is_created_two_entries_are_added_when_i_view_entries_returns_correct_list_of_entries(self):
        self.diary = Diary("name", "correctPassword")
        self.diary.create_entry("New day", "It's a new day")
        self.diary.create_entry("New month", "It's a new month")

        print(self.diary.view_entries())

