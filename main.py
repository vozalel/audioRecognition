# This functions get audio from url, and recognition audio to string format
import speech_recognition as sr
import urllib.request

url = 'https://psv4.userapi.com/c618531//u24561657/audiomsg/d3/9235519b70.mp3'
r = sr.Recognizer()

def recognize_text_from_audio(audio):
    try:
        return r.recognize_google(audio)
    except Exception as e:
        return e.__str__()


def recognition(url: str) -> str:
    audio = urllib.request.urlopen(url).read()
    return recognize_text_from_audio(audio)

print (recognition(url))