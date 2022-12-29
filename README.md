# py-d2

![Banner](docs/images/banner.png)

An unofficial, fully typed python interface for building .d2 graph files in python.

## Installation

```bash
pip install py-d2
```

## Usage

```python
from py_d2 import D2Graph, D2Node, D2Connection, D2Style

nodes = [
    D2Node(name="node_name1", style=D2Style(fill="red")),
    D2Node(name="node_name2", style=D2Style(fill="blue"))]
links = [
    D2Connection(from_node="node_name1", to_node="node_name2")
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

![example graph](/docs/images/d2.svg)

See the [tests](/tests/test_py_d2) for more detailed usage examples.


## Supported Features

- [x] Shapes (nodes)
- [x] Connections (links)
- [x] Styles
- [x] Containers (nodes/links in nodes)
- [x] Shapes in shapes
- [x] Arrow directions
- [x] Markdown / block strings / code in shapes
- [ ] Icons in shapes
- [ ] SQL table shapes
- [ ] Class shapes
- [ ] Comments


## Development
### Prerequisite

- [Python 3.7+](https://www.python.org/)
- [Poetry 1.3](https://python-poetry.org/)
- [pre-commit](https://pre-commit.com/)

### Installation

following the steps below to setup the project:

```bash

```bash
# Clone the repository
git clone git@github.com:MrBlenny/py-d2.git && cd py-d2

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
# Run the example
poetry run example

# Debug with ipdb3
poetry run ipdb3 ./src/py_d2/main.py

# Code test
poetry run pytest -s

# Run default coverage test
poetry run tox

# Run example project coverage test at python 3.9 and 3.10
poetry run tox -e py{39,310}-py-d2

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
