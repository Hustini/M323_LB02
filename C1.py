from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/C1G', methods=['GET'])
def funktion():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 0
    for i in range(len(data)):
        result += data[i]

    result = sum(data)

    return jsonify({
        'approach': 'Refactoring',
        'result': f'{result}',
    })


@app.route('/C1F', methods=['GET'])
def funktion_2():
    data = [1, 2, 3, 4, 5]
    result = 0
    for i in range(len(data)):
        result += data[i]

    result = sum(data)

    return jsonify({
        'approach': 'Refactoring',
        'result': f'{result}',
    })


@app.route('/C1E', methods=['GET'])
def funktion_3():

    return jsonify({
        'approach': '',
        'result': f''
    })


if __name__ == '__main__':
    app.run()
