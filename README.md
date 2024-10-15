# Characters API

## Description

This API allows interaction with character data, enabling operations such as querying, inserting, and deleting characters. The API is developed in Python using the FastAPI framework and SQLAlchemy for managing the SQLite database.

## Features

- Retrieve all stored characters.
- Retrieve character data by ID.
- Insert a new character.
- Delete a character by ID.

## Data Structure

Each character has the following structure:

```json
{
  "id": 1,
  "name": "Luke Skywalker",
  "height": 172,
  "mass": 77,
  "hair_color": "blond",
  "skin_color": "fair",
  "eye_color": "blue",
  "birth_year": 1998
}
```

## Installation
Clone the repository:
```bash
git clone https://github.com/ilCat/pi-challenge.git

cd pi-challenge
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

```
uvicorn main:app --reload
```
## Running with Docker
To run the API in a Docker container, follow these steps:

Build the Docker image:
```bash
docker build -t characters-api .
```
Run the Docker container:
```bash
docker run -d -p 8000:8000 characters-api
```
The API will be accessible at http://localhost:8000.

## Usage
You can test the API using tools like Postman or cURL. Below is an example of how to make a GET request to retrieve all characters:

curl -X GET "http://127.0.0.1:8000/character/getAll"

## Endpoints
#### Get All Characters

URL: /character/getAll

Method: GET

Description: Returns a list of all characters.

#### Get Character by ID

URL: /character/get/{id}

Method: GET

Description: Returns the data of the character with the specified ID.

#### Add a New Character

URL: /character/add

Method: POST

Description: Inserts a new character. All fields are required and must comply with the data structure.

#### Delete Character by ID

URL: /character/delete/{id}

Method: DELETE

Description: Deletes the character with the specified ID.