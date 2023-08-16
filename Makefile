# SHELL := /bin/zsh
.ONE_SHELL:
# SHELL := /bin/zsh
BACKEND_HOME := $(PWD)/backend
# rm -rf backend/.venv

env: backend/requirements.txt
	@eval "$$(pyenv init -)" && pyenv shell 3.10.4
	python -m venv backend/.venv
	source backend/.venv/bin/activate && pip install --upgrade pip
	pip install -r backend/requirements.txt

venv: backend/.venv
	. ./backend/.venv/bin/activate