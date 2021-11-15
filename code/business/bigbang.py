

class BigBangLogic:

    def __init__(self, number):
        self.number = number

    def calculate_string_based_on_number(self):
        divisors = []
        for i in range(1, (self.number + 1)):
            is_not_divisible = True
            partial_divisor = ''
            if i % 3 == 0:
                partial_divisor = partial_divisor + "Big"
                is_not_divisible = False
            if i % 5 == 0:
                partial_divisor = partial_divisor + "Bang"
                is_not_divisible = False
            if i % 7 == 0:
                partial_divisor = partial_divisor + "Theory"
                is_not_divisible = False
            if is_not_divisible:
                partial_divisor = str(i)
            divisors.append(partial_divisor)
        return divisors

#big_bang = BigBang(105)
#print(big_bang.calculate_string_based_on_number())

