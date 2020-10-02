import random
import string
from test_data import manage_test_data


def generate_unique_email():
    email = generate_email()
    if email_is_unique(email):
        return email
    else:
        generate_unique_email()


def email_is_unique(email):
    users = manage_test_data.get_list_of_users()
    for key in users.keys():
        if key == email:
            return False
    return True


def generate_email():
    length_username = random.randint(3, 15)
    email = ''.join(random.choice(string.ascii_lowercase) for _ in range(1))
    email = email + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length_username-1))
    email = email + "@"
    length_domain_name = random.randint(3, 10)
    email = email + ''.join(random.choice(string.ascii_lowercase) for _ in range(1))
    email = email + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length_domain_name-1))
    email = email + "."
    length_domain = random.randint(3, 8)
    email = email + ''.join(random.choice(string.ascii_lowercase) for _ in range(length_domain))
    return email


def generate_first_name():
    length_first_name = random.randint(3, 10)
    first_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    first_name = first_name + ''.join(random.choice(string.ascii_lowercase) for _ in range(length_first_name-1))
    return first_name


def generate_last_name():
    length_last_name = random.randint(3, 10)
    last_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    last_name = last_name + ''.join(random.choice(string.ascii_lowercase) for _ in range(length_last_name-1))
    return last_name


def generate_password():
    length_password = random.randint(8, 20)
    password = ''.join(random.choice(string.printable[:-6]) for _ in range(length_password))
    return password


def generate_birthdate():
    month = random.randint(1, 12)
    if month < 10:
        month = "0" + str(month)
    day = random.randint(1, 28)
    if day < 10:
        day = "0" + str(day)
    year = random.randint(1920, 2001)
    birthdate = str(month) + "/" + str(day) + "/" + str(year)
    return birthdate
