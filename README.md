# CapstoneProject
Capstone project for Udacity full stack nanodegree
Using demo cases to craft

## Project description
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

### Models:
Movies with attributes title and release date
Actors with attributes name, age and gender

### Endpoints:
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/

### Roles:
- Casting Assistant  
Can view actors and movies

- Casting Director  
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies  

- Executive Producer  
All permissions a Casting Director has and…
Add or delete a movie from the database

### Tests:
One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role

## Authentication
This app use jwt from Auth0 to perform the authentication for each role. 


## API Endpoints

### GET '/categories'
- Fetches all categories. 
- Request Arguments: None
- Response: An object with success status, categories list and total_categories. The dictionary keys are id and types. 
<details>
<summary>Sample response</summary>

```
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "success": true, 
  "total_categories": 6
}
```
</details>

