from math import sqrt


DEFAULT_PROPORTION_THRESHOLD = 0.99
DEFAULT_LOWER_CONFIDENCE_BOUND = 0.75
MAGIC_STATISTICS_NUMBER = 1.96


class Binomy:
    def __init__(self, male_count, female_count):
        threshold = DEFAULT_PROPORTION_THRESHOLD
        lower_confidence_bound = DEFAULT_LOWER_CONFIDENCE_BOUND
        z = MAGIC_STATISTICS_NUMBER

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

        self.confidence = raw_male_proportion > threshold or raw_female_proportion > threshold and lower > lower_confidence_bound

    def enough_confidence(self):
        return self.confidence

if __name__ == "__main__":
    print __doc__