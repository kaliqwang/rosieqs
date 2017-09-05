# rosieqs
CS 3300 - Project Rosie - Query Server 1 (created using Django and Django REST Framework)

## Local Server

Run the following commands in the project root directory:

```
python manage.py makemigrations api
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Production Server

Hosted at: [kaliqwang.pythonanywhere.com](#)

Admin site: [kaliqwang.pythonanywhere.com/admin/](#)

The admin site provides a UI for managing database objects. The user and pass are both "admin".

### Browsable API endpoints
* [kaliqwang.pythonanywhere.com/api/items](#)
* [kaliqwang.pythonanywhere.com/api/items/{{item_id}}](#)
* [kaliqwang.pythonanywhere.com/api/events](#)
* [kaliqwang.pythonanywhere.com/api/events/{{event_id}}](#)

Standard REST operations are supported (e.g. GET, POST, PUT, and DELETE).

### Usage and JSON examples

Creating (POST) or updating (PUT) an item:

```javascript
{
    "name": "string",
    "initial_quantity": int,
}
```

Retrieving (GET) an item:

```javascript
{
    "id": int,
    "name": "string",
    "quantity": int,
    "initial_quantity": int
}
```

Creating (POST) or updating (PUT) an event:

```javascript
{
    "item": int, // item id
    "quantity_change": int
}
```

Retrieving (GET) an event:

```javascript
{
    "id": int,
    "item": int, // item id
    "quantity_change": int,
    "timestamp": "string"
}
```

### Filtering

The "items" endpoint supports the following query parameters:
* name (String)
* quantity (int)
* quantity_gt (int)
* quantity_gte (int)
* quantity_lt (int)
* quantity_lte (int)

Example: [kaliqwang.pythonanywhere.com/api/items/?name=water&quantity_gt=0](#) returns all items which have a name containing the string "water" and a quantity of greater than 0.

The "events" endpoint supports the following query parameters:
* item (int)
* year (int)
* month (int)

Example:  [kaliqwang.pythonanywhere.com/api/events/?item=23&year=2017&month=2](#) returns all events associated with the item having id=23 that occurred in Feb 2017.
