import unittest

from src.intern_profile import intern_name, role, department, skills


class TestInternProfile(unittest.TestCase):

    def test_profile_data(self):
        self.assertTrue(intern_name)
        self.assertTrue(role)
        self.assertTrue(department)
        self.assertTrue(skills)

    def test_skills_are_list(self):
        self.assertIsInstance(skills, list)
        self.assertGreater(len(skills), 0)


if __name__ == "__main__":
    unittest.main()