a = [
    123456789,
    124356789,
    123456779,
    124356769,
]
# jakub
def phone(number):
    try:
        if number in a:
            return number
        else:
            raise Exception("There is no such number!")
    except Exception as e:
        return e

# jarek
def phone_num(number):
    try:
        if not isinstance(number, int):
            raise ValueError("Invalid input")
        if number in a:
            return number
        else:
            raise Exception("The number is not in the list")
    except ValueError as ve:
        return str(ve)


print(phone_num(12345654489))