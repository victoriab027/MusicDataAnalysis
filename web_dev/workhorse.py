from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/save_slider_value', methods=['POST'])
def save_slider_value():
    data = request.get_json()
    slider_value = data['sliderValue']
    # Do something with the slider value
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run()
