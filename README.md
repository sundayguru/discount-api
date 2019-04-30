# discount-api

A simple api to assign/retrieve serial number discount.

## Prerequisite

You need to have installed the latest version of Python. All commands assumes you are on MAC.

## Installation

I have created `setup.sh` for easy setup. Run `source setup.sh` in your terminal.

Visit http://127.0.0.1:8000/admin to see application admin. user: `admin` password: `notsecret`.

Browse api http://127.0.0.1:8000/api/v1

## Tests

To run the test suite. run `source tests.sh` in your terminal.

## Endpoints

### POST /api/v1/serialnumbers/discount/

Assign or retrieve serial number discount.
Permission: any

#### Input
- serial: the serial number (required)

#### Response
```
{
    "discount": "test-code"
}
```

### GET /api/v1/serialnumbers/

List all serialnumbers.
Permission: authenticated

### GET /api/v1/disscounts/

List all discounts.
Permission: authenticated
