#!/usr/bin/env python

import sys
import unittest
import os.path

# sys.path.append("../")

from gender_detector import GenderDetector
from gender_detector.country import Country
from gender_detector.index import Index
from gender_detector.binomy import Binomy


class TestBinomy(unittest.TestCase):
    def test_enough_confidence(self):
        self.assertTrue(not Binomy(5,5).enough_confidence())
        self.assertTrue(not Binomy(0,1).enough_confidence())
        self.assertTrue(Binomy(0,6).enough_confidence())


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country('us')

    def test_use_country(self):
        self.assertTrue(os.path.isfile(self.country.file()))

    def test_non_existing_country(self):
        self.assertRaises(RuntimeError, Country, 'br')

    def test_guesser_method(self):
        country = Country('ar')
        self.assertEqual(country._guesser_method().__name__, 'no_method')


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
        detector = GenderDetector('us')
        self.assertEqual(detector.guess('Marcos'), 'male')


if __name__ == '__main__':
    unittest.main()
