=====================
internet-speedtest-pi
=====================

.. container::

    .. image:: https://img.shields.io/pypi/v/internet_speedtest_pi.svg
            :target: https://pypi.python.org/pypi/internet_speedtest_pi
            :alt: PyPI Version

    .. image:: https://img.shields.io/pypi/pyversions/internet_speedtest_pi.svg
            :target: https://pypi.python.org/pypi/internet_speedtest_pi/
            :alt: PyPI Python Versions

    .. image:: https://img.shields.io/pypi/status/internet_speedtest_pi.svg
            :target: https://pypi.python.org/pypi/internet_speedtest_pi/
            :alt: PyPI Status

    .. badges from below are commendted out

    .. .. image:: https://img.shields.io/pypi/dm/internet_speedtest_pi.svg
            :target: https://pypi.python.org/pypi/internet_speedtest_pi/
            :alt: PyPI Monthly Donwloads

.. container::

    .. image:: https://img.shields.io/github/workflow/status/khelfen/internet-speedtest-pi/CI/master
            :target: https://github.com/khelfen/internet-speedtest-pi/actions/workflows/ci.yml
            :alt: CI Build Status
    .. .. image:: https://github.com/khelfen/internet-speedtest-pi/actions/workflows/ci.yml/badge.svg?branch=master

    .. image:: https://img.shields.io/github/workflow/status/khelfen/internet-speedtest-pi/Documentation/master?label=docs
            :target: https://khelfen.github.io/internet-speedtest-pi/
            :alt: Documentation Build Status
    .. .. image:: https://github.com/khelfen/internet-speedtest-pi/actions/workflows/documentation.yml/badge.svg?branch=master

    .. image:: https://img.shields.io/codecov/c/github/khelfen/internet-speedtest-pi.svg
            :target: https://codecov.io/gh/khelfen/internet-speedtest-pi
            :alt: Codecov Coverage
    .. .. image:: https://codecov.io/gh/khelfen/internet-speedtest-pi/branch/master/graph/badge.svg

    .. image:: https://img.shields.io/requires/github/khelfen/internet-speedtest-pi/master.svg
            :target: https://requires.io/github/khelfen/internet-speedtest-pi/requirements/?branch=master
            :alt: Requires.io Requirements Status
    .. .. image:: https://requires.io/github/khelfen/internet-speedtest-pi/requirements.svg?branch=master

    .. badges from below are commendted out

    .. .. image:: https://img.shields.io/travis/khelfen/internet-speedtest-pi.svg
            :target: https://travis-ci.com/khelfen/internet-speedtest-pi
            :alt: Travis CI Build Status
    .. .. image:: https://travis-ci.com/khelfen/internet-speedtest-pi.svg?branch=master

    .. .. image:: https://img.shields.io/readthedocs/internet-speedtest-pi/latest.svg
            :target: https://internet-speedtest-pi.readthedocs.io/en/latest/?badge=latest
            :alt: ReadTheDocs Documentation Build Status
    .. .. image:: https://readthedocs.org/projects/internet-speedtest-pi/badge/?version=latest

    .. .. image:: https://pyup.io/repos/github/khelfen/internet-speedtest-pi/shield.svg
            :target: https://pyup.io/repos/github/khelfen/internet-speedtest-pi/
            :alt: PyUp Updates

.. container::

    .. image:: https://img.shields.io/pypi/l/internet_speedtest_pi.svg
            :target: https://github.com/khelfen/internet-speedtest-pi/blob/master/LICENSE
            :alt: PyPI License

    .. image:: https://app.fossa.com/api/projects/git%2Bgithub.com%2Fkhelfen%2Finternet-speedtest-pi.svg?type=shield
            :target: https://app.fossa.com/projects/git%2Bgithub.com%2Fkhelfen%2Finternet-speedtest-pi?ref=badge_shield
            :alt: FOSSA Status

.. container::

    .. image:: https://badges.gitter.im/khelfen/internet-speedtest-pi.svg
            :target: https://gitter.im/internet-speedtest-pi/community
            :alt: Gitter Chat
    .. .. image:: https://img.shields.io/gitter/room/khelfen/internet-speedtest-pi.svg

    .. image:: https://img.shields.io/badge/code%20style-black-000000.svg
            :target: https://github.com/psf/black
            :alt: Code Style: Black

Python package to measure the current internet speed and write it to a log file.

* Free software: `MIT License`_
* Documentation: https://internet-speedtest-pi.readthedocs.io.

.. _`MIT License`: https://github.com/khelfen/internet-speedtest-pi/blob/master/LICENSE

Features
--------

* TODO

Install
-------

Use ``pip`` for install:

.. code-block:: console

    $ pip install internet_speedtest_pi

If you want to setup a development environment, use ``poetry`` instead:

.. code-block:: console

    $ # Install poetry using pipx
    $ python -m pip install pipx
    $ python -m pipx ensurepath
    $ pipx install poetry

    $ # Clone repository
    $ git clone https://github.com/khelfen/internet-speedtest-pi.git
    $ cd internet-speedtest-pi/

    $ # Install dependencies and hooks
    $ poetry install
    $ poetry run pre-commit install

Credits
-------

This package was created with Cookiecutter_ and the `elbakramer/cookiecutter-poetry`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`elbakramer/cookiecutter-poetry`: https://github.com/elbakramer/cookiecutter-poetry
