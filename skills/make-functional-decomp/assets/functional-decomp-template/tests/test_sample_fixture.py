from pathlib import Path
import unittest


class SampleFixtureTest(unittest.TestCase):
    def test_sample_fixture_exists(self):
        fixture = Path("tests/fixtures/generated/sample.bin")
        self.assertTrue(fixture.exists())
        self.assertTrue(fixture.read_bytes().startswith(b"DECOMP"))


if __name__ == "__main__":
    unittest.main()
