phone_book = dict()


def add_new_user(name, phone, dikt=phone_book):
    dikt[name] = phone


def get_number(name, dikt=phone_book):
    return dikt[name]


add_new_user('jerry', 8805345532)
add_new_user('garry', 5873265283)
print(get_number('garry'))
