from flask import Flask, jsonify, request
import get_prediction

@app.route("/predict_alphabets", methods=["post"])
def predict_data():
    image = request.files.get("alphabets")
    prediction = get_prediction(image)
    return jsonify({
        "prediction":prediction

    }), 200