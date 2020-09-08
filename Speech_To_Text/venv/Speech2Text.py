import speech_recognition as sr
import os
import time
import winsound

'''speech_recognition is a library for performing speech recognition, before using this please install this using pip 
install SpeechRecognition '''
import pyttsx3  # pyttsx3 is a text-to-speech conversion library in Python, it also works offline. Before using it


# install using pip install pyttsx3


def recognize_speech_from_mic():
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
                print("Speak !")
                r.adjust_for_ambient_noise(source2)  # listens for 1 second to calibrate the energy
                # threshold for ambient noise levels and to reduce noise
                audio2 = r.listen(source2)  # listens for the first phrase and extract it into audio data

                my_text = r.recognize_google(audio2)  # recognizes speech using Google Speech Recognition
                my_text = my_text.lower()  # Coverts the recognized text into lowercase

                print(my_text)  # Prints the text
                speakText(my_text)  # Speaks back the text

        except LookupError:  # Exception when audio is not recognized
            print('Sorry, Could Not Understand. Repeat again.')
            speakText('Sorry, Could Not Understand. Repeat again.')

        except sr.UnknownValueError:  # Exception for Unknown Values
            print('Sorry, Could Not Understand. Repeat again.')
            speakText('Sorry, Could Not Understand. Repeat again.')


def recognize_speech_from_audio():
    r = sr.Recognizer()
    '''The Recognizer instance is used to recognize speech'''
    a_name = input("Enter the name of your audio file along with the file extension. Eg : abc.wav\n ")

    audio1 = 'C:\\Users\\tushar.raj01\\Downloads\\Speech_To_Text\\Speech_To_Text\\audio_files\\'+a_name

    with sr.AudioFile(audio1) as source:
        print('Taking Audio File')
        audio1 = r.record(source)
        print('Done')
        '''The context manager opens the file and reads its contents, storing the data in an AudioFile instance called 
        source. Then the record() method records the data from the entire file into an AudioData instance. '''

    try:
        text = r.recognize_google(audio1, language="en-US", show_all=False)
        print('Transcription :' + text)

    except Exception as e:
        print(e)


def search_keyword():
    def speakText(command):  # Function to speak the text said by user.
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
    print(" Starting iteration")
    print("Clearing device logs and will start to collect New logs")
    time.sleep(3)

    path = 'C:\\Users\\tushar.raj01\\Downloads\\Speech_To_Text\\Speech_To_Text\\audio_files'
    song_list = os.listdir(path)  # Giving path for all the audio files.

    val = input("Enter keyword you want to search in audio file : ")

    r = sr.Recognizer()
    print("Please wait....!!!!! We are searching for the text in audio files. 👀 ")
    for song in song_list:
        time.sleep(10)

        time.sleep(3)

        audio02 = 'C:\\Users\\tushar.raj01\\Downloads\\Speech_To_Text\\Speech_To_Text\\audio_files\\' + song
        with sr.AudioFile(audio02) as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio1 = r.record(source)
        try:
            text = r.recognize_google(audio1)
            if text.__contains__(val):  # Checks for the specified text in the song list.
                print('The text is in '+song)
        except Exception as e:
            print("Oops..!! The given keyword is not available in the provided audio files")
            speakText("Oops..!! The given keyword is not available in the provided audio files")


class Speech2Text:
    name = input("What is your name?\n")
    print("Hi " + name)
    print("What would you like to do?\n"
          "\033[93m\033[1m1. Convert speech to text using your Microphone.\n"
          "2. Ingest an Audio file to convert it into text.\n"
          "3. Search for specific keyword in Audio Files.\033[0m \033[0m \n"
          "Note : For option 2 and 3 put all your audio files inside the \033[93maudio_files\033[0m folder inside the "
          "\033[93mSpeech_To_Text\033[0m folder.")
    choice = input()

    if choice == '1':
        recognize_speech_from_mic()
    elif choice == '2':
        recognize_speech_from_audio()
    elif choice == '3':
        search_keyword()
    else:
        print('Wrong Choice!')
