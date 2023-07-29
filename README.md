Overview
========
SDX API

Kytos Napp to handle the requirements of the AtlanticWave-SDX project.

Requirements
============

* kytos/core
* kytos/topology
* kytos/storehouse
* openAPI Specification
* swagger client
* flask
* python 3.9

Preparing the environment:
==========================

``Installing Python``

Please make sure that you're using python3.9


Installing swagger_client
==========================

For the whole installation process and requirements, please access
the AtlanticWave SDX repo in Github: https://github.com/atlanticwave-sdx


# Test

// Install python dependecies requirements

# Asynchronous Lint Engine

// ALE (Asynchronous Lint Engine) is a plugin providing linting (syntax checking and semantic errors)

// Installation in VIM with Vundle

cd ~/.vim/bundle

Set up Vundle:

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

git clone https://github.com/dense-analysis/ale.git

// Edit ~/.vimrc

set rtp+=~/.vim/bundle/Vundle.vim

let path='~/.vim/bundle/Vundle.vim'

call vundle#begin()

Plugin 'VundleVim/Vundle.vim'

Plugin 'dense-analysis/ale'

call vundle#end()            " required

filetype plugin indent on    " required

let g:ale_linters = {
        \   'python': ['flake8', 'pylint', 'pycodestyle'],
        \}


// Then run the command :PlugInstall in Vim.

:source ~/.vimrc
:PluginInstall

# Black

black --check --diff main.py

black main.py
black --line-length 80 main.py

# Isort

isort main.py

# Bandit

bandit --configfile bandit.yaml

// with the following bandit.yaml in the project's root directory

assert_used:
  skips: ['*_test.py', 'test_*.py']


# How to update dependencies versions

// Edit requirements.in/dev.txt if needed.

// Run pip-compile again, exactly as before:

$ <venv>/bin/pip-compile dev.in

# Pytest

python3 -m pytest --cov=app --cov-report=html

# Partial test

pytest -v -k "test_sdx_topology"

# Unit test

pytest tests/unit/test_main.py

pytest --cov app --cov-branch --cov-report term-missing
