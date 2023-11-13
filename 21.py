from flask import Flask, jsonify, request
app = Flask(__name__)
heart = [
    {
        "heart-id": "60",
        "date": "10/10/2024",
        "heart-rate": "180bpm"
    },
    {
        "heart-id": "40",
        "date": "11/11/2024",
        "heart-rate": "140bpm"
    }

]

@app.route('/21', methods=['GET'])
def get_heart():
    return jsonify(heart)

@app.route('/21', methods=['POST'])
def add_heart():
    new_heart = request.get_json()
    heart.append(new_heart)
    return {'heart-id':len(new_heart)}, 200


@app.route('/21/<int:index>', methods=['DELETE'])
def delete_heart(index):
    heart.pop =(index)
    return 'Heart rate deleted', 200

if __name__ == "__main__":
    app.run()