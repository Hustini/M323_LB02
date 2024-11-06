from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/B1G', methods=['GET'])
def algorithm():
    numbers = [1, 2, 3, 4, 5]
    result = 0
    for number in numbers:
        result += number
    return jsonify({
        'approach': 'algorithm',
        'result': result,
        'numbers': numbers
    })


@app.route('/B1F', methods=['GET'])
def get_immutable_values_result():
    return jsonify({})


@app.route('/B1E', methods=['GET'])
def get_functional_sum():
    return jsonify({})


if __name__ == '__main__':
    app.run()
