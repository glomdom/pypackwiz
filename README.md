# pypackwiz
A python script for [packwiz](https://packwiz.infra.link/) which simplifies project creation and automates instance creation. Has a few nifty stuff in it aswell.

## Installation
```console
$ pip install -i https://test.pypi.org/simple/ pypackwiz # will migrate to production pypi after main roadmap has been completed.
```

## Usage
```console
$ pypackwiz --help
Usage: pypackwiz [OPTIONS] COMMAND [ARGS]...

  A python wrapper for packwiz.

Options:
  --help  Show this message and exit.

Commands:
  init  Initializes a packwiz project.
```

## Roadmap

- [ ] create packwiz pack files using `packwiz init`
- [ ] proper modloader version checker
- [ ] copying of development files from instance to work directory
- [ ] multimc instance.cfg file generator, including pre- and post- launch commands