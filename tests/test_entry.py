from unittest import TestCase

from classwork.SKsTasks.entry import Entry


class TestEntry(TestCase):
    def setUp(self):
        self.entry = Entry(1, "new day", "it's a new morning")

    def test_that_entry_has_entry_id(self):
        self.assertEqual(1, self.entry.get_entry_id())
    def test_that_entry_has_entry_name(self):
        self.assertEqual("new day", self.entry.get_entry_title())
    def test_that_entry_has_entry_description(self):
        self.assertEqual("it's a new morning", self.entry.get_entry_body())