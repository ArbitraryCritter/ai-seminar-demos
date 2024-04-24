# Prepare Python3 environment

These examples use Python3 and various AI tooling, mainly transformers and PyTorch.
You will need a Python environment to execute them.

You should be sure to use a supported Python version, meaning Python 3.8 or newer.

## OSX

You should use homebrew or similar (perhaps MacPorts) to install Python3. Please see general instructions here:
https://brew.sh/
OR
https://www.macports.org/install.php

To install Python:
```
brew install python@3.10
```
OR
```
sudo port install python310
```

Finally you should install the "pipenv" package manager, as a user-wide dependency.
```
pip install pipenv --user
```

## Windows

On Windows, you should use miniconda. Get the Windows binary here and install it:
https://docs.anaconda.com/free/miniconda/miniconda-install/

Run a shell environment and install dependencies:
```
conda create --name nlp-seminar --yes
pip install --upgrade transformers accelerate faster_whisper
```

Whenever you open a new shell, you should run this, to activate the shell:
```
conda activate nlp-seminar
```
