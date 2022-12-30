import unittest

from bowlingCi import easy

class TestEasyMethods(unittest.TestCase):

    # test2
    # test3
    # test4
    # test5

    #dernier modif
    
    def test_easy(self):
        # Arrange

        # Action
        testEasy = easy()

        # Assert
        self.assertEqual(testEasy, 2)

if __name__ == '__main__':
    unittest.main()
