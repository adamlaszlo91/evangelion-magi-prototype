from threading import Thread
from concurrent.futures import Future
from ollama import chat  # type: ignore


class SubSystem:

    def __init__(self, system_prompt: str, ollama_model: str) -> None:
        self._system_prompt = system_prompt
        self._ollama_model = ollama_model

    def query(self, prompt: str, result: Future[str]) -> Thread:
        thread = Thread(target=self._query, args=[prompt, result])
        thread.start()
        return thread

    def _query(self, prompt: str, result: Future[str]):
        try:
            response = chat(
                model=self._ollama_model,
                messages=[
                    {"role": "system", "content": self._system_prompt},
                    {"role": "user", "content": prompt},
                ],
            )["message"]["content"]
            result.set_result(response)
        except:
            result.set_result("ERROR")
