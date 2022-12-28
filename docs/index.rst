PyPoject Starter
================

|Build Status| |license| |Documentation Status| |GitHub repo size|
|codecov|

.. raw:: html

   <!-- [![Release][rle-image]][rle-url] -->

.. raw:: html

   <!-- [![Sourcegraph][sg-image]][sg-url] -->

A template for the python project. It uses
`poetry <https://python-poetry.org/>`__ for dependency management and
`tox <https://github.com/tox-dev/tox>`__ for testing.



Features
--------

Some features in this template project:

-  Use `poetry <https://python-poetry.org/>`__ for dependency
   management.
-  Use tox、pytest、pytest-cov、coverage for testing.
-  Use black、isort for code formatting.
-  Use flake8 link for code linting.
-  Use mypy for static type checking.
-  Use `pre-commit <https://pre-commit.com/>`__ for code quality.
-  Use ipdb3 for debugging.
-  Multiple python versions support(Python 3.7+).
-  More features to be added 🚀 .

Project
-------

Contains the following projects under ``src`` as demo:

-  `hello <https://github.com/funnyzak/pyproject-starter/tree/main/src/hello>`__
   is a simple hello world project.
-  `pdf_parse <https://github.com/funnyzak/pyproject-starter/tree/main/src/pdf_parse>`__
   is a project that parse pdf.

Prerequisite
------------

-  `Python 3.7+ <https://www.python.org/>`__
-  `Poetry 1.2 <https://python-poetry.org/>`__
-  `pre-commit <https://pre-commit.com/>`__

Installation
------------

following the steps below to setup the project:

..  code-block:: php

   # Clone the repository
   git clone git@github.com:funnyzak/pyproject-starter.git && cd pyproject-starter

   # Install all dependencies
   poetry install --sync --all-extras --with dev,test,coverage

   # install git hook scripts for development
   pre-commit install

   # Other useful installation dependencies commands
   # Install dependencies with all extras
   poetry install --all-extras
   # Install dependencies with extras 'pdf' for pdf_parse project
   poetry install --extras "pdf"
   # Install dependencies with group 'dev'、'test' for development
   poetry install --with dev,test
   # Only install required dependencies for production
   poetry install


Usage
-----

There are some useful commands for development:

..  code-block:: bash

   # Run project => hello
   poetry run hello

   # Run project => pdf_parse: merge pdf
   poetry run merge_pdf_demo

   # Run project => pdf_parse: parse multi pdf to multi-layer pdf
   poetry run multi_layer_pdf_demo

   # Debug "hello" project with ipdb3
   poetry run ipdb3 ./src/hello/main.py

   # Code test
   poetry run pytest -s

   # Run default coverage test
   poetry run tox

   # Run hello project coverage test at python 3.9 and 3.10
   poetry run tox -e py{39,310}-hello

   # Lint with black
   poetry run black ./src --check

   # Format code with black
   poetry run black ./src

   # Check with mypy
   poetry run mypy ./src

   # Check import order with isort
   poetry run isort ./src --check

   # Lint with flake8
   poetry run flake8 ./src

Q&A
---

Development
~~~~~~~~~~~

Add new project
^^^^^^^^^^^^^^^

1. Create a new folder under ``src`` folder.
2. You can copy the ``hello`` project as a template.
3. Add folder name to ``packages`` in ``pyproject.toml`` file.
4. Code and test it.

Tip for project
^^^^^^^^^^^^^^^

-  You can create test cases for the new project in ``tests`` folder.
-  You can define script commands for the new project in
   ``pyproject.toml`` file. like ``poetry run hello`` command.
-  You can add new project to ``tox.ini`` file for coverage test.
-  You can add new project to ``mypy.ini`` file for static type
   checking.

Environment setup
~~~~~~~~~~~~~~~~~

install poetry
^^^^^^^^^^^^^^

See `poetry
installation <https://python-poetry.org/docs/#installation>`__.

install python3
^^^^^^^^^^^^^^^

See `python installation <https://www.python.org/downloads/>`__.

install pre-commit
^^^^^^^^^^^^^^^^^^

See `pre-commit installation <https://pre-commit.com/#install>`__.

References
----------

some useful references:

-  `poetry <https://python-poetry.org/>`__ is a dependency manager for
   Python that allows you to declare the libraries your project depends
   on and it will manage (install/update) them for you.
-  `PyPDF2 <https://pypdf2.readthedocs.io/en/latest/user/adding-pdf-annotations.html#free-text>`__
   is a library for working with PDF files.
-  `flake8 <https://flake8.pycqa.org/en/latest/>`__ is a wrapper around
   these tools: PyFlakes, pycodestyle, and Ned Batchelder’s McCabe
   script.
-  `isort <https://pycqa.github.io/isort/>`__ is a Python utility /
   library to sort imports alphabetically, and automatically separated
   into sections and by type.
-  `black <https://black.readthedocs.io/en/stable/>`__ is a Python code
   formatter.
-  `mypy <https://mypy.readthedocs.io/en/stable/config_file.html#per-module-and-global-options>`__
   is a static type checker for Python.
-  `pytest <https://docs.pytest.org/en/stable/>`__ is a testing
   framework for Python.
-  `pytest-cov <https://pytest-cov.readthedocs.io/en/latest/>`__ is a
   plugin for the pytest testing tool that measures coverage of Python
   code.
-  `coverage <https://coverage.readthedocs.io/en/coverage-5.5/>`__ is a
   tool for measuring code coverage of Python programs.
-  `ipdb <https://pypi.org/project/ipdb/>`__ is a IPython-enabled pdb.
-  `pre-commit <https://pre-commit.com/>`__ is a framework for managing
   and maintaining multi-language pre-commit hooks.
-  `tox <https://tox.readthedocs.io/en/latest/>`__ is a generic
   virtualenv management and test command line tool you can use for:

   -  checking your package installs correctly with different Python
      versions and interpreters
   -  running your tests in each of the environments, configuring your
      test tool of choice
   -  acting as a frontend to Continuous Integration servers, greatly
      reducing boilerplate and merging CI and shell-based testing.

Contribution
------------

If you have any questions or suggestions, please feel free to open an
issue or pull request.

|contribution|

License
-------

MIT License © 2022 `funnyzak <https://github.com/funnyzak>`__

.. |contribution| image:: https://contrib.rocks/image?repo=funnyzak/pyproject-starter
   :target: https://github.com/funnyzak/pyproject-starter/graphs/contributors
.. |Build Status| image:: https://github.com/funnyzak/pyproject-starter/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/funnyzak/pyproject-starter/actions
.. |license| image:: https://img.shields.io/github/license/funnyzak/pyproject-starter.svg?style=flat-square
   :target: https://github.com/funnyzak/pyproject-starter
.. |Documentation Status| image:: https://readthedocs.org/projects/pyproject-starter/badge/?version=latest&style=flat
   :target: https://pyproject-starter.readthedocs.io/en/latest/?badge=latest
.. |GitHub repo size| image:: https://img.shields.io/github/repo-size/funnyzak/pyproject-starter?style=flat-square&logo=github&logoColor=white&label=size
   :target: https://github.com/funnyzak/pyproject-starter
.. |codecov| image:: https://codecov.io/gh/funnyzak/pyproject-starter/branch/main/graph/badge.svg?token=K1AKZ65LY1
   :target: https://codecov.io/gh/funnyzak/pyproject-starter
