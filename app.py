from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
reviews = []
current_id = 1


# Helper function to find review by ID
def find_review(review_id):
    return next((r for r in reviews if r["id"] == review_id), None)


# 1. Create Review API
@app.route("/reviews", methods=["POST"])
def create_review():
    global current_id

    data = request.get_json()

    user_name = data.get("user_name")
    rating = data.get("rating")
    comment = data.get("comment", "")

    # Validation
    if not user_name or user_name.strip() == "":
        return jsonify({"error": "user_name is required"}), 400

    if not isinstance(rating, int) or rating < 1 or rating > 5:
        return jsonify({"error": "rating must be an integer between 1 and 5"}), 400

    review = {
        "id": current_id,
        "user_name": user_name,
        "rating": rating,
        "comment": comment
    }

    reviews.insert(0, review)  # latest first
    current_id += 1

    return jsonify({
        "message": "Review created successfully",
        "review": review
    }), 201


# 2. Fetch Reviews API
@app.route("/reviews", methods=["GET"])
def get_reviews():
    return jsonify(reviews), 200


# 3. Update Review API
@app.route("/reviews/<int:review_id>", methods=["PUT"])
def update_review(review_id):
    review = find_review(review_id)

    if not review:
        return jsonify({"error": "Review not found"}), 404

    data = request.get_json()

    rating = data.get("rating")
    comment = data.get("comment")

    if rating is not None:
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return jsonify({"error": "rating must be between 1 and 5"}), 400
        review["rating"] = rating

    if comment is not None:
        review["comment"] = comment

    return jsonify({
        "message": "Review updated successfully",
        "review": review
    }), 200


# 4. Delete Review API
@app.route("/reviews/<int:review_id>", methods=["DELETE"])
def delete_review(review_id):
    review = find_review(review_id)

    if not review:
        return jsonify({"error": "Review not found"}), 404

    reviews.remove(review)

    return jsonify({
        "message": "Review deleted successfully"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
