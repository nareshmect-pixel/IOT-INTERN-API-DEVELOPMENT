from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
students = [
    {"id": 1, "name": "Naresh"},
    {"id": 2, "name": "Sakthi"}
]

# GET API
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# POST API
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json

    new_student = {
        "id": len(students) + 1,
        "name": data["name"]
    }

    students.append(new_student)

    return jsonify({
        "message": "Student Added",
        "student": new_student
    })

# PUT API
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json

    for student in students:
        if student["id"] == id:
            student["name"] = data["name"]

            return jsonify({
                "message": "Student Updated",
                "student": student
            })

    return jsonify({"message": "Student Not Found"}), 404

# DELETE API
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):

    for student in students:
        if student["id"] == id:
            students.remove(student)

            return jsonify({
                "message": "Student Deleted"
            })

    return jsonify({"message": "Student Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True)