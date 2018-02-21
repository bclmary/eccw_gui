#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Wrappers used on the base elements of the GUI.
They add automated setting and getting of needed parameters.
Wrapped parameters are iteratively setted / gotten.
This allows saving and loading sessions with the GUI.
"""


from collections import OrderedDict


class Wrapper(object):
    """Wrapping non iterable parameter."""

    def __init__(self, arg=None, action=lambda x: None, process=lambda x: x):
        self.process = process
        self.action = action
        self.set_params(arg=arg)

    def get_params(self):
        return self.value

    def set_params(self, arg):
        self.value = self.process(arg)
        self.action(self.value)

    def get_select(self):
        return self.get_params()


class WrapperDict(object):
    """Wrapping parameters stored in a dictionary."""

    def __init__(self, arg=OrderedDict()):
        self.dict = arg

    def get_params(self):
        return OrderedDict([(key, value.get_params()) for key, value
                            in self.dict.items()])

    def set_params(self, **kwargs):
        parser = {key: value.set_params for key, value in self.dict.items()}
        self.check_params(parser, kwargs)

    def get_select(self):
        return OrderedDict([(key, value.get_select()) for key, value
                            in self.dict.items()])

    def check_params(self, parser, params):
        name = self.__class__.__name__
        if isinstance(params, dict):
            try:
                for key, value in params.items():
                    if isinstance(value, dict):
                        parser[key](**value)
                    else:
                        parser[key](value)
            except KeyError:
                raise TypeError(name+"() gets unknown keyword argument '"
                                + str(key) + "'.")
        else:
            raise TypeError(name+"() awaits a dict as argument.")


class WrapperList(object):
    """Wrapping parameters stored in a list."""

    def __init__(self, arg=[]):
        self.list = list(arg)

    def get_params(self):
        return [elt.get_params() for elt in self.list]

    def set_params(self, paramsList):
        for i, params in enumerate(paramsList):
            if isinstance(params, dict):
                self.list[i].set_params(**params)
            else:
                self.list[i].set_params(params)

    def get_select(self):
        return [elt.get_select() for elt in self.list]


if __name__ == "__main__":

    x = "something"
    W = Wrapper(x)
    print(W.get_params())

