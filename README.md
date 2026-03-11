# quote-api
A simple REST API for managing inspirational quotes using Flask
# Quote API Documentation

## Installation
To install the Quote API project, clone the repository and install the dependencies:

```bash
git clone https://github.com/Dharanidhar28/quote-api.git
cd quote-api
npm install
Usage
To run the project locally, use the following command:

bash
npm start
Visit http://localhost:3000 to see the API in action.

API Endpoints
1. Get a Random Quote
Endpoint: /api/quote
Method: GET
Description: Returns a random quote.
2. Get a Quote by ID
Endpoint: /api/quote/:id
Method: GET
Description: Returns a quote by its ID.
3. Create a New Quote
Endpoint: /api/quote
Method: POST
Description: Adds a new quote to the collection.
Request Body: { "text": "string", "author": "string" }
4. Update a Quote
Endpoint: /api/quote/:id
Method: PUT
Description: Updates an existing quote by its ID.
Request Body: { "text": "string", "author": "string" }
5. Delete a Quote
Endpoint: /api/quote/:id
Method: DELETE
Description: Deletes a quote by its ID.
Feel free to contribute to the project!
