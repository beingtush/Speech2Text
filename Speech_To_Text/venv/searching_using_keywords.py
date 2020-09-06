import os
import time
import winsound
import speech_recognition as sr


print(" Starting iteration")
print("Clearing device logs and will start to collect New logs")
time.sleep(3)

path = 'C:\\Users\\tushar.raj01\\Downloads\\Speech_To_Text\\Speech_To_Text\\audio_files'
song_list = os.listdir(path) #Giving path for all the audio files.

val = input("Enter keyword: ")

r = sr.Recognizer()

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
            print(song)
    except Exception as e:
        print(e)
