'''
This module is used for Unit testing
'''
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        '''
        Test the emotion joy
        '''
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        '''
        Test the emotion anger
        '''
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        '''
        Test the emotion disgust
        '''
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        '''
        Test the emotion sadness
        '''
        result = emotion_detector("I feel so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        '''
        Test the emotion fear
        '''
        result = emotion_detector("I am very afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == "__main__":
    unittest.main()