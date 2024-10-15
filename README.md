# Characters API

## Description

This API allows interaction with character data, enabling operations such as querying, inserting, and deleting characters. The API is developed in Python using the FastAPI framework and SQLAlchemy for managing the SQLite database.

## Features

- Retrieve all stored characters.
- Retrieve character data by ID.
- Insert a new character.
- Delete a character by ID.

## Requirements
Python 3.9^
Docker 

## Installation
Clone the repository:
```bash
git clone https://github.com/ilCat/characters-api.git

cd characters-api
```
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
Start the application:

```bash
fastapi dev app/main.py 
```

The API will be accessible at http://localhost:8000.
The API documentation will be accessible at http://localhost:8000/docs.

## Running with Docker
To run the API in a Docker container, follow these steps:

Build the Docker image:
```bash
docker-compose build
```
Run the Docker container:
```bash
docker-compose up
```
Stop the Docker container:
```bash
docker-compose down
```
The API will be accessible at http://localhost:8000.
The API documentation will be accessible at http://localhost:8000/docs.

## Usage
You can test the API using tools like Postman or cURL. Below is an example of how to make a GET request to retrieve all characters:

curl -X GET "http://127.0.0.1:8000/character/getAll"

## Data Structure

Each character has the following structure:

```json
{
    "id": 1,
    "name": "Tokita Ohma",
    "height": 1.82,
    "mass": 85.0,
    "hair_color": "black",
    "skin_color": "white",
    "eye_color": "black",
    "birth_year": 1992
}
```


## Endpoints
#### Get All Characters

URL:  http://localhost:8000/character/getAll

Method: GET

Description: Returns a list of all characters.

#### Get Character by ID

URL:  http://localhost:8000/character/get/{id}

Method: GET

Description: Returns the data of the character with the specified ID.

#### Add a New Character

URL:  http://localhost:8000/character/add

Method: POST

Description: Inserts a new character. All fields are required and must comply with the data structure.

#### Delete Character by ID

URL:  http://localhost:8000/character/delete/{id}

Method: DELETE

Description: Deletes the character with the specified Id.