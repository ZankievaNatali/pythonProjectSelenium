import asyncio
import datetime
import logging
import random
import string


def random_num():
    """Generates random number"""
    return str(random.randint(111111, 999999))


def random_str(length=7):
    """Generates random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def wait_until_ok(timeout=5, period=0.25):
    """Retries function until ok (or 5 seconds)"""
    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(
                seconds=timeout
            )
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    log.warning(f"Catching : {err}")
                    if datetime.datetime.now() > end_time:
                        raise err
                    asyncio.sleep(period)

        return wrapper

    return decorator


def select(arg, pattern):
    """Return in list all values from <select> element """

    values = []
    for x, y in arg.__dict__.items():
        if not callable(getattr(arg, x)) and x.startswith(pattern):
            values.append(y)

    return values
