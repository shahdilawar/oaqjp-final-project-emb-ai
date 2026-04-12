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

    return response_text