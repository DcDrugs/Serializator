import unittest
import sys

sys.path.append(sys.path[0] + "/..")
from tools.dumper import dump_class
from json import dumps


class first:
    pass


class second:
    i = 0
    v = [0, 1, 2, 3]


class third:
    i = 3
    v = [0, 1, 2, 3]

    def func(self, x, y):
        k = sum(v)
        return x + y + i + k


class third:
    i = 3
    v = [0, 1, 2, 3]

    def func(self, x, y):
        k = 0
        for item in self.v:
            k += item
        return x + y + self.i + k

    def func1(self, x, y):
        k = sum(v) + 2
        return x + y + i + k


class myclass_dict:
    i = 0
    v = [0, 1, 2, 3, 4, 5]
    item = {"get": "set"}

    def func(self, x, y):
        res = 0

        def f(x, y):
            return x + y

        for i in self.v:
            res += m.sin(f(x, y) + i)
        return res


def get_json_first():
    fp = open("json_object/class_first.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_second():
    fp = open("json_object/class_second.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_third():
    fp = open("json_object/class_third.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_myclass_dict():
    fp = open("json_object/class_myclass_dict.json", "r")
    res = fp.read()
    fp.close()
    return res


class DumpClass(unittest.TestCase):
    def test_class(self):
        self.assertEqual(dumps(dump_class(first), indent=4), get_json_first())
        self.assertEqual(dumps(dump_class(second), indent=4), get_json_second())
        self.assertEqual(dumps(dump_class(third), indent=4), get_json_third())
        self.assertEqual(
            dumps(dump_class(myclass_dict), indent=4), get_json_myclass_dict()
        )


if __name__ == "__main__":
    unittest.main()
