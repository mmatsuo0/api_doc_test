#!/usr/bin/env python

"""
module
version 0.0.2 edit
"""


class Class:
    """
    Class
    """
    def __init__(self):
        """
        init
        """
        pass

    def method(self):
        """
        method
        """
        pass

    def method2(self, a):
        """
        method2

        :param int a:
        """
        print(a)

    def method3(self, a):
        """
        method3

        :param a: description
        :type a: str
        """
        print(a)


def func(s, x):
    """
    function

    :param s: s
    :param x: x
    :return: return
    """
    p = 's: {}, x: {}'.format(s, x)
    return p
