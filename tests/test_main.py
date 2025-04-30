import unittest
from src.main import main
from io import StringIO
import sys

class TestMain(unittest.TestCase):
    def test_main(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
