import string
import json


def get_list_of_users(path="../testing_data/users.json"):
    with open(path, "r") as read_file:
        data = json.load(read_file)
        return data


def save_new_user(email: object, gender: object, first_name: object, last_name: object, password: object, birthdate: object, created: object,
                  path: object ="../testing_data/users.json") -> object:
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

