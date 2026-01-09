<!-- Simple Review Management API  -->

<!-- Objective -->
A basic backend service to manage reviews using CRUD operations.
Built using Python and Flask.



<!-- How to Run the Project -->

<!-- 1. Clone the repository -->
git clone <repo-url>
cd review-api

shell
Copy code

<!-- 2. Install dependencies -->
pip install -r requirements.txt

shell
Copy code

<!-- 3. Run the application -->
python app.py

powershell
Copy code

The server will start at:
http://127.0.0.1:5000

yaml
Copy code

---

 <!-- API Endpoints -->
 
 <!-- 1. Create Review --> 
**POST** `/reviews`

**Request Body**
```json
{
  "user_name": "Devaraj",
  "rating": 4,
  "comment": "Good service"
}
Success Response (201)

json
Copy code
{
  "message": "Review created successfully",
  "review": {
    "id": 1,
    "user_name": "Devaraj",
    "rating": 4,
    "comment": "Good service"
  }
}
Validation Errors (400)

user_name empty

rating not between 1–5

// 2. Fetch Reviews

GET /reviews

Response (200)

json
Copy code
[
  {
    "id": 1,
    "user_name": "Devaraj",
    "rating": 4,
    "comment": "Good service"
  }
]
Latest reviews appear first.

// 3. Update Review
PUT /reviews/{id}

Request Body

json
Copy code
{
  "rating": 5,
  "comment": "Excellent service"
}
Success Response (200)

json
Copy code
{
  "message": "Review updated successfully",
  "review": {
    "id": 1,
    "user_name": "Devaraj",
    "rating": 5,
    "comment": "Excellent service"
  }
}
Error (404)

json
Copy code
{
  "error": "Review not found"
}
// 4. Delete Review
DELETE /reviews/{id}

Success Response (200)

json
Copy code
{
  "message": "Review deleted successfully"
}
Error (404)

json
Copy code
{
  "error": "Review not found"
}
// HTTP Status Codes Used
201 – Created

200 – Success

400 – Bad Request

404 – Not Found

// #Assumptions
Data is stored in memory (no persistence required)

IDs are auto-incremented

No authentication required

Focus is on backend logic and API clarity