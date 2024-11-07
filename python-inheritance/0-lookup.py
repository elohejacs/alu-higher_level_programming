#!/usr/bin/python3
"""Defines a single function `lookup` that returns the list"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
