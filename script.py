#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simple Calculator Script"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"

if __name__ == "__main__":
    x, y = 79, 36
    print(f"Addition: {x} + {y} = {add(x, y)}")
    print(f"Subtraction: {x} - {y} = {subtract(x, y)}")
    print(f"Multiplication: {x} * {y} = {multiply(x, y)}")
    print(f"Division: {x} / {y} = {divide(x, y)}")
