from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/B4G', methods=['GET'])
def funktion():

    return jsonify({
        'approach': 'map, filter, reduce',
        'result': f'',
    })


@app.route('/B4F', methods=['GET'])
def funktion_2():

    return jsonify({
        'approach': 'list of all even numbers double',
        'result': f'',
    })


@app.route('/B4E', methods=['GET'])
def funktion_3():

    return jsonify({
        'approach': 'Total value per product where price over 20',
        'result': f''
    })


if __name__ == '__main__':
    app.run()
