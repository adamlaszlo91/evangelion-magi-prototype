from ascii_logo import ascii_logo
from threading import Thread
import ollama

system_prompt = 'A decision making request has been made: \"{}\"\nThree proposals have been made:\n\"{}\"\n\"{}\"\n\"{}\"\nCreate a final proposal based on thre previous ones! Answer in one sentence maximum.'
subsystem_prompt = 'Act as a decision making subsystem (part of Magi from Neon Genesis Evangelion.). You propose decisions from the point of view of a {}. Answer in one sentence maximum.'
answers = [None, None, None]


def acquire_melchior_response(input: str) -> None:
    answers[0] = None
    response = ollama.chat(model='llama3.1', messages=[{'role': 'system', 'content': subsystem_prompt.format('scientist')},
                                                       {'role': 'user', 'content': input}],)['message']['content']
    answers[0] = response
    print(f'Melchior: {response}')


def acquire_balthasar_response(input: str) -> None:
    answers[1] = None
    response = ollama.chat(model='llama3.1', messages=[{'role': 'system', 'content': subsystem_prompt.format('mother')},
                                                       {'role': 'user', 'content': input}],)['message']['content']
    answers[1] = response
    print(f'Balthasar: {response}')


def acquire_casper_response(input: str) -> None:
    answers[2] = None
    response = ollama.chat(model='llama3.1', messages=[{'role': 'system', 'content': subsystem_prompt.format('woman')},
                                                       {'role': 'user', 'content': input}],)['message']['content']
    answers[2] = response
    print(f'Casper: {response}')


def collect_responses(input: str) -> str:
    print()
    thread1 = Thread(target=acquire_melchior_response, args=[input])
    thread1.start()
    thread2 = Thread(target=acquire_balthasar_response, args=[input])
    thread2.start()
    thread3 = Thread(target=acquire_casper_response, args=[input])
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print()
    print('Suggestion:')
    response = ollama.chat(model='llama3.1', messages=[{'role': 'system', 'content': system_prompt.format(input, answers[0], answers[1], answers[2])},
                                                       {'role': 'user', 'content': '\n\n'.join(answers)}],)['message']['content']
    return response


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
