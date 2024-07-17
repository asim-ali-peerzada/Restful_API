"# Restful_API" 
curl -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d "{\"username\": \"admin\", \"password\": \"admin\"}"

This should return a JWT token if the credentials are correct.

By following these steps, you should be able to create a user and obtain a JWT token for testing your API.