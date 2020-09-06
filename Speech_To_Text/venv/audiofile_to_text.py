# Here we have written the code to convert audio file to text

import speech_recognition as sr

'''speech_recognition is a library for performing speech recognition, before using this please install this using pip 
install SpeechRecognition '''

r = sr.Recognizer()
'''The Recognizer instance is used to recognize speech'''

audio1 = 'C:\\Users\\tushar.raj01\\Downloads\\Speech_To_Text\\Speech_To_Text\\audio_files\\harvard.wav'

with sr.AudioFile(audio1) as source:
    print('Taking Audio File')
    audio1 = r.record(source)
    print('Done')
    '''The context manager opens the file and reads its contents, storing the data in an AudioFile instance called 
    source. Then the record() method records the data from the entire file into an AudioData instance. '''

try:
    text = r.recognize_google(audio1, language="en-US",show_all=False)
    print('Transcription :' + text)

except Exception as e:
    print(e)
