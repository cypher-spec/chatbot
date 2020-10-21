# May 2020 model
# prerequisites - pip install -U chatterbox & pip install -U chaterbox_corpus

# imports and variables
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as s_r
# use list trainer if needed - this was from the base program files
# from chatterbot.trainers import ListTrainer
chat_end = True
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1)

# chatbot name - does not appear anywhere else but the code
chatbot = ChatBot('HUESC')

# model training - multiple trainers not possible therefore only one language at the time is possible
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('I would like to book a flight.')


while chat_end == True:

    # user response is logged here and looped once kona responds
    #request = input('User: ')

    with my_mic as source:
        #print("Say now!!!!")
        r.adjust_for_ambient_noise(source) #reduce noise
        audio = r.listen(source) #take voice input from the microphone
    request  = r.recognize_google(audio) #to print voice into text
    print('User: '+ request)
    # this breaks the loop and quits the chat
    if request == ("bye"):
        print("HUESC: Goodbye Sir.")
        break
    

    # added this in to check if kona could be made to answer specific questions
    if request == ("name ?", "what is your name", "identity"):
        print("HUESC: i am HUESC")

    # konas response
    else:
        response = chatbot.get_response(request)
        print('HUESC: ', response)

