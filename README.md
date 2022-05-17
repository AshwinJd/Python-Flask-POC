## Setup

**1. Install dependencies**
> pip install -r requirements.txt

**2. Setup virtual env under folder venv**

**3. Run using python**
> python app.py


**Alternatively run using gunicorn**
> ./venv/bin/gunicorn -b 0.0.0.0:5000 app:application


**4. Run Mongo**
> docker-compose -f docker-compose-mongo.yml up -d



**Lint Check**
> pylint src common --rcfile=./lintrules.rc


**Run Test cases**
- Make sure mongo is running, since the test cases uses mongo
> python -m pytest