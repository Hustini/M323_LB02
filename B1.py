from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/B1G', methods=['GET'])
def algorithm():
    numbers = [5, 4, 3, 2, 1]
    def bubble_sort(numbers):
        sorted = False
        while not sorted:
            changed = False
            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    changed = True
            if not changed:
                sorted = True
                return numbers
    result = bubble_sort(numbers)

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
