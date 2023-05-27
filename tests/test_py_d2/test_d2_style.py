# -*- coding: utf-8 -*-
from py_d2.style import D2Style


def test_d2_style():
    style = D2Style()
    assert str(style) == ""


def test_d2_style_fill():
    style = D2Style(fill="red")
    assert str(style) == "style: {\n  fill: red\n}"


def test_d2_style_stroke():
    style = D2Style(stroke="red")
    assert str(style) == "style: {\n  stroke: red\n}"


def test_d2_style_stroke_width():
    style = D2Style(stroke_width=2)
    assert str(style) == "style: {\n  stroke-width: 2\n}"


def test_d2_style_shadow():
    style = D2Style(shadow=True)
    assert str(style) == "style: {\n  shadow: true\n}"


def test_d2_style_opacity():
    style = D2Style(opacity=0.5)
    assert str(style) == "style: {\n  opacity: 0.5\n}"


def test_d2_style_stroke_dash():
    style = D2Style(stroke_dash=2)
    assert str(style) == "style: {\n  stroke-dash: 2\n}"


def test_d2_style_three_d():
    style = D2Style(three_d=True)
    assert str(style) == "style: {\n  3d: true\n}"


def test_d2_style_all():
    style = D2Style(
        stroke="red",
        stroke_width=2,
        fill="red",
        shadow=True,
        opacity=0.5,
        stroke_dash=2,
        three_d=True,
    )
    assert str(style) == "\n".join(
        [
            "style: {",
            "  stroke: red",
            "  stroke-width: 2",
            "  fill: red",
            "  shadow: true",
            "  opacity: 0.5",
            "  stroke-dash: 2",
            "  3d: true",
            "}",
        ]
    )
