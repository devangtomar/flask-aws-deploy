from flask import Blueprint, request, jsonify

api_bp = Blueprint("api", __name__)

items = {}

@api_bp.route("/items", methods=["GET"])
def get_items():
    return jsonify(items), 200

@api_bp.route("/items/<item_id>", methods=["GET"])
def get_item(item_id):
    item = items.get(item_id)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

@api_bp.route("/items", methods=["POST"])
def create_item():
    data = request.json
    item_id = str(len(items) + 1)
    items[item_id] = data
    return jsonify({"id": item_id, "data": data}), 201

@api_bp.route("/items/<item_id>", methods=["PUT"])
def update_item(item_id):
    if item_id in items:
        items[item_id] = request.json
        return jsonify({"id": item_id, "data": items[item_id]}), 200
    return jsonify({"error": "Item not found"}), 404

@api_bp.route("/items/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return jsonify({"message": "Item deleted"}), 200
    return jsonify({"error": "Item not found"}), 404