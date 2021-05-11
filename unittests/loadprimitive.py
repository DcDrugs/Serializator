import unittest
import sys

sys.path.append(sys.path[0] + "/..")
from tools.loader import load_list, load_dict, load_primitive


class LoadPrimitive(unittest.TestCase):
    def test_int(self):
        i = 0
        self.assertEqual(load_primitive(i), i)

    def test_bool(self):
        i = True
        self.assertEqual(load_primitive(i), i)

    def test_str(self):
        i = "hi"
        self.assertEqual(load_primitive(i), i)

    def test_list1(self):
        i = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(load_list(i), i)

    def test_list2(self):
        i = ["str", True, 3, 4, 5, 6, None]
        self.assertEqual(load_list(i), i)

    def test_list3(self):
        i = [["str", 0], [[[0, 0], 0], True], True, 3, 4, 5, 6, None]
        self.assertEqual(load_list(i), i)

    def test_dict1(self):
        i = {"str": True, 3: 4, 5: 6, None: True}
        self.assertEqual(load_dict(i), i)

    def test_dict2(self):
        t = {"str": True, 3: {"None": True, True: True}}
        self.assertEqual(load_dict(t), t)


if __name__ == "__main__":
    unittest.main()
