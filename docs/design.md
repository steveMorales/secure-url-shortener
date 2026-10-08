High Level Concept:

GET /health -> general health check for containers
POST /shorten -> The app will accept a URL, validate it, stores it, returns a code
GET /{code} -> looks up the code and redirects, or returns error code (404)
Some tests (pytest): valid URL, invalid URL, unknown code, health check

Design Notes:

Short code generation

1. Random String -> predictable?
    Can account for this via pythons secret module (maybe random but that is predictable too)
2. Hash of URL -> collisions? 
    retry on collision

Repeated URL -> keep all old codes valid (this could result in memory issues)

URL Schemes -> beginning with only http:// and https:// all others "invalid"

Currently no database -> v1 will have in-memory dict storage

302 redirect: I want to track every time the link is clicked. This will result in higher load on server but would add data collection capabilities and allow me to add a feature to potentially track site visits

Max URL Length: 2048 characters -> common practice to max at this to avoid issues

Error Handling: 

400 Bad Request: invalid URL
403 Forbidden: Blocked Domain, can add these in for malicious sites

Success:

200 OK: Returns the shortened url

Code length will be 6 so should create 62^6 unique codes (alphabet size is 62 in base62). This is ideal because the likelihood of a collision with a new code and an existing code is extremely low. Similarly its very unlikely that an attacker will guess a code correctly with a code length of 6 especially in v1.


