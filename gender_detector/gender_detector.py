#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2014 Marcos Vanetta
#
# Author: Marcos Vanetta <marcosvanetta@gmail.com>
#


import csv
from country import Country
from index import Index
from name import Name


class GenderDetector:
    def __init__(self, country='us', unknown_value='unknown'):
        self.index = Index(country)
        self.country = Country(country)
        self.unknown_value = unknown_value

    def guess(self, name):
        name = self._format_name(name)
        initial_position = self.index(name[0])
        with open(self.country.file()) as csvfile:
            csvfile.seek(initial_position)
            reader = csv.reader(csvfile)
            for line in reader:
                if line[0] == name:
                    return self._guesser(line)
            return self.unknown_value

    def _guesser(self, row):
        name = row[0]
        gender = row[4]
        male_count = int(row[2])
        female_count = int(row[3])
        return Name(name, gender, male_count, female_count).guess()

    def _format_name(self, name):
        name = name.strip()
        return name[0].upper() + name[1:].lower().strip()


if __name__ == "__main__":
    print __doc__
