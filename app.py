from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store for demonstration
items = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99},
]


# GET: Retrieve all items
@app.route("/api/items", methods=["GET"])
def get_items():
    return jsonify(items), 200


# GET: Retrieve a specific item by ID
@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200


# POST: Add a new item
@app.route("/api/items", methods=["POST"])
def create_item():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    if "name" not in data or "price" not in data:
        return jsonify({"error": "Missing required fields: 'name' and 'price'"}), 400

    new_item = {"id": len(items) + 1, "name": data["name"], "price": data["price"]}
    items.append(new_item)
    return jsonify(new_item), 201


if __name__ == "__main__":
    # Runs the local development server
    app.run(debug=True, port=5000)
