#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2014 Marcos Vanetta
#
# Author: Marcos Vanetta <marcosvanetta@gmail.com>
#


import csv
import os
import sys
import io
from .country import Country


class GenderDetector:
    def __init__(self, country='us', unknown_value='unknown'):
        self.country = Country(country)
        self.unknown_value = unknown_value
        self.country_names = self._load_data()

    def guess(self, name):
        name = self._format_name(name)
        
        # get name info from dict
        if name in self.country_names:
            return self._guess(self.country_names[name])
        else:
            return self.unknown_value

    def _guess(self, name_info):
        gender = self.country.guess(name_info)
        if gender in ['male', 'female']:
            return gender
        else:
            return self.unknown_value                
    
    def _load_data(self):
        names = {}
        
        # ensure the right codec is being used for each CSV file
        encodings = {'ukprocessed.csv': 'utf8',
                     'usprocessed.csv': 'utf8',
                     'uyprocessed.csv': 'latin1',
                     'arprocessed.csv': 'latin1'}
        
        filepath = self.country.file()
        filename = os.path.basename(self.country.file())

        '''
        Useful snippet for reading non-unicode characters taken from ShadowRanger's
        answer here:
        http://stackoverflow.com/questions/33677586/handling-non-utf8-characters-in-csv-in-python-3-vs-python-2
        '''
        with io.open(filepath, encoding=encodings[filename], newline='') as csvdata:
            if sys.version_info[0] == 2:
                # Lazily convert lines from unicode to utf-8 encoded str
                csvdata = (line.encode('utf-8') for line in csvdata)
            reader = csv.reader(csvdata)
            if sys.version_info[0] == 2:
                # Decode row values to unicode on Py2; they're already str in Py3
                reader = ([x.decode('utf-8') for x in row] for row in reader)
    
            for row in reader:
                names[row[0]] = {
                    'name': row[0],
                    'gender': row[4],
                    'male_count': row[2],
                    'female_count': row[3]
                }
            
        return names

    def _format_name(self, name):
        name = name.strip()
        return name[0].upper() + name[1:].lower().strip()


if __name__ == "__main__":
    print(__doc__)
