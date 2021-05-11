import unittest
import sys

sys.path.append(sys.path[0] + "/..")
from factory.factory import serializer


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


def get_yaml_myclass():
    fp = open("json_object/class_myclass.yaml", "r")
    res = fp.read()
    fp.close()
    return res


def get_yaml_myclass_obj():
    fp = open("json_object/builds_myclass.yaml", "r")
    res = fp.read()
    fp.close()
    return res


class DumpYaml(unittest.TestCase):
    def test_dump(self):
        self.assertEqual(
            serializer.get_parser("Yaml").dumps(myclass), get_yaml_myclass()
        )

    def test_dump_obj(self):
        self.assertEqual(
            serializer.get_parser("Yaml").dumps(myclass()),
            get_yaml_myclass_obj(),
        )


if __name__ == "__main__":
    unittest.main()
