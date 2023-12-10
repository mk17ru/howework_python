
python setup.py sdist bdist_wheel
anaconda upload dist/*
pip install -i https://pypi.anaconda.org/mk17ru/simple table-generator
