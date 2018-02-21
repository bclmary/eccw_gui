#!/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Various shared tools.
"""


def float_check(value, default=None):
    """value must be a float or default."""
    try:
        return float(value)
    except ValueError:
        return default


def str_check(value, default=''):
    """value must be a string or default."""
    if value is None:
        return default
    else:
        return str(value)


def _is_leaf(elt):
    """Return True if elt if not an iterable."""
    if isinstance(elt, dict):
        return False
    elif isinstance(elt, list):
        return False
    elif isinstance(elt, tuple):
        return False
    else:
        return True


def graph_print(elt, indent=0, level=0):
    """Print 'elt' and all its contained elements (if any) in a pretty way.

**How dictionaries are printed**
::

    { key1     : value1
      key2     : value2
      ...
      last_key : valueN
    }

**How lists are printed**
::

    [ 0   : value1
      1   : value2
     ...
      N-1 : valueN
    ]

**How tuples are printed**
::

    ( 0   : value1
      1   : value2
     ...
      N-1 : valueN
    )

.. note:: If lists or tuples are leafs of the graph (ie they do not contains
          iterable elements) they are printed simply using repr().

"""
    if level == 0:
        print(" "*indent, end="")
    if isinstance(elt, dict):
        print("{ ", end="")
        keysizemax = max([len(key) for key in elt.keys()])
        m = indent + 2
        for i, (key, value) in enumerate(elt.items()):
            n = keysizemax - len(key)
            if i != 0:
                print("\n" + " "*(indent + 2), end="")
            print(str(key) + " "*n + " : ", end="")
            graph_print(value, indent + keysizemax + 5, level+1)
        print("\n" + " "*(m-2) + "}", end="")
    elif isinstance(elt, (list, tuple)):
        if all([_is_leaf(e) for e in elt]):
            print(repr(elt), end="")
        else:
            A = "[" if isinstance(elt, list) else "("
            Z = "]" if isinstance(elt, list) else ")"
            print(A + " ", end="")
            indexsizemax = len(str(len(elt)-1))
            m = indent + 2
            for i, value in enumerate(elt):
                n = indexsizemax - len(str(i))
                if i != 0:
                    print("\n" + " "*(indent + 2), end="")
                print(str(i) + " "*n + " : ", end="")
                graph_print(value, indent + indexsizemax + 5, level+1)
            print("\n" + " "*(m-2) + Z, end="")
    else:
        print(repr(elt), end="")
    if level == 0:
        print()


if __name__ == "__main__":

    from collections import OrderedDict as OD

    test = OD([
        ("value", 1.),
        ("text", "foo"),
        ("bool", True),
        ("dict", OD([
            ("value", 1.),
            ("text", "foo"),
            ("bool", True),
            ("tuple", (1, 2, 3)),
            ("list", ["A", "B", "C"])
            ])),
        ("list", [1., "foo", True, (1, 2, 3), ["A", "B", "C"]]),
        ("tuple", (1., "foo", True, (1, 2, 3), ["A", "B", "C"]))
        ])
    graph_print(test)  # , indent=4)
