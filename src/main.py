from ascii_logo import ASCII_LOGO
from threading import Thread
from subsystem import SubSystem
from concurrent.futures import Future

OLLAMA_MODEL = "llama3.2:latest"
PERSONAS = (("Melchior", "scientist"), ("Balthazar", "mother"), ("Caspar", "woman"))

SUBSYSTEM_PROMPT = "Act as a {}. You will be asked to make a decision. Answer in one sentence, period. Do not ask back."
SYSTEM_PROMPT = 'A decision making request has been made:\n"{}"\n\nMultiple proposals have been created:\n{}\n\nSelect the one idea with the most support. Answer in one sentence, period. Do not ask back.'


def collect_result(input: str):
    threads: list[Thread] = []
    results: dict[str, Future[str]] = {}
    for name, role in PERSONAS:
        future = Future[str]()
        results[name] = future
        threads.append(
            SubSystem(SUBSYSTEM_PROMPT.format(role), OLLAMA_MODEL).query(
                input, result=future
            )
        )

    for thread in threads:
        thread.join()

    for name, role in PERSONAS:
        print()
        print(f"{name} ({role})\n{results[name].result()}")

    print()
    print("Verdict:")
    verdict_result = Future[str]()
    SubSystem(
        SYSTEM_PROMPT.format(
            input, "\n\n".join([f'"{r.result()}"' for r in results.values()])
        ),
        OLLAMA_MODEL,
    ).query(input, result=verdict_result).join()
    print(verdict_result.result())


def main() -> None:
    print(ASCII_LOGO)
    print("Magi System prototype")
    while True:
        print()
        user_input = input("Input: ")
        if user_input == "q":
            print("Exiting...")
            return
        else:
            collect_result(input=user_input)


if __name__ == "__main__":
    orange = "\033[38;5;208m"
    print(orange)
    main()
