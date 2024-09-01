import unittest
from unittest.mock import patch
from io import StringIO
from HelloWorld import main

class TestHelloWorld(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_output(self, mock_stdout):
        # Call the main function
        main()
        # Get the output printed by the main function
        output = mock_stdout.getvalue()
        # Check if the output matches the expected string
        self.assertEqual(output.strip(), "Like this!!\nHello, World")

if __name__ == '__main__':
    unittest.main()
