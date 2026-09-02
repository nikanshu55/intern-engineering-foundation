import unittest

from src.intern_profile import intern_name, role, department, skills


class TestInternProfile(unittest.TestCase):

    def test_profile_data(self):
        self.assertTrue(intern_name)
        self.assertTrue(role)
        self.assertTrue(department)
        self.assertTrue(skills)


if __name__ == "__main__":
    unittest.main()