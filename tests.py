import unittest

from bowlingCi import easy

class TestEasyMethods(unittest.TestCase):

    # test
    
    def test_easy(self):
        # Arrange

        # Action
        testEasy = easy()

        # Assert
        self.assertEqual(testEasy, 1)

if __name__ == '__main__':
    unittest.main()
