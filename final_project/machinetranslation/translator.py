import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(
    version='2021-08-30',
    authenticator=authenticator
)

lt.set_service_url(url)

def englishToFrench(englishText):
    #write the code here
    translation = lt.translate(text=englishText, model_id='en-fr').get_result()
    
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    translation = lt.translate(text=frenchText, model_id='fr-en').get_result()
    
    englishText = translation['translations'][0]['translation']
    return englishText  