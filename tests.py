import unittest

from bowlingCi import easy

class TestEasyMethods(unittest.TestCase):

    # testtest
    # testtest111
    # testtest
    # testtest
    # testtest
    # test2
    # test3
    # test3
    # test3
    # test3

    #dernier modif
    
    def test_easy(self):
        # Arrange

        # Action
        testEasy = easy()

        # Assert
        self.assertEqual(testEasy, 2)

if __name__ == '__main__':
    unittest.main()
