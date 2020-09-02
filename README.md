# CarStore3000
Stand-alone code to deal with the data of a car dealer

# Setup
Add a secret key in .env
Generation example:
```python
import random, string
"".join([random.choice(string.printable) for _ in range(24)])
```

FLASK_APP=run.py flask init_db
python3 run.py

# Installation
pip3 install python-dotenv
pip3 install flask
pip3 install flask_sqlalchemy
pip3 install flask_wtf
pip3 install pandas

# TODO
- the csv comes from the car dealer, should be an API