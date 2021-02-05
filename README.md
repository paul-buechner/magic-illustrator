# Magic Illustrator

[![license](https://img.shields.io/pypi/l/ansicolortags.svg)]()
[![GitHub issues](https://img.shields.io/github/issues/paul-buechner/magic-illustrator)]()
[![GitHub pull requests](https://img.shields.io/github/issues-pr/paul-buechner/magic-illustrator)]()

Magic illustrator is a python script using image processing to draw a chosen image via mouse control.

It is also possible to fill the eintire drawing layer.

<div align="center" style="padding:5px;" width="100%">
<img src="https://media.giphy.com/media/2ReSk1TZwY6Ojr337Z/giphy.gif" style="margin: 10px;" width="400" height="300"/>
<img src="https://media.giphy.com/media/5akHWqeXszylTV0Vx5/giphy.gif" style="margin: 10px;" width="400" height="300"/>
</div>

# Installation

Magic Illustrator runs on Python 3.9 or higher version. Read more about the setup [here](#Directly).

## Directly

If you want to hack on yourself, clone this repository and in that directory execute:

```bash
# Install python requirements
pip install -r requirements.txt
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

## Anaconda

If you are using Anaconda Environment execute the following steps:

- Create a conda environment using `conda env create -f environment.yml`
- Activate the created environment `conda activate magic-illustrator`

# Usage

After installing the required packages run the illustrator:

```bash
python main.py
```

The image which is drawn can be configured in `src/illustrator_config.py` in the `path` variable. There are also options regarding `image_dimensions` and `KeyCode` Selections which maybe need to take into consideration.

As mentioned before, to fire certain actions requires to hit certain keys on the keyboard. By default following is set:

- `'d'` draw selected image
- `'c'` fill the eintire drawing layer
- `'e'` exit everything and close thread

Hitting `'d'` or `'c'` while the programm is drawing will stop and reset the process without killing the thread.

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# License

This project falls under the [MIT](https://choosealicense.com/licenses/mit/) license.
