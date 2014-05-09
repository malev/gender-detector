import os


class Country:
    '''
    Handles the data files per country

    Arguments:
    arg1 -- country code
    '''
    def __init__(self, country='us'):
        self.country = country
        if not os.path.isfile(self.file()):
            raise RuntimeError("There is no data file for that coutry")

    def file(self):
        return self.base_directory() + 'data/%sprocessed.csv' % (self.country)

    def base_directory(self):
      return os.path.dirname(os.path.realpath(__file__)) + os.path.sep


if __name__ == "__main__":
    print __doc__
