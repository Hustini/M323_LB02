from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/B1G', methods=['GET'])
def get_pure_function_result():
    return jsonify({})


@app.route('/B1F', methods=['GET'])
def get_immutable_values_result():
    return jsonify({})


@app.route('/B1E', methods=['GET'])
def get_functional_sum():
    return jsonify({})


if __name__ == '__main__':
    app.run()
