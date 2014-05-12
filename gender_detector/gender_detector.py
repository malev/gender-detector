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
            for row in reader:
                if row[0] == name:
                    return self._guess(row)
            return self.unknown_value

    def _guess(self, row):
        gender = self.country.guess(row)
        if gender in ['male', 'female']:
            return gender
        else:
            return self.unknown_value

    def _format_name(self, name):
        name = name.strip()
        return name[0].upper() + name[1:].lower().strip()


if __name__ == "__main__":
    print __doc__
