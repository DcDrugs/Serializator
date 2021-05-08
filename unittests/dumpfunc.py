import unittest
import sys

sys.path.append(sys.path[0] + "/..")
from tools.dumper import dump_func
import math as m
from tools.inspector import is_primitive
from json import dumps
import json_object


def func():
    pass


def hello():
    print("Hello, World!")


def params(x):
    print(x)


def sum(x, y):
    return x + y


def something(x, y):
    c = 3
    return x * y / c


def module_add(x, y):
    return m.sin(x + y)


def func_in_func(x, y):
    def f(x, y):
        return x + y

    return is_primitive(m.sin(f(x, y)) ** 33)


def get_json_func():
    fp = open("json_object/func.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_hello():
    fp = open("json_object/hello.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_params():
    fp = open("json_object/params.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_sum():
    fp = open("json_object/sum.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_something():
    fp = open("json_object/something.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_module_add():
    fp = open("json_object/module_add.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_func_in_func():
    fp = open("json_object/func_in_func.json", "r")
    res = fp.read()
    fp.close()
    return res


class DumpFunc(unittest.TestCase):
    def test_func_only(self):
        self.assertEqual(dumps(dump_func(func), indent=4), get_json_func())
        self.assertEqual(dumps(dump_func(hello), indent=4), get_json_hello())
        self.assertEqual(dumps(dump_func(params), indent=4), get_json_params())
        self.assertEqual(dumps(dump_func(sum), indent=4), get_json_sum())
        self.assertEqual(
            dumps(dump_func(something), indent=4), get_json_something()
        )

    def test_add_module(self):
        self.assertEqual(
            dumps(dump_func(module_add), indent=4), get_json_module_add()
        )

    def test_func_in_func(self):
        self.assertEqual(
            dumps(dump_func(func_in_func), indent=4), get_json_func_in_func()
        )


if __name__ == "__main__":
    unittest.main()
