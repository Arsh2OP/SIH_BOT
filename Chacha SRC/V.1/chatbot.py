import aiml
import speech_recognition as sr
import pyttsx3
from langid.langid import LanguageIdentifier, model
from googletrans import Translator

kernel = aiml.Kernel()
kernel.learn("English.aiml")
kernel.learn("your_aiml_script_hi.aiml")

recognizer = sr.Recognizer()
engine_hindi = pyttsx3.init()
engine_english = pyttsx3.init()

identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

translator = Translator()

conversation_context = {
    "previous_user_input": "",
    "previous_bot_response": "",
}

def get_spoken_input():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            return user_input.lower()
        except sr.UnknownValueError:
            print("Chacha Chaudhary: I couldn't understand your voice. Please try again.")
        except sr.RequestError as e:
            print(f"Chacha Chaudhary: Error with speech recognition: {e}")
        return ""

def get_chatbot_response(user_input):
    detected_language, _ = identifier.classify(user_input)
    response = kernel.respond(user_input)
    
    
    conversation_context["previous_user_input"] = user_input
    conversation_context["previous_bot_response"] = response
    
    if detected_language == "hi":
        return response, "hi"
    else:
    
        translated_response = translator.translate(response, src="en", dest=detected_language).text
        return translated_response, detected_language


def speak(text, language):
    if language == "en":
        engine_english.say(text)
        engine_english.runAndWait()
    elif language == "hi":
        engine_hindi.say(text)
        engine_hindi.runAndWait()

if __name__ == "__main__":
    print("Chacha Chaudhary: Hello! How can I assist you today?")
    
    while True:
        user_input = get_spoken_input()
        
        if user_input == "exit":
            print("Chacha Chaudhary: Goodbye!")
            break
        
        if user_input:
            print("You:", user_input)
            
            
            user_input_with_context = f"{user_input} <|> {conversation_context['previous_user_input']} <|> {conversation_context['previous_bot_response']}"
            response, response_language = get_chatbot_response(user_input_with_context)
            
            if response_language == "hi":
                print(f"Chacha Chaudhary (Hindi):", response)
                speak(response, "hi")
            elif response_language == "en":
                print(f"Chacha Chaudhary (English):", response)
                speak(response, "en")
            else:
                print(f"Chacha Chaudhary:", response)
