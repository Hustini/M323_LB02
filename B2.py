from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/B2G', methods=['GET'])
def funktion():
    def add(x, y):
        return x + y
    tmp = add
    result = tmp(2, 3)
    return jsonify({
        'approach': 'store func in variable',
        'result': result
    })


@app.route('/B2F', methods=['GET'])
def funktion_2():
    def apply_to_list(func, value):
        return func(value)
    def square(x):
        return x * x

    x = 2
    result = apply_to_list(square, x)

    return jsonify({
        'approach': 'func as an argument',
        'result': result,
    })


@app.route('/B2E', methods=['GET'])
def funktion_3():
    def create_multiplier(n):
        def multiplier(x):
            return x * n
        return multiplier

    result = create_multiplier(2)

    return jsonify({
        'approach': 'Closures',
        'result': f'{result}'
    })


if __name__ == '__main__':
    app.run()
