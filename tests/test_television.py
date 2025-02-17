import unittest
from classwork.SKsTasks import tv_task


class TestTV(unittest.TestCase):
    def test_that_tv_task_function_exists(self):
        tv_task.get_encrypt_text("Hello")
