=====================
internet-speedtest-pi
=====================

Python package to measure the current internet speed and write it to a log file.

* Free software: `MIT License`_

.. _`MIT License`: https://github.com/khelfen/internet-speedtest-pi/blob/master/LICENSE

Features
--------

* TODO

Install
-------

Use ``poetry`` for install:

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

Basic Usage
-----------

Running a speed test once is as simple as running:

.. code-block:: console

    $ poetry run python run_speedtest.py

The results will be saved in a newly created ``results`` directory. Running the script
again will append the results to the existing CSV file.

You can use ``crontab`` or other tools to schedule to run the speed test as often as you
like. The bash `run_internet_speedtest_pi.sh`_ script provided with this repo is a basic
template on how you can setup a run. Just fill out the marked variables with your local
variables. After that you can add a crontab by running the following:

.. code-block:: console

    $ crontab -e

This will create a new cron file if you have not setup one before. To run the script
every minute add the following line with your local variables into the cron file.

.. code-block:: console

    * * * * * /<path>/<to>/bash /home/<user>/<path>/<to>/run_internet_speedtest_pi.sh

.. _`run_internet_speedtest_pi.sh`: https://github.com/khelfen/internet-speedtest-pi/blob/main/run_internet_speedtest_pi.sh

After saving and closing the file start ``crontab`` by running the following:

.. code-block:: console

    $ service cron start

After starting ``crontab``

Credits
-------

This package was created with Cookiecutter_ and the `elbakramer/cookiecutter-poetry`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`elbakramer/cookiecutter-poetry`: https://github.com/elbakramer/cookiecutter-poetry
