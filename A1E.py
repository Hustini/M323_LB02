from flask import Flask, jsonify, request

app = Flask(__name__)


# Objektorientierter Ansatz
class RectangleOO:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Prozeduraler Ansatz
def calculate_area_procedural(width, height):
    return width * height


# Funktionaler Ansatz
calculate_area_functional = lambda width, height: width * height


@app.route('/A1E', methods=['GET', 'POST'])
def a1e():
    width = 1
    height = 1

    # Objektorientierte Lösung
    rectangle_oo = RectangleOO(width, height)
    area_oo = rectangle_oo.area()

    # Prozedurale Lösung
    area_procedural = calculate_area_procedural(width, height)

    # Funktionale Lösung
    area_functional = calculate_area_functional(width, height)

    return f'object_oriented: {area_oo}, procedural: {area_procedural}, functional: {area_functional}'


if __name__ == '__main__':
    app.run()
