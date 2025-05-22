# This was a Speech-To-Text file created by Hugo in order for users to use a microphone with finding various information

'''
Speech-to-Text Module
---------------------
Handles microphone input and converts speech to normal string of text.

Last Modified: 05/16/2025
'''
import speech_recognition as sr

class SpeechToText:
    '''
    Manages speech-to-text recognition using a background listener.

    Features:
    - Converts microphone input to text separate from main code.
    - Supports a voice command ('stop listening') to terminate recognition.
    - Provides methods to start listening, retrieve recognized text, 
      and check for listening status.

    Logical Usage:
    ```
        from speech_to_text import SpeechToText
        # when button clicked on
            stt = SpeechToText() # create stt instance
            stt.toggle() # starts listening
            while stt.listening(): # repeatedly listen until not listening
                # if button clicked off
                    stt.toggle() # stops listening
                else:
                    text = stt.get_recognized_text()
                    if text:
                        # optional stt.toggle() to turn off
                        # process text
    ```
    Main Components:
    - `toggle()` : toggles on and off speech recognition
    - `listening()` : boolean representing _is_listening state
    - `get_recognized_text()` : Returns user input then resets internals for reuse
    - `start_listening()` : begins capturing audio after adjusting for ambient noise
    - `stop_listening()` : Sets _is_listening to false and stop's listening thread
    
    Requires Speech Recognition API. Pip install command below:
    ```
    pip install SpeechRecognition
    ```
    '''
    def __init__(self):
        self._is_listening = False
        self._recognized_text = None
        self._stop_listening = None

    def toggle(self):
        '''
        Safely toggles the speech recognizer on or off.

        This method manages the recognizer's background listening thread to prevent 
        multiple threads from being started unintentionally.
        '''
        if self._is_listening:
            self.stop_listening()
        else:
            self.start_listening()

    def handle_speech(self, recognizer : sr.Recognizer, audio : sr.AudioData) -> None:
        '''
        Processes captured audio from mic into string.\n
        Calls stop_listening() if 'stop listening' is heard.\n
        Is a callback function for `listen_in_background` method.\n
        '''
        try:
            text = recognizer.recognize_google(audio) # gets text from google API based on audio
            print(f'You said: {text}')
            if 'stop listening' in text.lower():
                self.stop_listening()
            else:
                self._recognized_text = text
        except sr.UnknownValueError:
            print('Could not understand audio. Please Try again')
        except sr.RequestError as e:
            print(f'\nAPI error: {e}\n')
        except:
            print('Unexpected Error')

    def start_listening(self) -> None:
        '''
        Calibrates the microphone and starts background listening.
        '''
        recognizer = sr.Recognizer()
        try:
            mic = sr.Microphone()
            with mic as source:
                print('Calibrating microphone for ambient noise...')
                recognizer.adjust_for_ambient_noise(source, duration=2) # Will automatically adjust for background
                recognizer.energy_threshold *= 0.8 # Reduced to improve accuracy
                print('Calibration complete.')
            
            self._stop_listening = recognizer.listen_in_background(mic, self.handle_speech) # Creates listening thread
            self._is_listening = True
            print('Listening in the background... Say "stop listening" to exit.')
        except IOError:
            print('Mic not found')
            return
    
    def stop_listening(self) -> None:
        '''
        Sets _is_listening to false and stop's listening thread
        '''
        print('Muting mic')
        self._stop_listening(wait_for_stop=False) # _stop_listening waits until wait_for_stop is set to false for background thread to end
        self._is_listening = False

    def get_recognized_text(self) -> str:
        '''
        Returns and clears the last recognized speech text.
        '''
        text = self._recognized_text
        self._recognized_text = None
        return text

    def listening(self) -> bool:
        '''
        Returns whether _is_listening is true, or in other words,\n
        The program is still listening to audio input
        '''
        return self._is_listening

if __name__ == '__main__':
    import time
    stt = SpeechToText()
    stt.start_listening()

    while stt.listening():
        time.sleep(2)
    
    print('Program exited cleanly')