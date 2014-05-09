# Gender Detector

Library for guessing a person's gender by their first name. This library is based on [beauvoir](https://github.com/jeremybmerrill/beauvoir).

# How to use it

Nothing too fancy, just install and:

    from gender_detector import GenderDetector
    detector = GenderDetector('us')
    detector.guess('Marcos') # => 'male'

# Testing

    nosetest

# TODO:

* work
* valid languages
* improve file's path
* add statistics info
