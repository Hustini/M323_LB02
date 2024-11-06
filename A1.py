from flask import Flask, jsonify, request

app = Flask(__name__)

# Beispiel-Daten
numbers = [1, 2, 3, 4, 5]


# Objektorientierte Programmierung
class SummationCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_sum(self):
        result = 0
        for num in self.numbers:
            result += num
        return result


@app.route('/A1E/functional', methods=['GET'])
def get_functional_sum():
    result = sum(numbers)
    return jsonify({
        'approach': 'functional',
        'result': result,
        'numbers': numbers
    })


@app.route('/A1E/procedural', methods=['GET'])
def get_procedural_sum():
    result = 0
    for num in numbers:
        result += num

    return jsonify({
        'approach': 'procedural',
        'result': result,
        'numbers': numbers
    })


@app.route('/A1E/oop', methods=['GET'])
def get_oop_sum():
    calculator = SummationCalculator(numbers)
    result = calculator.calculate_sum()
    return jsonify({
        'approach': 'object-oriented',
        'result': result,
        'numbers': numbers
    })


if __name__ == '__main__':
    app.run()
