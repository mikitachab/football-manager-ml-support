#!/bin/bash
python3 -m virtualenv venv
source venv/bin/acticate
pip install numpy pandas matplotlib seaborn sklearn imblearn jupyter

# customize jupyter

pip install jupyterthemes
pip install --upgrade jupyterthemes
pip install jupyter_contrib_nbextensions

jt -t onedork -fs 95 -altp -tfs 11 -nfs 115 -cellw 88% -T
jupyter contrib nbextension install --system
