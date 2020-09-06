# Here we have written the code to convert speech to text
import speech_recognition as sr

'''speech_recognition is a library for performing speech recognition, before using this please install this using pip 
install SpeechRecognition '''
import pyttsx3  # pyttsx3 is a text-to-speech conversion library in Python, it also works offline. Before using it
# install using pip install pyttsx3

r = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
'''The Recognizer instance is used to recognize speech'''


def speakText(command):  # Function to speak the text said by user.
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while 1:
    try:
        with sr.Microphone() as source2:  # uses the default microphone as the audio source
            r.adjust_for_ambient_noise(source2)  # listens for 1 second to calibrate the energy
            # threshold for ambient noise levels and to reduce noise
            audio2 = r.listen(source2)  # listens for the first phrase and extract it into audio data

            MyText = r.recognize_google(audio2)  # recognizes speech using Google Speech Recognition
            MyText = MyText.lower()  # Coverts the recognized text into lowercase

            print(MyText)  # Prints the text
            speakText(MyText)  # Speaks back the text

    except LookupError:  # Exception when audio is not recognized
        print("Could not understand audio")

    except sr.UnknownValueError:  # Exception for Unknown Values
        print("Did not get you, Try Again! ")
