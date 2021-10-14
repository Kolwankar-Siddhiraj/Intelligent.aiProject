import speech_recognition as sr 
from gtts import gTTS 
from playsound import playsound
from fpdf import FPDF
import pyttsx3
import datetime
from interviwe_details_text import interview_in_text
# import random
# import os
# import requests
# import subprocess
# import traceback
# import threading 
# import difflib 

print("Execution stared !")

engine=pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('volume',1)

my_microphone = sr.Microphone()
obj_recognition = sr.Recognizer()

# all #gobal variables 
candidate_response = []
asked_questions = []
candidate_answers = []
question_list = ["What Type of Language C is?", "What are Functions in C?", 
                "When C Programming was invented", "Who Developed C Programming Language"]
answer_list = ["1974","Dennis Ritchie", "it is Structured and Procedural Programming Language", 
                "A function is a block of code that performs a specific task,The function contains the set of programming statements enclosed by {}. A function can be called multiple times to provide reusability and modularity to the C program. In other words, we can say that the collection of functions creates a program. The function is also known as procedureor subroutinein other programming languages."]
use_mic_again = True
add_line = interview_in_text("interviwe_text.txt")


# name = str(input("Enter your name :: "))


def use_mic():
    # global use_mic_again
    with my_microphone as source:
        try:
            print("Mic is active !")
            #voice_input = obj_recognition.listen(source, timeout=3)
            voice_input = obj_recognition.listen(source)
            
            try:
                voice_message = obj_recognition.recognize_google(voice_input)
            except Exception as error:
                print("Something went wrong...!", error)
                use_speaker("Sorry Could not recognize your voice. Please speak again.")
                #gobal use_mic_again
                
                # if use_mic_again:
                #     use_mic_again = False
                #     voice_message = use_mic()
                # else:
                #     use_speaker("Fine. Let's move on to next question.")
        
        except Exception as error:
            print("Something went wrong..!", error)
            use_speaker("Sorry Could not recognize your voice. Please speak again.")
            #gobal use_mic_again
            
            # if use_mic_again:
            #     use_mic_again = False
            #     voice_message = use_mic()
            # else:
            #     use_speaker("Fine. Let's move on to next question.")

    print("Mic is closed !")
    return voice_message


def use_speaker(speak_message):
    #gobal use_mic_again
    #use_mic_again = True
    print("Speaker is active !")
    engine.say(speak_message)
    engine.runAndWait()
    print("Speaker is closed !")


def technical_questions():
    for question in question_list:
        use_speaker(question)
        add_line.add_sentence("Interviwer", question)
        can_response = use_mic()
        candidate_response.append(can_response)
        add_line.add_sentence("Candidate ", can_response)
        asked_questions.append(question)
        candidate_answers.append(can_response)

# interviwe started 
name = str(input("Enter your name :: "))

use_speaker(f"Hello {name}")
add_line.add_sentence("Interviwer", f"Hello {name}")

can_response = use_mic()
candidate_response.append(can_response)
add_line.add_sentence("Candidate ", can_response)

currentTime = datetime.datetime.now()
if currentTime.hour < 12:
    use_speaker("Good morning")
    add_line.add_sentence("Interviwer", "Good morning")
elif 12 <= currentTime.hour < 18:
    use_speaker("Good afternoon")
    add_line.add_sentence("Interviwer", "Good afternoon")
else:
    use_speaker("Good evening")
    add_line.add_sentence("Interviwer", "Good evening")

can_response = use_mic()
candidate_response.append(can_response)
add_line.add_sentence("Candidate ", can_response)

# start asking technical questions
technical_questions()






print("candidate responses :: ", candidate_response)
print("asked questions :: ", asked_questions)
print("candidate answers :: ", candidate_answers)


print("Execution ended !")


