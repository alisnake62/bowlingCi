import unittest

from bowlingCi import easy

class TestEasyMethods(unittest.TestCase):

    # test1

    #dernier modif
    
    def test_easy(self):
        # Arrange

        # Action
        testEasy = easy()

        # Assert
        self.assertEqual(testEasy, 1)

if __name__ == '__main__':
    unittest.main()
