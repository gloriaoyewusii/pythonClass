from unittest import TestCase

from classwork.SKsTasks.diaries import Diaries
from classwork.SKsTasks.diary import Diary
from classwork.SKsTasks.entry import Entry


class TestDiaries(TestCase):
    def setUp(self):
        self.diaries = Diaries()
    def test_that_diaries_size_is_one_when_i_add_1_diary_to_the_list(self):
        self.diaries.add("name", "password")
        self.assertEqual(1, self.diaries.check_size())
        self.assertNotEqual(0, self.diaries.check_size())

    def test_that_i_can_get_username_of_diary_account(self):
        self.diaries.add("name", "password")

        self.assertEqual("name", self.diaries.find_diary_by("name").get_username())
        self.assertEqual("password", self.diaries.find_diary_by("name").get_password())

    def test_that_1_diary_is_added_to_the_diary_list_when_i_find_diary_by_username_returns_diary(self):

        diary = Diary("name", "password")
        self.diaries.add(diary.get_username(), diary.get_password())
        self.assertEqual("name", self.diaries.find_diary_by("name").get_username())
        self.assertEqual("password", self.diaries.find_diary_by("name").get_password())

        self.diary2 = Diary("name2", "password2")
        self.diaries.add(self.diary2.get_username(), self.diary2.get_password())

        self.assertEqual(2, self.diaries.check_size())
        #
        # self.assertEqual(diary, self.diaries.find_diary_by("name"))
        self.assertEqual("name2", self.diaries.find_diary_by("name2").get_username())

        self.assertEqual("password", self.diaries.find_diary_by("name").get_password())
        print(self.diaries)

    def test_that_i_add_2diaries_to_diaries_list_when_i_delete_one_size_returns_one(self):
        diary = Diary("name", "password")
        diary2 = Diary("name2", "password2")
        self.diaries.add(diary.get_username(), diary.get_password())
        self.diaries.add(diary2.get_username(), diary2.get_password())
        self.assertEqual(2, self.diaries.check_size())

        self.diaries.delete(diary2.get_username(), diary2.get_password())
        self.assertEqual(1, self.diaries.check_size())
        self.diaries.delete(diary.get_username(), diary.get_password())
        self.assertEqual(0, self.diaries.check_size())