import random
import string
import json


def generate_unique_email():
    email = generate_email()
    if email_is_unique(email):
        return email
    else:
        generate_unique_email()


def email_is_unique(email):
    users = get_list_of_users()
    for key in users.keys():
        if key == email:
            return False
    return True


def get_list_of_users(path="../configuration/users.json"):
    with open(path, "r") as read_file:
        data = json.load(read_file)
        return data


def save_new_user(email: object, gender: object, first_name: object, last_name: object, password: object, birthdate: object, created: object,
                  path: object = "../configuration/users.json") -> object:
    data = get_list_of_users()
    new_user = {email: {
                "PASSWORD": password,
                "FIRST_NAME": first_name,
                "LAST_NAME": last_name,
                "GENDER": gender,
                "BIRTHDATE": birthdate,
                "CREATED": created
                }
            }

    data.update(new_user)
    with open(path, "w") as write_file:
        json.dump(data, write_file, indent=2)


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