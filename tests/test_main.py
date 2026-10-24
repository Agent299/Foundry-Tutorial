import io
import unittest
from contextlib import redirect_stdout

import foundry_tutorial


class MainTests(unittest.TestCase):
    def test_main_prints_greeting(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            foundry_tutorial.main()

        self.assertEqual(output.getvalue(), "Hello from foundry-tutorial!\n")


if __name__ == "__main__":
    unittest.main()
