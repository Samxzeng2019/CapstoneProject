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
- get:actors
- get:movies

#### Casting Director  
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies  
- delete:actors	
- get:actors
- get:movies
- patch:actors
- patch:movies
- post:movies

#### Executive Producer  
All permissions a Casting Director has and…
Add or delete a movie from the database
- delete:actors	
- delete:movies	
- get:actors
- get:movies
- patch:actors
- patch:movies
- post:actors	
- post:movies

### Permissions: 
- delete:actors	
- delete:movies	
- get:actors
- get:movies
- patch:actors
- patch:movies
- post:actors	
- post:movies

### Tests and authentication:
Test cases are included in the postman test collect with respective latest jwt token included for testing. 

If the jwt token expires upon reviewing, one can use these credentials below to authenticate and get the updated jwt respectively: 

Sign up url: https://fullstackiam.us.auth0.com/authorize?audience=movies&response_type=token&client_id=oD6Qs5cOnmppeoZsMtF3MpzNXXqcyC1Z&redirect_uri=https://localhost:5000&state=STATE

Authentication credentials:

| Authentication | Casting Assistant               | Casting Director               | Executive Director               |
| -------------- | ------------------------------- | ------------------------------ | -------------------------------- |
| username       | castingassistant20@capstone.com | castingdirector30@capstone.com | executivedirector40@capstone.com |
| password       | castingassistant20@capstone.com | castingdirector30@capstone.com | executivedirector40@capstone.com |


## API Endpoints

### Endpoints description:
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/

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

