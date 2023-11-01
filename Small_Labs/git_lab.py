"""Cannon Whitney 1"""


def encoder(password):
    password = str(password)

    new_password = ''

    for i in password:
        i = int(i)
        i = i + 3
        new_password += str(i)

    return new_password


def decoder(password):
    pass


def main():
    menu = """Menu
-------------
1. Encode
2. Decode
3. Quit"""

    while True:
        print(menu)
        menu_option = input('Please enter an option: ')

        if menu_option == '1':
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')

        elif menu_option == '2':
            print(f'decoded password: {decoder(password)}')

        elif menu_option == '3':
            quit()


