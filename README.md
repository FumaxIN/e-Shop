# e-Shop

A mini online shop management backend to create, delete, update and filter through the products.


### Features


## Requirements

* [Python](https://www.python.org/downloads/) 3.8 or above
* [pip](https://pip.pypa.io/en/stable/installing/) 20.1 or above
* [Django](https://pypi.org/project/Django/)
* [Django-Rest-Framework](https://pypi.org/project/djangorestframework/k)


## Running

After succefully installing the above dependencies, simply start the server:

```shell
python manage.py runserver
```

## Endpoints

`https://127.0.0.1:8000/items` to see the list of prducts. Add a new product through JSON format without mentioning the id.

`https://127.0.0.1:8000/search/<keyword>` to search throught the database.

`https://127.0.0.1:8000/items/<int>` to go to a speciic product. This endpoint allows you to Delete or Patch the object.

The above operations can be performed through admin panel as well ater registering yoursel as superuser.

