from unittest import TestCase

from classwork.SKsTasks.sevensegment import SevenSegment


class MyTestCase(TestCase):
    def setUp(self):
        self.seven_segment = SevenSegment()

    def test_that_segment_is_on_when_last_digit_is_1_and_off_when_last_digit_is_zero(self):
        binary_digit = "11111101"
        self.assertEqual(True, self.seven_segment.is_on(binary_digit))

    def test_that_binary_digits_11111101_displays_zero(self):
        # binary_digit = "11111101"
        # self.seven_segment.set_digit(binary_digit)
        # self.assertTrue(self.seven_segment.is_on(binary_digit))
        # self.assertEqual(binary_digit, self.seven_segment.get_digit())
        output = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', ' ', ' ', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        self.assertEqual(self.seven_segment.display_zero(), output)
    def test_that_binary_digits_00001101_displays_one(self):
        # binary_digit = "00001101"
        # self.seven_segment.set_digit(binary_digit)
        # self.assertTrue(self.seven_segment.is_on(binary_digit))
        # self.assertEqual(binary_digit, self.seven_segment.get_digit())
        output = [
            ['#', ' ', ' ', ' '],
            ['#', ' ', ' ', ' '],
            ['#', ' ', ' ', ' '],
            ['#', ' ', ' ', ' '],
            ['#', ' ', ' ', ' ']
        ]
        self.assertEqual(self.seven_segment.display_one(), output)

    def test_that_binary_digits_11011011_displays_two(self):
        output = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#']
        ]
        self.assertEqual(self.seven_segment.display_two(), output)
    def test_that_binary_digits_11110011_displays_three(self):
        output = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        self.assertEqual(self.seven_segment.display_three(), output)

    def test_that_binary_digits_01100111_displays_four(self):
        output = [
            ['#', ' ', ' ', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['', ' ', ' ', '#'],
            [' ', ' ', ' ', '#']
        ]
        self.assertEqual(self.seven_segment.display_four(), output)

    def test_that_binary_digits_10110111_displays_five(self):
        output = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#'],
            ['', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        self.assertEqual(self.seven_segment.display_five(), output)

    def test_that_binary_digits_10111111_displays_six(self):
        output = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        self.assertEqual(self.seven_segment.display_six(), output)

    def test_that_binary_digits_11100001_displays_seven(self):
        output = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#'],
            ['', ' ', ' ', '#'],
            [' ', ' ', ' ', '#']
        ]
        self.assertEqual(self.seven_segment.display_seven(), output)

    def test_that_binary_digits_11111111_displays_eight(self):
        output = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        self.assertEqual(self.seven_segment.display_eight(), output)

    def test_that_binary_digits_11100111_displays_nine(self):
        output = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['', ' ', ' ', '#'],
            [' ', ' ', ' ', '#']
        ]
        self.assertEqual(self.seven_segment.display_nine(), output)
    def test_that_when_is_on_and_user_inputs_binary_digits__display_returns_shape(self):
        user_input = "01100111"
        self.seven_segment.set_digit(user_input)
        self.assertEqual(self.seven_segment.display_four(), self.seven_segment.determine_output(user_input))
        # self.seven_segment.display_nothing(user_input)
        # self.assertEqual(self.seven_segment.display_nothing(), )

