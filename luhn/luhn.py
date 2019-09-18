class Luhn(object):
    def __init__(self, card_num):
        if len(card_num) < 2:
            raise valueError ("Invalid string - input must be at least 2 characters long.")
        else:
            self.card_num = card_num

    def valid(self):
        try:
            card_num = int(self.card_num)
