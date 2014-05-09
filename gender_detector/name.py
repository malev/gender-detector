from math import sqrt


DEFAULT_PROPORTION_THRESHOLD = 0.99
DEFAULT_LOWER_CONFIDENCE_BOUND = 0.75
MAGIC_STATISTICS_NUMBER = 1.96


class Name:
    def __init__(self, name, gender='unknown', male_count=0, female_count=0,
            unknown_value='unknown'):
        self.name = name
        self.gender = gender
        self.male_count = male_count
        self.female_count = female_count
        self.total = float(self.male_count + self.female_count)
        self.unknown_value = unknown_value

    def guess(self):
        if self._enough_confidence():
            return self._guess_gender()
        else:
            return self.unknown_value

    def _guess_gender(self):
        if self.male_count > self.female_count:
            return 'male'
        elif self.female_count > self.male_count:
            return 'female'
        else:
            return self.unknown_value

    def _enough_confidence(self):
        threshold = DEFAULT_PROPORTION_THRESHOLD
        lower_confidence_bound = DEFAULT_LOWER_CONFIDENCE_BOUND
        z = MAGIC_STATISTICS_NUMBER

        male_count = self.male_count
        female_count = self.female_count
        total = float(male_count + female_count)

        if total == 0.0:
            raw_male_proportion = 0
            raw_female_proportion = 0
        else:
            raw_male_proportion = male_count / total
            raw_female_proportion = female_count / total

        nt = total + z ** 2
        observed = max([male_count, female_count])
        estimated_value = (observed + ((z ** 2) / 2)) / nt
        interval = z * sqrt(estimated_value * (1 - estimated_value) / nt)
        lower = max([raw_female_proportion, raw_male_proportion]) - interval

        return raw_male_proportion > threshold or raw_female_proportion > threshold and lower > lower_confidence_bound
