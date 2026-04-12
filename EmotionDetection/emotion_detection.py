'''
This module is used to detect emotion using Watson NLP libraries
'''
import requests
import json

def emotion_detector(text_to_analyze : str):
    # URL of the watson library
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers dictionary to be passed to the NLP library
    headers =  {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, headers = headers, json = myobj)

    # Retrieve the response from the NLP model
    response_text = response.text

    #Retrieve the emotions alone.
    emotion_dict = json.loads(response_text)['emotionPredictions'][0]['emotion']

    # Identify the max score and the dominant emotion.
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

   # Add the dominant emotion to the dictionary.    
    emotion_dict['dominant_emotion'] = dominant_emotion

    return emotion_dict