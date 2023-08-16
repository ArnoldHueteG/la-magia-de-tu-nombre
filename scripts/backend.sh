

setup_backend() {
    pyenv shell 3.10.4
	python -m venv backend/.venv
	source backend/.venv/bin/activate && pip install --upgrade pip
	pip install -r backend/requirements.txt
}

activate_backend(){
    source backend/.venv/bin/activate
}