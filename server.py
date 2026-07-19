"""
This module is used to host the server using Flask.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def root_endpoint():
    """
    This function handles the root endpoint of the server.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """
    This function handles GET requests on the /emotionDetector endpoint.
    It returns a text response evaluating the emotion of the input text.
    The input text is entered through HTTP arguments.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze == "":
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return_string = "For the given statement, the system response is "
    return_string += f"'anger': {result['anger']}, "
    return_string += f"'disgust': {result['disgust']}, "
    return_string += f"'fear': {result['fear']}, "
    return_string += f"'joy': {result['joy']} and "
    return_string += f"'sadness': {result['sadness']}. "
    return_string += f"The dominant emotion is {result['dominant_emotion']}."

    return return_string

app.run()
