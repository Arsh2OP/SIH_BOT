import aiml
import speech_recognition as sr
import pyttsx3
import langid

# Initialize AIML kernel
kernel = aiml.Kernel()

# Load AIML files for English
kernel.learn("your_aiml_script_en.aiml")

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine for Hindi
engine_hindi = pyttsx3.init()

# Initialize the text-to-speech engine for English
engine_english = pyttsx3.init()

# Function to get user's spoken input
def get_spoken_input():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio, language="en")
            return user_input.lower()
        except sr.UnknownValueError:
            print("Chatbot: I couldn't understand your voice. Please try again.")
        except sr.RequestError as e:
            print(f"Chatbot: Error with speech recognition: {e}")
        return ""

# Function to get chatbot response in the specified language
def get_chatbot_response(user_input, language="en"):
    if language == "en":
        response = kernel.respond(user_input)
        return response
    elif language == "hi":
        # You would need to implement Hindi responses in AIML or a translation mechanism
        # For demonstration purposes, we'll just echo the input in Hindi.
        return f"आपने कहा: {user_input}"

# Function to make the chatbot speak in the specified language
def speak(text, language="en"):
    if language == "en":
        engine_english.say(text)
        engine_english.runAndWait()
    elif language == "hi":
        engine_hindi.say(text)
        engine_hindi.runAndWait()

if __name__ == "__main__":
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = get_spoken_input()
        
        if user_input == "exit":
            break
        
        if user_input:
            print("You:", user_input)
            
            # Detect the language of the user input using 'langid'
            detected_language, _ = langid.classify(user_input)
            
            response = get_chatbot_response(user_input, detected_language)
            
            if response:
                print(f"Chatbot ({detected_language}):", response)
                speak(response, detected_language)
            else:
                print(f"Chatbot ({detected_language}): I'm sorry, I couldn't understand your request.")
