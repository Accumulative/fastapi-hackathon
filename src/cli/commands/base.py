from asyncio import run
from functools import wraps
from typing import Callable

import typer


class AsyncTyper(typer.Typer):
    def async_command(self, _func: Callable = None, *args, **kwargs):
        def decorator(async_func):
            @wraps(async_func)
            def sync_func(*_args, **_kwargs):
                return run(async_func(*_args, **_kwargs))

            self.command(*args, **kwargs)(sync_func)
            return async_func

        if _func:
            return decorator(_func)
        return decorator
