import unittest
import string
from main import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        # Test case 1: Check if the default length is 8
        password_generator = PasswordGenerator()
        password = password_generator.generate_password()
        self.assertEqual(len(password), 8)

    def test_custom_length(self):
        # Test case 2: Check if the custom length is applied
        password_generator = PasswordGenerator(length=12)
        password = password_generator.generate_password()
        self.assertEqual(len(password), 12)

    def test_one_character_included(self):
        # Test case 3: Check if at least one character set is included
        password_generator = PasswordGenerator(include_uppercase=True, include_lowercase=True,
                                               include_digits=True, include_special_chars=True)
        password = password_generator.generate_password()

        self.assertTrue(any(c.isupper() for c in password) or
                        any(c.islower() for c in password) or
                        any(c.isdigit() for c in password) or
                        any(c in string.punctuation for c in password))

    def test_only_lowercase_included(self):
        # Test case 4: Check if only lowercase letters are included
        password_generator = PasswordGenerator(include_uppercase=False,
                                               include_digits=False, include_special_chars=False)
        password = password_generator.generate_password()
        self.assertTrue(all(c.islower() for c in password))

    def test_only_uppercase_included(self):
        # Test case 5: Check if only uppercase letters are included
        password_generator = PasswordGenerator(include_lowercase=False,
                                               include_digits=False, include_special_chars=False)
        password = password_generator.generate_password()
        self.assertTrue(all(c.isupper() for c in password))

    def test_only_digits_included(self):
        # Test case 6: Check if only digits are included
        password_generator = PasswordGenerator(include_uppercase=False,
                                               include_lowercase=False, include_special_chars=False)
        password = password_generator.generate_password()
        self.assertTrue(all(c.isdigit() for c in password))

    def test_only_special_characters_included(self):
        # Test case 7: Check if only special characters are included
        password_generator = PasswordGenerator(include_uppercase=False,
                                               include_lowercase=False, include_digits=False)
        password = password_generator.generate_password()
        self.assertTrue(all(c in string.punctuation for c in password))
        # password_generator = PasswordGenerator(length=8, include_uppercase=True, include_lowercase=True,
        #                                       include_digits=True, include_special_chars=True)
        # password = password_generator.generate_password()
        # self.assertEqual(len(password), 8)
        # self.assertTrue(any(c in string.ascii_uppercase for c in password) or
        #                 any(c in string.ascii_lowercase for c in password) or
        #                 any(c in string.digits for c in password) or
        #                 any(c in string.punctuation for c in password))
        # self.assertEqual(password, 'y')
        # self.assertEqual(password, 'y')
        # self.assertEqual(password, 'y')
        # self.assertEqual(password, 'y')

    # def test_no_character_sets_included(self):
    #     with self.assertRaises(ValueError):
    #         PasswordGenerator(length=8, include_uppercase=False, include_lowercase=False, include_digits=False,
    #                           include_special_chars=False)
    #
    # def test_default_values(self):
    #     password_generator = PasswordGenerator()
    #     password = password_generator.generate_password()
    #     self.assertIsInstance(password, str)
    #     self.assertEqual(len(password), 8)
    #     self.assertTrue(any(c.isupper() for c in password))
    #     self.assertTrue(any(c.islower() for c in password))
    #     self.assertTrue(any(c.isdigit() for c in password))
    #     self.assertTrue(any(c in string.punctuation for c in password))


if __name__ == '__main__':
    unittest.main()
