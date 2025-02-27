class SevenSegment:
    def __init__(self):
        self.digit = None
        self._is_on = True

    def is_on(self, binary_digits) -> bool:
        # jg
        if binary_digits[len(binary_digits) - 1] == 0:
            self._is_on = False
        elif binary_digits[len(binary_digits) - 1] == 1:
            self._is_on = True
        return self._is_on

    def set_digit(self, binary_digit):
        self.digit = binary_digit

    def get_digit(self):
        return self.digit

    def display_zero(self):
        zero = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', ' ', ' ', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        return zero
    def display_one(self):
        one = [
            ['#', ' ', ' ', ' '],
            ['#', ' ', ' ', ' '],
            ['#', ' ', ' ', ' '],
            ['#', ' ', ' ', ' '],
            ['#', ' ', ' ', ' ']
        ]
        return one

    def display_two(self):
        two = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#']
        ]
        return two

    def display_three(self):
        three = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        return three

    def display_four(self):
        four = [
            ['#', ' ', ' ', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#']
        ]
        return four
    def display_five(self):
        five = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#'],
            ['', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        return five
    def display_six(self):
        six = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        return six
    def display_seven(self):
        seven = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#']
        ]
        return seven

    def display_eight(self):
        eight = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        return eight
    def display_nine(self):
        nine = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#']
        ]
        return nine

    def determine_output(self, user_input):
        # user_input = list(user_input)
        if user_input[len(user_input) - 1] == 0:
            self._is_on = False
            return []
        else:
            print(user_input)
            match user_input:
                case "11111101":
                    return self.display_zero()
                case "00001101":
                    return self.display_one()
                case "11011011":
                    return self.display_two()
                case "11110011":
                    return self.display_three()
                case "01100111":
                    return self.display_four()
                case "10110111":
                    return self.display_five()
                case "10111111":
                    return self.display_six()
                case "11100001":
                    return self.display_seven()
                case "111111111":
                    return self.display_eight()
                case "11100111":
                    return self.display_nine()
