Gender Detector
===============

Gender detector is a Python library for guessing a person's gender by his/her first name. This library is based on [beauvoir](https://github.com/jeremybmerrill/beauvoir) with support for United States, United Kingdom,  Argentina and Uruguay.

**This is still in beta stages, use with precaution**

© 2014 Marcos Vanetta. Available under GPL2 License. See LICENSE.

Datasets
========

* UK, from `OpenGenderTracking project <http://opengendertracking.github.com>`_
* US, from `OpenGenderTracking project <http://opengendertracking.github.com>`_
* AR, from `Names query site <http://www.buenosaires.gob.ar/areas/registrocivil/nombres/busqueda/buscador_nombres.php?menu_id=16082>`_ from the goverment of the City of Buenos Aires. **this is a small sample, use with precaution!**.
* UY, from `Civil registry <https://catalogodatos.gub.uy/dataset/partidas-de-registro-civil-de-montevideo>`_) in Montevideo. Same as in AR, **Use with precaution!**

How to use it
=============

Nothing too fancy, just install:

.. code-block:: bash

    pip install gender-detector

And then:

.. code-block:: python

    from gender_detector import GenderDetector
    detector = GenderDetector('us') # It can also be ar, uk, uy.
    detector.guess('Marcos') # => 'male'


TODO:
=====

* Add information about statistics
* Better datasets
