# -*- coding: utf-8 -*-
from py_d2.D2Connection import D2Connection


def test_d2_connection_label():
    connection = D2Connection(from_shape="a", to_shape="b", label="c")
    assert str(connection) == "a -> b: c"


def test_d2_connection_no_label():
    connection = D2Connection(from_shape="a", to_shape="b")
    assert str(connection) == "a -> b"
