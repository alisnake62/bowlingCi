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
    # test4
    # test5
    # test6# test7
    # test8
    # test9# test10
     # test9# test11
     # test12
     # test13

    #dernier modif
    
    def test_easy(self):
        # Arrange

        # Action
        testEasy = easy()

        # Assert
        self.assertEqual(testEasy, 1)

if __name__ == '__main__':
    unittest.main()
