from py_d2.D2Link import D2Link


def test_d2_link_label():
    link = D2Link(from_node="a", to_node="b", label="c")
    assert str(link) == "a -> b: c"


def test_d2_link_no_label():
    link = D2Link(from_node="a", to_node="b")
    assert str(link) == "a -> b"
