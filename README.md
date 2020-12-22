# Medical Record Management System

Website designed in Django for fast access of Medical Reports. 

## **Services**:

* 2 User Implementation
    * Doctor
    * Patient
* Storing all the reports and prescriptions of the Users(Patients)
* Filtering their reports and prescriptions by Date or Hospital name etc..
* Giving Tablet Notifications for Users(Patients)
* Forum for patients where Doctor only can answer questions asked by patients

## **Uses**:

* Easy for doctor to access all the previous history of patient
* Useful for old patients who generally forget their medicine
* Patients can check whether their health is improving or not by checking previous reports
* Forums are helpful for patients who are seeking for second advise for Operations etc..

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django.

```bash
pip install django
```

## Usage

Go to Folder containing Project and Type these commands in Command Prompt

```bash
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
