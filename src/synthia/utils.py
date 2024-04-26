import sys
import random
from time import sleep
import time
from typing_extensions import Callable, TypeVar, ParamSpec, Literal, Any, Optional
import datetime
from functools import wraps
from pydantic import decorator

T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")

P = ParamSpec("P")
R = TypeVar("R")


def timeit(func: Callable[P, R]):
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        log(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper


def iso_timestamp_now() -> str:
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    return now.isoformat()


def log(
        msg: str,
        *values: object,
        sep: str | None = " ",
        end: str | None = "\n",
        file: Any | None = None,
        flush: Literal[False] = False
    ):
    print(
        f"[{iso_timestamp_now()}] {msg}",
        *values,
        sep=sep,
        end=end,
        file=file,
        flush=flush,
    )

class RetryException(Exception):
    """An exception that can be retried."""
    pass


@decorator.decorator(retry=RetryException)
def retry(
    max_retries: Optional[int]= None,
    func: Optional[Callable[P, T]]= None
    ) -> object:
    """
    Retry a function if it raises one of the specified exceptions.

    The decorated function should not return None.
    """
    assert max_retries is None or max_retries > 0
    if not func:
        raise ValueError("'func' must be provided")

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            max_retries_ = max_retries or 1
            for _ in range(max_retries_ + 1):
                try:
                    if isinstance(func, Callable):
                        result: Optional[T] = func(retry=RetryException, **args, **kwargs)  # type: ignore
                        assert result is not None, f"func '{func.__name__}' returned None"
                    else:
                        raise ValueError(f"'func' is not callable: {func}")
                    return result  # type: ignore
                except Exception as e:
                    log(
                        f"An exception occurred in '{func.__name__}': {e}, "
                        f"but we'll retry (try {_ + 1} of {max_retries_})."
                    )
                    delay = 1.4 ** _ + random.uniform(0, 1)
                    sleep(delay)
                    continue
            func_name = func.__name__
            raise Exception(
                f"The function '{func_name}' failed {max_retries_} times. "
                f"Please check for bugs such as NullPointerException, "
                f"unhandled exceptions, and more."
            ) from None

    return wrapper


