import PyPDF2
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

#Using the IBM Bluemix Text to Speech API
IBMAPIKey = os.environ.get("IBMApiKey")
IBM_Endpoint = os.environ.get("IBMEndpoint")
authenticator = IAMAuthenticator(IBMAPIKey)
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url(IBM_Endpoint)

filename = "how2use.pdf"
splitname = filename.split(".")[0]
basefile = open(filename, 'rb')
fileReader = PyPDF2.PdfFileReader(basefile)

for page in range(0,fileReader.numPages):
    pageText = fileReader.getPage(page).extractText()
    with open(f"{splitname} - Page {page + 1}.wav", 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                pageText,
                voice='en-GB_KateVoice',
                accept='audio/wav'
            ).get_result().content)