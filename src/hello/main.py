# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-02
# license: MIT
# description: print "hello world!"
# usage: poetry run python src/hello/main.py
# notes:


def hello() -> str:
    """Return hello world."""
    return "Hello, world!"


def say_hello() -> None:
    """Print hello world."""
    print(hello())


if __name__ == "__main__":
    say_hello()  # pragma: no cover
