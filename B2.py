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
def funktion():
    def apply_operation(func, x, y):
        return func(x, y)

    result = apply_operation(sum, 5, 10)

    return jsonify({
        'approach': 'func as an argument',
        'result': result,
    })


@app.route('/B2E', methods=['GET'])
def funktion():
    def create_multiplier(n):
        def multiplier(x):
            return x * n
        return multiplier

    double = create_multiplier(2)
    triple = create_multiplier(3)

    return jsonify({
        'approach': 'Closures',
        'result': (double, triple),
    })


if __name__ == '__main__':
    app.run()
