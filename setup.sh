pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py load_discount discount_codes.csv --d
./manage.py load_serialnumber serial_numbers.csv --d
./manage.py runserver