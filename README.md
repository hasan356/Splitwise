# Splitwise

This is the application similar to splitwise which divides the expenses
between friends in a group.

## Prerequisite
You should have python3 installed on your system. If not installed, you can
install it from [here](https://www.python.org/downloads/).

## Build the application
```
    make build
```
It will install all the dependency and requirement needed for this application

## Running the application
```
    make run
```
This will start the application server locally running at port 8000

## API Documentation

[Design Doc](https://docs.google.com/document/d/1iMovoLf7-w_uCO54O3L09IQjEfM1xtGwl0ouLuSOCXs/edit#)

[Postman Collection](https://www.getpostman.com/collections/207a5d72e78ea2761e79)

Following api are exposed
## 1. Create User

Endpoint - localhost:8000/splitwise/user 

Method - POST

Request Body 
```
{
    "email": "hasan.15021995@gmail.com"
}
```

```
curl --location --request POST 'localhost:8000/splitwise/user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "hasan.15021995@gmail.com"
}'

```

## 2. Create Group

Endpoint - localhost:8000/splitwise/group 

Method - POST

Request Body 
```
{
    "name": "office"
}
```

```
curl --location --request POST 'localhost:8000/splitwise/group' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "name": "coffee"
}'

```

## 3. Assign User

Endpoint - localhost:8000/splitwise/assign-user 

Method - POST

Request Body 
```
{
    "user_email": "hasan.150295@gmail.com",
    "group_name": "coffee"
}
```

```
curl --location --request POST 'localhost:8000/splitwise/assign-user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_email": "hasan.150295@gmail.com",
    "group_name": "coffee"
}'

```

## 4. Create Expenses

Endpoint - localhost:8000/splitwise/expense

Method - POST

Request Body 

1. Exact Split

```
{
    "name": "Breakfast",
    "created_by": "hasan.150295@gmail.com",
    "amount": 100,
    "expense_type": "EXACT",
    "group_name": "test",
    "split_map": {
        "hasan.150295@gmail.com": 30,
        "hasan.a@toppr.com": 10,
        "hasan.15021995@gmail.com": 60
    }
}
```

```
curl --location --request POST 'localhost:8000/splitwise/expense' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Breakfast",
    "created_by": "hasan.150295@gmail.com",
    "amount": 100,
    "expense_type": "EQUAL",
    "group_name": "test",
    "split_map": {
        "hasan.150295@gmail.com": 30,
        "hasan.a@toppr.com": 10,
        "hasan.15021995@gmail.com": 60
    }
}'
```

2. Equal Split

```
{
    "name": "Test",
    "created_by": "hasan.150295@gmail.com",
    "amount": 100,
    "expense_type": "EQUAL",
    "group_name": "test"
}

```
```
curl --location --request POST 'localhost:8000/splitwise/expense' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Test",
    "created_by": "hasan.150295@gmail.com",
    "amount": 100,
    "expense_type": "EQUAL",
    "group_name": "test"
}'
```

## 5. User Transactions

Endpoint - localhost:8000/splitwise/expense

Method - GET

Query Params 
1. ?email=hasan.15021995@gmail.com&status=pending
2. ?email=hasan.15021995@gmail.com&status=settled
Response Format

```

[
    {
        "Date": "17/September",
        "Group": "test",
        "Expense": "Breakfast",
        "Amount": "100.00",
        "Pending": "10.00"
    },
    {
        "Date": "17/September",
        "Group": "test",
        "Expense": "Lunch",
        "Amount": "100.00",
        "Pending": "20.00"
    },
    {
        "Date": "17/September",
        "Group": "test",
        "Expense": "Dinner",
        "Amount": "100.00",
        "Pending": "33.33"
    },
    {
        "Date": "17/September",
        "Group": "test",
        "Expense": "Late Night",
        "Amount": "120.00",
        "Pending": "40.00"
    },
    {
        "Date": "17/September",
        "Group": "test",
        "Expense": "Test",
        "Amount": "100.00",
        "Pending": "33.33"
    }
]

```

## 6. Settle Amount

Endpoint - localhost:8000/splitwise/settle

Method - POST

Request Body

```

{
    "user_email": "hasan.15021995@gmail.com",
    "settle_user_email": "hasan.150295@gmail.com"
}

```
```
curl --location --request POST 'localhost:8000/splitwise/settle' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_email": "hasan.15021995@gmail.com",
    "settle_user_email": "hasan.150295@gmail.com"
}'
```