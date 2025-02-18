from flask import Flask, request, jsonify, render_template
import boto3

app = Flask(__name__)

# Configure Boto3 to use LocalStack
dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1',
    endpoint_url='http://localhost:4566',  # LocalStack URL
    aws_access_key_id='test',
    aws_secret_access_key='test'
)

# DynamoDB Table Name
TABLE_NAME = "QueryTable"
table = dynamodb.Table(TABLE_NAME)

# Home Page - Show Dataset
@app.route('/')
def home():
    response = table.scan()  # Fetch all users
    users = response.get("Items", [])
    return render_template("index.html", users=users)

# Insert a User (POST)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    table.put_item(Item=data)
    return jsonify({"message": "User added successfully"}), 201

# Get a User by ID (GET)
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    response = table.get_item(Key={'UserID': user_id})
    if 'Item' in response:
        return jsonify(response['Item'])
    return jsonify({"error": "User not found"}), 404

# Update a User (PUT)
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    table.update_item(
        Key={'UserID': user_id},
        UpdateExpression="SET #name = :name, Email = :email",
        ExpressionAttributeNames={"#name": "Name"},
        ExpressionAttributeValues={":name": data["Name"], ":email": data["Email"]},
    )
    return jsonify({"message": "User updated successfully"})

# Delete a User (DELETE)
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    table.delete_item(Key={'UserID': user_id})
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
