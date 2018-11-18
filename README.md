# NumEconUtils 

This python package provides a CLI used for the course _Introduction to programming and numerical analysis_ by the staff.

## Installation

The package can be installed by:

```bash
pip install git+https://www.github.com/numeconcopenhagen/numeconutils
```

## Features

At the current state the features is very basic and has not been fully tested yet.

### Remove cell content based on regex

```bash
NumEconUtils clearcells Notebook.ipynb
```

will copy the notebook and save the file as `Notebook_fillin.ipynb`, and clear all code cells where the first line begins with #fillin. Make sure that the file doesn't exist before running the command. 