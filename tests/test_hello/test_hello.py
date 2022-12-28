# -*- coding: utf-8 -*-
from hello import main


def test_hello():
    assert main.hello() == "Hello, world!"


def test_say_hello(capsys):
    main.say_hello()
    captured = capsys.readouterr()
    assert captured.out.index("Hello, world!") == 0
