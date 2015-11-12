#!/usr/bin/env python

import sys
import unittest
import os.path

# sys.path.append("../")

from ..gender_detector import GenderDetector
from gender_detector.country import Country
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


class TestGenderDetector(unittest.TestCase):
    def test_format_name(self):
        detector = GenderDetector()
        for name in ['mARCOS', ' Marcos ', 'Marcos    ', 'MARCOS']:
            self.assertEqual(
                detector._format_name(name),
                'Marcos'
            )

    def test_us_guessing(self):
        # test scanning csv file for name
        detector = GenderDetector('us')
        self.assertEqual(detector.guess('Marcos'), 'male')
        
    def test_ar_guessing(self):
        # test scanning csv file for name
        detector = GenderDetector('ar')
        self.assertEqual(detector.guess('Zulema'), 'female')
        
    def test_uk_guessing(self):
        # test scanning csv file for name
        detector = GenderDetector('uk')
        self.assertEqual(detector.guess('Xara'), 'female')

    def test_uy_guessing(self):
        # test scanning csv file for name
        detector = GenderDetector('uy')
        self.assertEqual(detector.guess('Aaroon'), 'male')


if __name__ == '__main__':
    unittest.main()
