# Project Name

A Python module to create a Shell session.

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)

## Installation

- clone the repository
- run 
  ```shell
  python setup.py build &&
  python setup.py test &&
  python setup.py install
  ```

## Usage

```python
import interactive_session as m
session = m.InteractiveSession("bash", "exit")
print(session.execute("echo hello"))
session.close()

```

## License

This project is licensed under the MIT License.
