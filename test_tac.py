"""
Unit tests for TAC Generator
"""
import pytest
from tac_generator import TACGenerator


def test_simple_addition():
    gen = TACGenerator()
    result = gen.generate("x = a + b")
    assert "x = a + b" in result or "t1 = a + b" in result


def test_multiplication_precedence():
    gen = TACGenerator()
    result = gen.generate("x = a + b * c")
    lines = result.split('\n')
    assert len(lines) == 2
    assert "b * c" in lines[0]
    assert "+" in lines[1]


def test_parentheses():
    gen = TACGenerator()
    result = gen.generate("x = (a + b) * c")
    lines = result.split('\n')
    assert "+" in lines[0]
    assert "*" in lines[1]


def test_complex_expression():
    gen = TACGenerator()
    result = gen.generate("x = a + b * c - d / e")
    lines = result.split('\n')
    assert len(lines) == 4


def test_multiple_generations():
    gen = TACGenerator()
    gen.generate("x = a + b")
    result = gen.generate("y = c * d")
    assert "t1" in result
    assert "y = t1" in result or "t" in result


def test_nested_parentheses():
    gen = TACGenerator()
    result = gen.generate("x = ((a + b) * (c - d))")
    assert len(result.split('\n')) >= 3
