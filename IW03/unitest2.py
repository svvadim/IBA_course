import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(
       main.fulname('Бурмакова',
                    'Анастасия',
                    'Владимировна'),
            'Бурмакова Анастасия Владимировна'
                    )
    def test_big(self):
        self.assertEqual(
       main.fulname('Бурмакова',
                    'АНАСТАСИЯ',
                    'ВЛАДИМИРОВНА'),
            'Бурмакова Анастасия Владимировна'
                    )
    def test_small(self):
        self.assertEqual(
       main.fulname('бурмакова',
                    'анастасия',
                    'владимировна'),
            'Бурмакова Анастасия Владимировна'
                    )

if __name__ == '__main__':
    unittest.main()
