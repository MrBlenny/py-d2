# -*- coding: utf-8 -*-
from py_d2.D2Connection import D2Connection
from py_d2.D2Connection import Direction


def test_d2_connection_label():
    connection = D2Connection(shape_1="a", shape_2="b", label="c")
    assert str(connection) == "a -> b: c"


def test_d2_connection_no_label():
    connection = D2Connection(shape_1="a", shape_2="b")
    assert str(connection) == "a -> b"


def test_d2_connection_direction_to():
    connection = D2Connection(shape_1="a", shape_2="b", direction=Direction.TO)
    assert str(connection) == "a -> b"


def test_d2_connection_direction_from():
    connection = D2Connection(shape_1="a", shape_2="b", direction=Direction.FROM)
    assert str(connection) == "a <- b"


def test_d2_connection_direction_both():
    connection = D2Connection(shape_1="a", shape_2="b", direction=Direction.BOTH)
    assert str(connection) == "a <-> b"


def test_d2_connection_direction_none():
    connection = D2Connection(shape_1="a", shape_2="b", direction=Direction.NONE)
    assert str(connection) == "a -- b"
