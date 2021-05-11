import unittest
import sys

sys.path.append(sys.path[0] + "/..")
from tools.loader import load_class, get_load_obj
from json import loads
import math as m


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


def get_json_second():
    fp = open("json_object/class_second.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_third():
    fp = open("json_object/class_thirds.json", "r")
    res = fp.read()
    fp.close()
    return res


def get_json_myclass():
    fp = open("json_object/class_myclasss.json", "r")
    res = fp.read()
    fp.close()
    return res


class LoadClass(unittest.TestCase):
    def test_second(self):
        test = load_class(loads(get_json_second())[".castom_class"])
        my = second()
        self.assertEqual(my.i, test.i)
        self.assertEqual(my.v, test.v)

    def test_third(self):
        test = load_class(loads(get_json_third())[".castom_class"])
        my = third()
        self.assertEqual(my.i, test.i)
        self.assertEqual(my.v, test.v)
        self.assertEqual(my.func(10, 1), test.func(test, 10, 1))

    def test_myclass(self):
        test = load_class(loads(get_json_myclass())[".castom_class"])
        my = myclass()
        self.assertEqual(my.i, test.i)
        self.assertEqual(my.v, test.v)
        t = test.func(test, 10, 1)
        self.assertEqual(my.func(10, 1), test.func(test, 10, 1))


if __name__ == "__main__":
    unittest.main()
