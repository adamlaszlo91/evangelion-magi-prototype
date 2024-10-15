from ascii_logo import ascii_logo
from threading import Thread

"""
Magi-1: Melchior: Dr. Naoko Akagi as a scientist;
Magi-2: Balthasar: Dr. Naoko Akagi as a mother;
Magi-3: Casper: Dr. Naoko Akagi as a woman.
"""
answers = [None, None, None]


def acquire_melchior_response(input: str) -> None:
    response = 'yo'
    answers[0] = response
    print(f'Melchior: {response}')


def acquire_balthasar_response(input: str) -> None:
    response = 'yo'
    answers[1] = response
    print(f'Balthasar: {response}')


def acquire_casper_response(input: str) -> None:
    response = 'yo'
    answers[2] = response
    print(f'Casper: {response}')


def collect_responses(input: str) -> str:
    thread1 = Thread(target=acquire_melchior_response, args=[input])
    thread1.start()
    thread2 = Thread(target=acquire_balthasar_response, args=[input])
    thread2.start()
    thread3 = Thread(target=acquire_casper_response, args=[input])
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    return '\n'.join(answers)


def main() -> None:
    print(ascii_logo)

    print('Magi System prototype')
    while True:
        print()
        user_input = input('Input: ')
        if user_input == 'q':
            print('Exiting...')
            return
        else:
            print(collect_responses(input=user_input))


if __name__ == '__main__':
    orange = '\033[38;5;208m'
    print(orange)
    main()
