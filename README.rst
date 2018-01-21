Welcome to Pythonic Interviews
==============================

A repository collecting in one place everything I think can be useful to keep one's Pythonic zen even in the toughest job interviews, and more importantly to become a better Python Developer.


Features
--------

The idea is to cover:

* Definitions of fondamental concepts of Object Oriented programming and Python
* Best coding practices and examples
* Description of important packages
* Common structures and algorithms
* Common coding interview questions


Philosophy
----------

It is originally intended to be notes for myself but I release it in the hope it will be helpful for others. I will try my best to update it regularly and stick to the best practices.


Testing
-------

The code is tested with pytest. To run them:
::

    cd path-to-repository/src/
    pytest

To get more info about coverage and such::

    pytest --cov-report term-missing --cov=. --verbose

Continuous Integration testing is done by Travis

.. image:: https://travis-ci.org/arnaudblois/pythonic_interviews.svg?branch=master
    :alt: build-status


Contributing
---------------

Any help is always appreciated and if you have any suggestions or improvement, do not hesitate to create a ticket/pull request.
Thank you very much for your interest in Pythonic Interviews.


License
-------

* Definition, tutorials and documentation licensed under `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/legalcode>`_.
* Code source distributed under MIT license
