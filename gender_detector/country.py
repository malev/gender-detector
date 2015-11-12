import os
from .binomy import Binomy


class Country:
    '''
    Handles the data files per country

    Arguments:
    arg1 -- country code
    '''
    def __init__(self, country):
        self.country = country
        self._validate_country()

    def guess(self, name_info):
        name = name_info['name']
        opt = {
            'gender': name_info['gender'],
            'male_count': name_info['male_count'],
            'female_count': name_info['female_count']
        }
        return self._guesser_method()(name, opt)

    def _guesser_method(self):
        # { country : method }
        return {
            'ar': self.no_method,
            'uk': self.binomy,
            'uy': self.no_method,
            'us': self.binomy
        }[self.country]

    def no_method(self, name, opt={}):
        return opt['gender']

    def binomy(self, name, opt={}):
        male_count = int(opt['male_count'])
        female_count = int(opt['female_count'])
        gender = opt['gender']
        bin = Binomy(male_count, female_count)

        if bin.enough_confidence():
            if male_count > female_count:
                return 'male'
            elif female_count > male_count:
                return 'female'
            else:
                return 'unknown'

    def _validate_country(self):
        if not os.path.isfile(self.file()):
            raise RuntimeError("There is no data file for that coutry")

    def file(self):
        return self._base_directory() + 'data/%sprocessed.csv' % (self.country)

    def _base_directory(self):
      return os.path.dirname(os.path.realpath(__file__)) + os.path.sep


if __name__ == "__main__":
    print(__doc__)
