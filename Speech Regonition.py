import speech_recognition as sr
import subprocess
def recognize_speech_from_mic(recognizer, microphone):

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
 sensitivity to ambient noise and record audio
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
        print ("speak now")
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable/unresponsive"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    response = recognize_speech_from_mic(recognizer, mic)
    print (response['transcription'])
    if response['transcription'] == "open email":
        print ("opening...")
        subprocess.run("C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.EXE")
    elif response['transcription'] == "tell James":
        print ("tell him what?")
        response2 = recognize_speech_from_mic(recognizer, mic)
        phrase = response2['transcription']
        subprocess.run(f"pstest \\\\192.168.1.16 msg * Justin says {phrase}")