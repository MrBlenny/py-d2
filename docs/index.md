# d2-py

A fully typed python interface for building .d2 graph files for use with the D2 engine.

## Installation

```bash
pip install d2-py
```

## Usage

```python
from d2_py import D2Graph, D2Node, D2Link, D2Style

nodes = [
    D2Node(name="node_name1", style=D2Style(fill="red")),
    D2Node(name="node_name2", style=D2Style(fill="blue"))]
links = [
    D2Link(from_node="node_name1", to_node="node_name2")
]

diagram = D2Diagram(nodes=nodes, links=links)

with open("graph.d2", "w") as f:
    f.write(str(diagram))

```

produces the following graph.d2 file:

```d2

node_name1: {
  style: {
    fill: red
  }
}
node_name2: {
  style: {
    fill: blue
  }
}
node_name1 -> node_name2

```

This can be rendered using `d2 render graph.d2` or [https://play.d2lang.com/](https://play.d2lang.com/) to produce

![example graph](./docs/images/d2.svg)


## Development
### Prerequisite

- [Python 3.7+](https://www.python.org/)
- [Poetry 1.2](https://python-poetry.org/)
- [pre-commit](https://pre-commit.com/)

### Installation

following the steps below to setup the project:

```bash

```bash
# Clone the repository
git clone git@github.com:funnyzak/pyproject-starter.git && cd pyproject-starter

# Install all dependencies
poetry install --sync --all-extras --with dev,test,coverage

# install git hook scripts for development
pre-commit install

# Install dependencies with group 'dev'、'test' for development
poetry install --with dev,test
# Only install required dependencies for production
poetry install
```

### Usage

There are some useful commands for development:

```bash

# Debug "hello" project with ipdb3
poetry run ipdb3 ./src/py_d2/main.py

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
```
