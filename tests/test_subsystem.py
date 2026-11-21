from concurrent.futures import Future
from pytest_mock import MockFixture
from subsystem import Subsystem


def test_query(mocker: MockFixture):
    mocker.patch(
        "subsystem.chat",
        return_value={"message": {"content": "the answer"}},
    )
    future = Future[str]()
    thread = Subsystem("system instructions", "test-model").query(
        "the question", future
    )
    thread.join()
    assert future.result() == "the answer"


def test_query_with_error(mocker: MockFixture):
    mocker.patch("subsystem.chat", side_effect=RuntimeError("Ollama unavailable"))
    future = Future[str]()
    thread = Subsystem("system instructions", "test-model").query(
        "the question", future
    )
    thread.join()
    assert future.result() == "ERROR"
