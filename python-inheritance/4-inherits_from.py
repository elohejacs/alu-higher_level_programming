#!/usr/bin/python3
"""This module defines a function"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
