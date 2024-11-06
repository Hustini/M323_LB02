from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/A1G', methods=['GET'])
def get_pure_function_result():
    numbers = [1, 2, 3, 4, 5]
    def pure_function(nums):
        return sum(nums)

    result = pure_function(numbers)
    return jsonify({
        'approach': 'pure function',
        'result': result,
        'numbers': numbers
    })


@app.route('/A1F', methods=['GET'])
def get_immutable_values_result():
    def demonstrate_immutable_values():
        immutable_tuple = (1, 2, 3)

        try:
            immutable_tuple[0] = 10
        except TypeError as e:
            tuple_error = str(e)

        return tuple_error
    
    result = demonstrate_immutable_values()
    return jsonify({
        'approach': 'immutable function',
        'result': result,
    })


@app.route('/A1E/functional', methods=['GET'])
def get_functional_sum():
    numbers = [1, 2, 3, 4, 5]
    result = sum(numbers) # numbers = [1, 2, 3, 4, 5]
    return jsonify({
        'approach': 'functional',
        'result': result,
        'numbers': numbers
    })


@app.route('/A1E/procedural', methods=['GET'])
def get_procedural_sum():
    numbers = [1, 2, 3, 4, 5]
    result = 0
    for num in numbers:  # numbers = [1, 2, 3, 4, 5]
        result += num

    return jsonify({
        'approach': 'procedural',
        'result': result,
        'numbers': numbers
    })


@app.route('/A1E/oop', methods=['GET'])
def get_oop_sum():
    numbers = [1, 2, 3, 4, 5]
    calculator = SummationCalculator(numbers)  # numbers = [1, 2, 3, 4, 5]
    result = calculator.calculate_sum()
    return jsonify({
        'approach': 'object-oriented',
        'result': result,
        'numbers': numbers
    })


# Objektorientierte Programmierung
class SummationCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_sum(self):
        result = 0
        for num in self.numbers:
            result += num
        return result


if __name__ == '__main__':
    app.run()
