import aiml
import speech_recognition as sr
import os
import pygame
import langid


AIML_EN_DIRECTORY = "aiml_en"
AIML_HI_DIRECTORY = "aiml_hi"
RESPONSES_DIRECTORY = "responses"


response_audio_mapping = {
    "hi there! i am chacha chaudhary. i am here to assist you about namami gange": "hello.mp3",
    "i am chacha chaudhary created to assist you with information about namami gange. how can i assist you today?": "hello.mp3",
    "i was created by shravind singh, khushi garg, preeti upadhyay, ritesh upadhyay and manish gupta.": "Creators.mp3",
    "i'm sorry, i don't have access to real-time weather data for [1]. you can check a weather website or app for the current conditions.": "weather_audio.mp3",
    "i don't have access to real-time clock information. you can check the time on your device.": "time_audio.mp3",
    "today's date is <system><date/></system>.": "date_audio.mp3",
    "why did the chicken cross the road? to get to the other side!": "joke_audio.mp3",
    "of course! here's a joke: knock, knock. who's there? boo. boo who? don't cry; it's just a joke!": "joke_audio.mp3",
    "as a chatbot, i don't have personal preferences, but i can recommend some great movies if you'd like.": "no_preference.mp3",
    "i'm not able to provide detailed movie information at the moment. please specify the movie title, and i'll do my best to give you a brief overview.": "movie_audio.mp3",
    "the current president of the united states is joe biden.": "president_audio.mp3",
    "there are seven continents on earth: africa, antarctica, asia, europe, north america, australia (oceania), and south america.": "continents_audio.mp3",
    "i exist in the digital world and don't have a physical location.": "location_audio.mp3",
    "i don't have personal preferences, but i'm here to help you with any questions or tasks you have.": "no_preference.mp3",
    "i don't age as humans do; i'm a digital creation here to assist you.": "age.mp3",
    "shravind singh": "daddy_audio.mp3",
    "goodbye! if you have more questions in the future, feel free to return.": "goodbye_audio.mp3",
    "namami gange is a comprehensive project initiated by the indian government to rejuvenate and clean the ganges river. it aims to restore the ecological balance and sanctity of the ganges and its tributaries. the project was launched to address various issues, including pollution, waste management, and riverfront development.": "namami_gange_audio.mp3",
    "the primary objectives of the namami gange project are:\n1. to reduce pollution and maintain water quality.\n2. to promote sustainable sanitation practices.\n3. to conserve and rejuvenate the river's biodiversity.\n4. to ensure continuous water flow.\n5. to promote afforestation and wastewater management.": "objectives_audio.mp3",
    "the namami gange project has had a significant impact, including:\n1. reduction in pollution levels.\n2. improved water quality.\n3. increased biodiversity.\n4. enhanced riverfront amenities.\n5. promotion of sustainable practices.": "impact.mp3",
    "you can contribute to the namami gange project by:\n1. practicing responsible waste disposal.\n2. avoiding the use of single-use plastics.\n3. supporting local clean-up and awareness initiatives.\n4. promoting water conservation in your community.\n5. spreading awareness about the project's goals and achievements.": "contribution.mp3",
    "i'm sorry, i don't have information on that topic. please feel free to ask me anything else related to namami gange or its objectives.": "no_response.mp3",
    "bilingual brilliance: \"well, folks, i'm not just a one-language wonder! i can chat with you in both english and hindi, making sure everyone feels right at home. voice magic: no need to type away—just talk to me! i'm all ears and ready to assist you with the power of voice. it's like having a real conversation. mr. multitasker: i'm not your average bot—i wear many hats! whether you want info on namami gange or just a good laugh, i've got you covered. voice of warmth: to make our talks even cozier, i've added pre-recorded voice responses. it's like chatting with a friendly neighbor over the fence. naturally smart: don't worry about speaking 'computerese.' i understand your everyday language, thanks to aiml. it's like talking to an old friend. touch of ease: navigating with me is a breeze! i've got this cool touch panel interface that even a child can use. it's super user-friendly. interactive guru: i'm your info buddy! i can tell you all about namami gange, its goals, and the impact it's making. knowledge is power! school kids' pal: calling all young explorers! i love hanging out with school kids and teaching them about our rivers. let's learn together! namami gange advocate: i'm on a mission to spread the word about namami gange. together, we can make a difference for our rivers and the environment. low-maintenance pro: i'm not high-maintenance; i'm here for you anytime. no constant updates needed—I'm good to go with my aiml knowledge. offline superstar: even in places with spotty internet, i shine. i don't need real-time data, so you can count on me anytime, anywhere. your custom assistant: i'm flexible! if you want to chat about something specific, just let me know. i can customize my responses to suit your needs.\"": "main_selling_points.mp3"
    
}

def initialize_aiml():
    
    english_kernel = aiml.Kernel()
    hindi_kernel = aiml.Kernel()
    english_kernel.learn(os.path.join(AIML_EN_DIRECTORY, "English.aiml"))
    hindi_kernel.learn(os.path.join(AIML_HI_DIRECTORY, "Hindi.aiml"))
    english_kernel.respond("LOAD AIML B")
    hindi_kernel.respond("LOAD AIML B")
    return english_kernel, hindi_kernel

def initialize_audio():
    
    pygame.mixer.init()
    pygame.mixer.set_num_channels(1)  

def play_response(response_text):
    best_match = None
    max_match_length = 0

    for key, audio_file in response_audio_mapping.items():
        match_length = len(set(response_text.lower().split()) & set(key.lower().split()))
        if match_length > max_match_length:
            max_match_length = match_length
            best_match = audio_file

    if best_match:
        response_file = os.path.join(RESPONSES_DIRECTORY, best_match)
        if os.path.exists(response_file):
            pygame.mixer.music.load(response_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
        else:
            print(f"Response file '{best_match}' not found.")
    else:
        print(f"No audio file mapping found for response: '{response_text}'")

def get_user_input(recognizer):
    
    with sr.Microphone() as source:
        print("Listening...")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            user_input = recognizer.recognize_google(audio, language="hi-IN")
            print("You (Voice):", user_input)
            return user_input.lower()
        except sr.WaitTimeoutError:
            print("You didn't provide any input.")
            return ""
        except sr.UnknownValueError:
            print("I couldn't understand your voice. Please try again.")
            return ""
        except sr.RequestError as e:
            print(f"Error with speech recognition: {e}")
            return ""

def detect_input_language(user_input):
    
    detected_language, _ = langid.classify(user_input)
    return detected_language

def handle_user_input(user_input, english_kernel, hindi_kernel):
    detected_language = detect_input_language(user_input)
    
    
    aiml_kernel = english_kernel if detected_language == "en" else hindi_kernel
    
    
    if user_input == "exit":
        print("Goodbye!")
        return False

    
    response = aiml_kernel.respond(user_input)

    if response:
        print(f"Chacha Chaudhary (AIML - {detected_language}): {response}")
        
        play_response(response)
    else:
        print("I couldn't understand your request.")

    return True

def cleanup():
    
    pygame.mixer.quit()

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    english_kernel, hindi_kernel = initialize_aiml()
    initialize_audio()

    
    input_method = input("Choose input method ('voice' or 'text'): ")
    
    if input_method.lower() not in ["voice", "text"]:
        print("Invalid input method. Please choose 'voice' or 'text'.")
    else:
        print("Hello, I am your bilingual AIML bot with prerecorded voice responses.")
        
        while True:
            user_input = get_user_input(recognizer) if input_method == "voice" else input("You (Text): ")

            if not handle_user_input(user_input, english_kernel, hindi_kernel):
                break

        cleanup()
