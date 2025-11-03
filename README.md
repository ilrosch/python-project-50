# Gendiff (generating file difference)

[![Actions Status](https://github.com/ilrosch/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ilrosch/python-project-50/actions) [![gendiff](https://github.com/ilrosch/python-project-50/actions/workflows/gendiff.yml/badge.svg)](https://github.com/ilrosch/python-project-50/actions/workflows/gendiff.yml) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ilrosch_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=ilrosch_python-project-50) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=ilrosch_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=ilrosch_python-project-50)

Program that determines the difference between two data structures

- Support for various input formats: YAML, JSON
- Report generation in plain text, stylish, and JSON formats

Requirements:
- python >= 3.12
- uv >= 0.8 

Help for use:

```
gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

---

## Example

- Compare two files and output using **stylish format**:
```
gendiff <file_path1> <file_path2> --format=stylish
```
[![asciicast](https://asciinema.org/a/RrtWs6D9A0xzj2Lanc74oJtr3.svg)](https://asciinema.org/a/RrtWs6D9A0xzj2Lanc74oJtr3)

- Compare two files and output using **plain format**:
```
gendiff <file_path1> <file_path2> --format=plain
```
[![asciicast](https://asciinema.org/a/ZLuGdj9ckfhJO5S7gjQH0Xxgc.svg)](https://asciinema.org/a/ZLuGdj9ckfhJO5S7gjQH0Xxgc)

- Compare two files and output using **json format**:
```
gendiff <file_path1> <file_path2> --format=json
```
[![asciicast](https://asciinema.org/a/fXwgXs2H9i4fTHdf7xhjv3UTC.svg)](https://asciinema.org/a/fXwgXs2H9i4fTHdf7xhjv3UTC)

---

## Tech stack
- **Language:** python
- **Packages:**
    - [ruff](https://docs.astral.sh/ruff/)
    - [pytest](https://docs.pytest.org/en/stable/)
    - [uv](https://docs.astral.sh/uv/)

---

## Get started

- Clone repository:

```
git clone git@github.com:ilrosch/python-project-50.git
```

- Install dependencies:
```
make install
```

- Run linter:
```
make lint
```

- Run tests:
```
make test
```