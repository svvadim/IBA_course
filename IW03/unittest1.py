import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_something_2(self):
        self.assertNotEqual(True, False)


if __name__ == '__main__':
    unittest.main()
