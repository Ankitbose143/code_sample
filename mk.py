import unittest
from unittest.mock import MagicMock
from tradd import my_function
from unittest.mock import patch

# def add(arg1, arg2):
#     return int(arg1+arg2)
#
# class testc(unittest.TestCase):
#     def test(self):
#         mck= MagicMock()
#         mck2 = MagicMock()
#         mck.return_value = 2
#         mck2.return_value = 5
#         mck.assert_called_once()
#         mck2.assert_called_once()
#         self.assertEqual(add(mck,mck2), 7)
#
#
# if __name__ == '__main__':
#     unittest.main()
#     # print(test)

# import unittest
# from unittest.mock import MagicMock

def my_function(arg1, arg2):
    # This is the function that you want to test
    print("enter myfnct")
    result1 = arg1 + arg2
    print("+++",result1)
    return int(result1)

class MyTestCase(unittest.TestCase):
    # @patch('mk.my_function')
    @patch('tradd.my_function')
    def test_my_function(self, mock_my_function):
        # Create a mock object
        mock_arg1 = MagicMock(return_value=9)
        mock_arg2 = MagicMock(return_value=2)
        mock_my_function.return_value = 7
        mock_arg1 = 4
        mock_arg2 = 2
        # Call the function with the mock objects
        print("----mck", int(mock_arg1), int(mock_arg2), mock_arg1)
        result = my_function(int(mock_arg1), int(mock_arg2))
        print("Resss", result, int(result))
        print("----",mock_my_function.return_value,"===", result)
        # Verify that the function was called with the mock objects
        # mock_arg1.assert_called_once()
        # mock_arg2.assert_called_once()
        mock_my_function.return_value = 7
        # Verify that the function returned the expected result
        self.assertEqual(result, mock_my_function.return_value)

if __name__ == '__main__':
    unittest.main()