========
Tarakimu
========


.. image:: https://img.shields.io/pypi/v/tarakimu.svg
        :target: https://pypi.python.org/pypi/tarakimu

.. image:: https://img.shields.io/travis/tehamalab/tarakimu.svg
        :target: https://travis-ci.org/tehamalab/tarakimu

.. image:: https://readthedocs.org/projects/tarakimu/badge/?version=latest
        :target: https://tarakimu.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/tehamalab/tarakimu/shield.svg
     :target: https://pyup.io/repos/github/tehamalab/tarakimu/
     :alt: Updates



A python library for number to Swahili words conversion


* Free software: BSD license
* Documentation: https://tarakimu.readthedocs.io.


Installation
-------------

To install tarakimu library you can use pip:

.. code-block:: console

    $ pip install tarakimu


Basic Usage
-----------

*Examples*

Using Python

.. code-block:: python

    from tarakimu import num_to_words

    num_to_words('88')  # returns 'themanini na nane'
    
    num_to_words(88.88)  # returns 'themanini na nane nukta nane nane'
    
    num_to_words('-88000000')  # returns 'hasi kuadrilioni themanini na nane'


Using command line interface

.. code-block:: console

    $ tarakimu numtowords 88  -l sw  # writes to the standard output 'themanini na nane'
