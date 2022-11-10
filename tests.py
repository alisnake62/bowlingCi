import unittest

from bowlingCi import easy

class TestEasyMethods(unittest.TestCase):

    def test_easy(self):
        # Arrange

        # Action
        easyTest = easy()

        # Assert
        self.assertEqual(easyTest, 1)

if __name__ == '__main__':
    unittest.main()