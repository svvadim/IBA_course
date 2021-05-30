#!/usr/bin/env python3
import unittest

import HWS


class MyTestCase(unittest.TestCase):
    def test_break_into_squares(self):
        self.assertEqual(HWS.break_into_squares(20, 30), 3)

    def test_sum_digit(self):
        self.assertEqual(HWS.sum_digit(1111111111), 10)

    def test_lucky_tickets(self):
        self.assertEqual(len(HWS.lucky_tickets(0, 100000)), 1)

    def test_lucky_tickets_2(self):
        test_value = ['69999 and 70000',
                      '159999 and 160000',
                      '249999 and 250000',
                      '339999 and 340000',
                      '429999 and 430000'
                      ]
        for result in HWS.lucky_tickets(0, 430001):
            self.assertIn(result, test_value)


if __name__ == '__main__':
    unittest.main()
