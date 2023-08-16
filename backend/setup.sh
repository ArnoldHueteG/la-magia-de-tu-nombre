BACKEND_HOME=$(pwd)/backend
pyenv shell 3.10.4
python -m venv $BACKEND_HOME/.venv
source $BACKEND_HOME/.venv/bin/activate && pip install --upgrade pip
pip install -r $BACKEND_HOME/requirements.txt


source $BACKEND_HOME/.venv/bin/activate
pip install -r $BACKEND_HOME/requirements.txt
