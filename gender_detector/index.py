from collections import OrderedDict
from country import Country


class Index:
    """
    Generate index based on the position in bytes
    of every letter in the alphabet.
    The index is stored in an OrderedDict.
    It's a lazy index, the index is not generated
    till the first call.
    """
    def __init__(self, country='us'):
        self.indices = []
        self.country = Country(country)

    def __call__(self, letter):
        if len(self.indices) == 0:
            self._generate_index()
        return self.indices[letter.upper()]

    def _generate_index(self):
        self.indices = OrderedDict()
        with open(self.country.file()) as file:
            total = file.readline() # Omit headers line
            for line in file:
                if line[0] not in self.indices:
                    self.indices[line[0]] = len(total)
                total = total + line


if __name__ == "__main__":
    print __doc__