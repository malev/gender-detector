# Gender Detector

Gender detector is a Python library for guessing a person's gender by his/her first name. This library is based on [beauvoir](https://github.com/jeremybmerrill/beauvoir) with some performance improvements and support for two more countries.

**This is still in beta stages, use with precaution**

© 2014 Marcos Vanetta. Available under GPL2 License. See LICENSE.md.

# Datasets

* UK, from [OpenGenderTracking project](opengendertracking.github.com)
* US, from [OpenGenderTracking project](opengendertracking.github.com)
* AR, from [Names query site](http://www.buenosaires.gob.ar/areas/registrocivil/nombres/busqueda/buscador_nombres.php?menu_id=16082) from the goverment of the City of Buenos Aires. **I understand this data is not enough so be careful with the results**.
* UR, from [Civil registry](https://catalogodatos.gub.uy/dataset/partidas-de-registro-civil-de-montevideo) in Montevideo. Same as in AR, **Use with precaution!**

# How to use it

Nothing too fancy, just install:

    pip install gender-detector

And then:

```python
from gender_detector import GenderDetector
detector = GenderDetector('us') # Can be us, uk, ur, ar
detector.guess('Marcos') # => 'male'
```

# TODO:

* Add information about statistics
* Better datasets
