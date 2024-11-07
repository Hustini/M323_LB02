from functools import reduce
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/B4G', methods=['GET'])
def funktion():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    sum_of_numbers = reduce(lambda x, y: x + y, numbers)

    return jsonify({
        'approach': 'map, filter, reduce',
        'result': f'map: {squared_numbers}, filter: {even_numbers}, reduce: {sum_of_numbers}',
    })


@app.route('/B4F', methods=['GET'])
def funktion_2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers))

    return jsonify({
        'approach': 'list of all even numbers double',
        'result': list(result),
    })


@app.route('/B4E', methods=['GET'])
def funktion_3():
    cart = [
        {"product": "A", "price": 15, "quantity": 2},
        {"product": "B", "price": 25, "quantity": 1},
        {"product": "C", "price": 30, "quantity": 3},
        {"product": "D", "price": 20, "quantity": 1}
    ]

    expensive_products = filter(lambda item: item["price"] > 20, cart)
    result = map(lambda item: item["price"] * item["quantity"], expensive_products)

    return jsonify({
        'approach': 'Total value per product where price over 20',
        'result': list(result)
    })


if __name__ == '__main__':
    app.run()
