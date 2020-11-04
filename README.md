# CapstoneProject
Capstone project for Udacity full stack nanodegree
Using demo cases to craft

## Project description
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

### Models:
Movies with attributes title and release date
Actors with attributes name, age and gender

### Roles:
#### Casting Assistant  
Can view actors and movies
1. get:actors
1. get:movies

#### Casting Director  
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies  
1. delete:actors	
1. get:actors
1. get:movies
1. patch:actors
1. patch:movies
1. post:movies

#### Executive Producer  
All permissions a Casting Director has and…
Add or delete a movie from the database
1. delete:actors	
1. delete:movies	
1. get:actors
1. get:movies
1. patch:actors
1. patch:movies
1. post:actors	
1. post:movies

### Permissions: 
1. delete:actors	
1. delete:movies	
1. get:actors
1. get:movies
1. patch:actors
1. patch:movies
1. post:actors	
1. post:movies

### Tests and authentication:
Test cases are included in the postman test collection with the latest jwt token included for each role to test the api. 
Run the whole collection ```Capstone Project.postman_collection.json``` in sequence will simulate all the errors and successes from the endpoints. 

If the jwt token expires upon reviewing, one can use these credentials below to authenticate and get the updated jwt respectively: 

Sign up url: https://fullstackiam.us.auth0.com/authorize?audience=movies&response_type=token&client_id=oD6Qs5cOnmppeoZsMtF3MpzNXXqcyC1Z&redirect_uri=http://localhost:5000&state=STATE

Authentication credentials:

| Authentication | Casting Assistant               | Casting Director               | Executive Director               |
| -------------- | ------------------------------- | ------------------------------ | -------------------------------- |
| username       | castingassistant20@capstone.com | castingdirector30@capstone.com | executivedirector40@capstone.com |
| password       | castingassistant20@capstone.com | castingdirector30@capstone.com | executivedirector40@capstone.com |


### API Endpoints description:
- POST /actors and /movies and
- PATCH /actors/ and /movies/
- GET /actors and /movies
- DELETE /actors/ and /movies/

#### POST '/actors'
- Add actors profile to the database
- Request Arguments: Dictionary object with keys: age, gender, name
- Response: An object with success status and actor details. 
<details>
<summary>Sample response</summary>

```
{
    "actors": {
        "age": 35,
        "gender": "male",
        "id": 1,
        "name": "James"
    },
    "success": true
}
```
</details>

#### POST '/movies'
- Add movie profile to the database
- Request Arguments: Dictionary object with keys: title and release_date
- Response: An object with success status and movie details. 
<details>
<summary>Sample response</summary>

```
{
    "movies": {
        "id": 1,
        "release_date": "20-Oct-2019",
        "title": "Spider man"
    },
    "success": true
}
```
</details>

#### PATCH '/actors/<int:actor_id>'
- Update actors profile to the database from selected actor id
- Request Arguments: Dictionary object with keys: age, gender, name
- Response: An object with success status and actor details. 
<details>
<summary>Sample response</summary>

```
{
    "actors": {
        "age": 44,
        "gender": "male",
        "id": 2,
        "name": "Ray"
    },
    "success": true
}
```
</details>

#### PATCH '/movies/<int:movie_id>'
- Update movies profile to the database from selected movie id
- Request Arguments: Dictionary object with keys: title and release_date
- Response: An object with success status and movies details. 
<details>
<summary>Sample response</summary>

```
{
    "movies": {
        "id": 2,
        "release_date": "20-Aug-2011",
        "title": "Cars"
    },
    "success": true
}
```
</details>

#### GET '/actors'
- Query actors profile to the database
- Request Arguments: None
- Response: An object with success status and actor details in array. 
<details>
<summary>Sample response</summary>

```
{
    "actors": [
        {
            "age": 35,
            "gender": "male",
            "id": 1,
            "name": "James"
        },
        {
            "age": 44,
            "gender": "male",
            "id": 2,
            "name": "Ray"
        }
    ],
    "success": true
}
```
</details>

#### GET '/movies'
- Update movies profile to the database 
- Request Arguments: None
- Response: An object with success status and movies details in array. 
<details>
<summary>Sample response</summary>

```
{
    "movies": [
        {
            "id": 1,
            "release_date": "20-Oct-2019",
            "title": "Spider man"
        },
        {
            "id": 2,
            "release_date": "20-Aug-2011",
            "title": "Cars"
        }
    ],
    "success": true
}
```
</details>

#### DELETE '/actors/<int:actor_id>'
- Delete actors profile to the database from selected actor id
- Request Arguments: None
- Response: An object with success status and deleted actor id. 
<details>
<summary>Sample response</summary>

```
{
    "delete": 2,
    "success": true
}
```
</details>

#### DELETE '/movies/<int:movie_id>'
- Delete movies profile to the database from selected movie id
- Request Arguments: None
- Response: An object with success status and deleted movie id. 
<details>
<summary>Sample response</summary>

```
{
    "delete": 3,
    "success": true
}
```
</details>