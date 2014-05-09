#!/usr/bin/env python

import unittest
import os.path
from gender_detector import Country, Name, Index, GenderDetector


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country('us')

    def test_use_country(self):
        self.assertTrue(os.path.isfile(self.country.file()))

    def test_non_existing_country(self):
        self.assertRaises(RuntimeError, Country, 'br')


class TestName(unittest.TestCase):
    def test_guess_gender(self):
        name = Name('Marcos', 'male', 10, 0)
        self.assertEqual('male', name.guess())

        name = Name('Mary', 'female', 0, 10)
        self.assertEqual('female', name.guess())

        name = Name('whoknows', 'unknown', 0, 0)
        self.assertEqual('unknown', name.guess())


class TestIndex(unittest.TestCase):
    def test_lazy_index(self):
        # Generate index only when it's needed
        index = Index()
        self.assertEqual(len(index.indices), 0)
        position = index('A')
        self.assertNotEqual(len(index.indices), 0)
        self.assertEqual(position, 87)

class TestGenderDetector(unittest.TestCase):
    def test_format_name(self):
        detector = GenderDetector()
        for name in ['mARCOS', ' Marcos ', 'Marcos    ', 'MARCOS']:
            self.assertEqual(
                detector._format_name(name),
                'Marcos'
            )

    def test_guessing(self):
        detector = GenderDetector()
        self.assertEqual(detector.guess('Marcos'), 'male')


if __name__ == '__main__':
    unittest.main()
