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
    def sort_pass(lst):
        if len(lst) <= 1:
            return lst
        if lst[0] > lst[1]:
            return [lst[1]] + sort_pass([lst[0]] + lst[2:])
        return [lst[0]] + sort_pass(lst[1:])

    def sort(lst, n=None):
        if n is None:
            n = len(lst)
        if n == 1:
            return lst
        lst = sort_pass(lst)
        return sort(lst, n - 1)

    numbers = [5, 4, 3, 2, 1]
    result = sort(numbers)
    return jsonify({
        'approach': 'functional algorithm',
        'result': result,
        'numbers': numbers
    })


@app.route('/B1E', methods=['GET'])
def get_functional_sum():
    return jsonify({})


if __name__ == '__main__':
    app.run()
