import EE308_lab2
import unittest
class test(unittest.TestCase):
    def test_first_level(self):
        self.assertEqual(EE308_lab2.first_level(), 35)
    def test_second_level(self):
        self.assertEqual(EE308_lab2.second_level(),[3,2])
    def test_third_level(self):
        self.assertEqual(EE308_lab2.third_level(),2)
    def test_fourth_level(self):
        self.assertEqual(EE308_lab2.fourth_level(),2)
if __name__ == '__main__':
    unittest.main()
