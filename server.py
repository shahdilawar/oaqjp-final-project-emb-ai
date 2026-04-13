'''
This module serves as Customer facing function using Flask
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Instantiate Flask object
app = Flask(__name__)

@app.route("/")
def home():
    '''
    This method is to route to index page.
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_analyzer():
    '''
    This method will take in the user sentence and analyze the dominant emotion.
    '''

    # retrieve the input query value
    text_to_analyze = request.args.get("textToAnalyze")

    # Retrieve the emotion dictionary
    emotion_dict = emotion_detector(text_to_analyze)

    # handle invalid / blank input
    if emotion_dict['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the output
    formatted_output = format_output(emotion_dict)

    return formatted_output


def format_output(result):
    '''
    Utility module to format the output.
    '''
    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    