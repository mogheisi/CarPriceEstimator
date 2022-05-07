# Car Price Estimator

This Django project uses car data to estimate the price of the car you want by using machine learning, using the data of the vehicles extracted from the Divar site.

# How to run

To run project in development mode; Just use steps below:

1. Install python2, pip, virtualenv in your system.
2. Clone the project https://github.com/Shntia/CarPriceEstimator.git
3. Make development environment ready using commands below;
```sh
   git clone https://github.com/Shntia/CarPriceEstimator.git && cd CarPriceEstimator
  python3 -m venv env  # Create virtualenv named env
  source build/bin/activate
  pip install -r requirements.txt
  python manage.py migrate  # Create database tables
   ```
4. Run project using python manage.py runserver
5. Go to http://localhost:8000 to see project.
