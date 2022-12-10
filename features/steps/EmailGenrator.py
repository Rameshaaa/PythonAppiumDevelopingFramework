import random
import string

class Random:
    def random_email(char_num):
        return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))