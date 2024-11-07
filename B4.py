from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/B4G', methods=['GET'])
def funktion():
    square = lambda x: x * x
    result = square(5)

    return jsonify({
        'approach': 'simple lambda func',
        'result': result
    })


@app.route('/B4F', methods=['GET'])
def funktion_2():
    add = lambda x, y: x + y
    result = add(5, 3)

    return jsonify({
        'approach': 'complex lambda func',
        'result': result,
    })


@app.route('/B4E', methods=['GET'])
def funktion_3():
    words = ["apple", "banana", "kiwi", "pear", "grapefruit"]
    result = sorted(words, key=lambda word: len(word))

    return jsonify({
        'approach': 'sorted with lambda func',
        'result': f'{result}'
    })


if __name__ == '__main__':
    app.run()
