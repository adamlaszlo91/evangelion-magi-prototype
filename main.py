from ascii_logo import ascii_logo


def main() -> None:
    print(ascii_logo)

    print('Magi System prototype')
    print()
    while True:
        user_input = input('Input: ')
        if user_input == 'q':
            print('Exiting...')
            return
        else:
            print('OK')


if __name__ == '__main__':
    orange = '\033[38;5;208m'
    print(orange)
    main()
