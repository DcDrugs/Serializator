import unittest
import sys

sys.path.append(sys.path[0] + "/..")
from factory.factory import serializer
import math as m


class myclass:
    i = 0
    v = [0, 1, 2, 3, 4, 5]

    def func(self, x, y):
        res = 0

        def f(x, y):
            return x + y

        for i in self.v:
            res += m.sin(f(x, y) + i)
        return res


def get_json_myclass():
    fp = open("json_object/class_myclasss.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_myclass_obj():
    fp = open("json_object/build_myclasss.json", "r")
    res = fp.read()
    fp.close()
    return res


class LoadJson(unittest.TestCase):
    def test_load(self):
        my = serializer.get_parser("JSON").loads(get_json_myclass())
        self.assertEqual(my.func(my, 5, 6), myclass().func(5, 6))

    def test_dump_obj(self):
        my = serializer.get_parser("JSON").loads(get_json_myclass_obj())
        self.assertEqual(my.func(my, 5, 6), myclass().func(5, 6))


if __name__ == "__main__":
    unittest.main()
