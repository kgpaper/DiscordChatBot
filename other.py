import random
import string


# random string 생성함수, 투표페이지 고유번호
def create_random_string():
    char_set = string.ascii_uppercase + string.digits
    print (''.join(random.sample(char_set*20, 20)))
