class Luhn(object):
    def __init__(self, card_num):
        if len(card_num) < 2:
            raise ValueError ("Invalid string - input must be at least 2 characters long.")
        else:
            self.card_num = "".join(card_num.split(" "))

    def valid(self):
        valid = True
        numbers = []
        for i in self.card_num:
            try:
                numbers.append(int(i))
            except:
                raise ValueError("Input contains non-integer values.")
        if len(numbers) == 16:
            for i in range(-2,-len(numbers) - 1,-2):
                new_val = numbers[i]*2
                if new_val > 9: new_val -= 9
                numbers[i] = new_val
            if sum(numbers) % 10 == 0:
                print("Valid number.")
            else:
                print("Invalid number.")
        
if __name__ == "__main__":
    test = Luhn("4539 1488 0343 6467")
    test.valid()
                    
