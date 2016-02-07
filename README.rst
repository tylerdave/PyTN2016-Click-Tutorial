===============================
PyTennessee 2016 - Writing Command Line Applications that Click
===============================

.. image:: https://travis-ci.org/tylerdave/PyTN2016-Click-Tutorial.svg?branch=master
    :target: https://travis-ci.org/tylerdave/PyTN2016-Click-Tutorial

Tutorial for writing command line applications using click.

-----
About
-----

Abstract: https://www.pytennessee.org/schedule/presentation/117/ 
Repo: https://github.com/tylerdave/PyTN2016-Click-Tutorial
Slides: https://speakerdeck.com/tylerdave/pytennessee-2016-writing-command-line-applications-that-click
Follow-up: COMING SOON

-------------------
Installation: TL;DR
-------------------

Know all about installing and developing Python packages and don't feel like reading the rest?:

* Have Git and Python installed
* Create and activate a virtualenv
* Clone this repo (or your own fork of it) and ``cd`` to it.
* Install the package in editable mode: ``pip install -e .``

-----------------------------------
Installation: Detailed Instructions
-----------------------------------

Prerequisites
-------------

In order to make use of this tutorial you will a system with the following installed:

* Git
* Python (2.7, 3.3, 3.4, 3.5)

If you do not already have these installed, follow these directions:

* `Installing Git`_
* `Installing Python`_

.. _`Installing Git`: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
.. _`Installing Python`: http://docs.python-guide.org/en/latest/starting/installation/

Virtualenv
----------

The virtualenv package allows you to create isolated environments for
developing Python code.

* To make sure it is installed, run this command:

  .. code-block:: console
  
    pip install virtualenv

  *or on Windows (if the above doesn't work):*

  .. code-block:: console

    python -m pip install virtualenv

  This will either install the package or let you know it's already installed. If it is already installed, you will see:

  .. code-block:: console
    
    Requirement already satisfied (use --upgrade to upgrade)

* Create a virtualenv for this tutorial:

  .. code-block:: console
  
    virtualenv click_tutorial

* Activate the virtualenv:

  .. code-block:: console
  
    source click_tutorial/bin/activate

  *or on Windows:*

  .. code-block:: console

    click_tutorial\Scripts\activate
  
Get The Tutorial
----------------

* (Optional) Fork this repo on GitHub
* Clone the repo locally (using either this repo's URL or that of your new fork.)

  .. code-block:: console
  
    git clone https://github.com/tylerdave/PyTN2016-Click-Tutorial.git pytn

Install The Tutorial
--------------------

The tutorial repo is configured to be a Python package in order to ease
installation.

* In a terminal/console ``cd`` to cloned tutorial directory: ``cd pytn``
* Install the package in editable mode:

  .. code-block:: console
  
    pip install -e .

* Run tests to verify installation:

  .. code-block:: console
  
    py.test -v tests/

* Verify that all tests report PASSED

Run The Tutorial
----------------

Once installed, the ``tutorial`` command should be available.

* See usage information

  .. code-block:: console

    tutorial --help
