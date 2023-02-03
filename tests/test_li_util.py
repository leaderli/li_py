import unittest

from li import li_util


class LiUtilTestCase(unittest.TestCase):
    def test_dict_deep_get(self):
        # noinspection PyTypeChecker
        self.assertIsNone(li_util.dict_deep_get(None, None))
        self.assertIsNone(li_util.dict_deep_get({}, ["hello", "world"]))
        self.assertEqual("1", li_util.dict_deep_get({
            "hello": {
                "world": "1"
            }
        }, ["hello", "world"]))


if __name__ == '__main__':
    unittest.main()
