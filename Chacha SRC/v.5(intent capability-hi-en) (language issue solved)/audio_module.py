import os
import pygame

RESPONSES_DIRECTORY = "responses"


response_audio_mapping = {
        "hi there! i am chacha chaudhary. i am here to assist you about namami gange": "hi.mp3",
        "hello there! i am chacha chaudhary. i am here to assist you about namami gange": "hello.mp3",
        "namashkar! i am chacha chaudhary. i am here to assist you about namami gange": "namashkar.mp3",
        "namaste! i am chacha chaudhary. i am here to assist you about namami gange": "namaste.mp3",
        "i am chacha chaudhary an aiml based interactive voice and text enabled bot created to assist you with information about project namami gange. how can i assist you today?": "i_am_chacha_chaudhary.mp3",
        "i am chacha chaudhary created to assist you with information about namami gange. how can i assist you today?": "hello.mp3",
        "i was created by shravind singh, khushi garg, preeti upadhyay, ritesh upadhyay and manish gupta.": "Creators.mp3",
        "as a chatbot, i don't have personal preferences, but i can recommend some great movies if you'd like.": "no_preference.mp3",
        "i'm not able to provide detailed movie information at the moment. please specify the movie title, and i'll do my best to give you a brief overview.": "movie_audio.mp3",
        "i don't have personal preferences, but i'm here to help you with any questions or tasks you have.": "no_preference.mp3",
        "i don't age as humans do; i'm a digital creation here to assist you.": "age.mp3",
        "namami gange is a comprehensive project initiated by the indian government to rejuvenate and clean the ganges river. it aims to restore the ecological balance and sanctity of the ganges and its tributaries. the project was launched to address various issues, including pollution, waste management, and riverfront development.": "what_is_namami.mp3",
        "the primary objectives of the namami gange project are:\n1. to reduce pollution and maintain water quality.\n2. to promote sustainable sanitation practices.\n3. to conserve and rejuvenate the river's biodiversity.\n4. to ensure continuous water flow.\n5. to promote afforestation and wastewater management.": "objectives.mp3",
        "the namami gange project has had a significant impact, including:\n1. reduction in pollution levels.\n2. improved water quality.\n3. increased biodiversity.\n4. enhanced riverfront amenities.\n5. promotion of sustainable practices.": "impact.mp3",
        "you can contribute to the namami gange project by:\n1. practicing responsible waste disposal.\n2. avoiding the use of single-use plastics.\n3. supporting local clean-up and awareness initiatives.\n4. promoting water conservation in your community.\n5. spreading awareness about the project's goals and achievements.": "contribution.mp3",
        "i'm sorry, i don't have information on that topic. please feel free to ask me anything else related to namami gange or its objectives.": "no_response.mp3",
        "bilingual brilliance: \"well, folks, i'm not just a one-language wonder! i can chat with you in both english and hindi, making sure everyone feels right at home. voice magic: no need to type away—just talk to me! i'm all ears and ready to assist you with the power of voice. it's like having a real conversation. mr. multitasker: i'm not your average bot—i wear many hats! whether you want info on namami gange or just a good laugh, i've got you covered. voice of warmth: to make our talks even cozier, i've added pre-recorded voice responses. it's like chatting with a friendly neighbor over the fence. naturally smart: don't worry about speaking 'computerese.' i understand your everyday language, thanks to aiml. it's like talking to an old friend. touch of ease: navigating with me is a breeze! i've got this cool touch panel interface that even a child can use. it's super user-friendly. interactive guru: i'm your info buddy! i can tell you all about namami gange, its goals, and the impact it's making. knowledge is power! school kids' pal: calling all young explorers! i love hanging out with school kids and teaching them about our rivers. let's learn together! namami gange advocate: i'm on a mission to spread the word about namami gange. together, we can make a difference for our rivers and the environment. low-maintenance pro: i'm not high-maintenance; i'm here for you anytime. no constant updates needed—I'm good to go with my aiml knowledge. offline superstar: even in places with spotty internet, i shine. i don't need real-time data, so you can count on me anytime, anywhere. your custom assistant: i'm flexible! if you want to chat about something specific, just let me know. i can customize my responses to suit your needs.\"": "msp.mp3",
        "ladies and gentlemen, i'm chacha chaudhary, your solution to elevate the namami gange programme engagement. listen closely to our innovation:\n\ndigital ambassador: seamlessly converse in english and hindi, thanks to ai, ml, and chatbot expertise.\nintuitive interface: explore effortlessly with a user-friendly touch panel.\nvoice interaction: simply talk, and i'll respond with a friendly voice.\npersonalized responses: my warm voice enhances your personalized experience.\nedu-tainment: learn while you laugh with informative content and humor.\nobjective amplification: i spread awareness and environmental responsibility.\naccessibility: designed for everyone, from school children to policymakers.\nreliability: i shine in low-internet areas, operating offline.\nflexibility: tailor my knowledge to your namami gange queries.\nenvironmental advocacy: join me in supporting afforestation and water conservation.": "solution.mp3",
        "the key components of the namami gange project include:\n1. sewerage treatment plants (stps) and effluent treatment plants (etps).\n2. riverfront development.\n3. afforestation and biodiversity conservation.\n4. public awareness and community participation.\n5. industrial pollution control measures.": "key_components.mp3",
        "नमामि गंगे का प्रकृति पर प्रभाव:\n1. पानी की गुणवत्ता में सुधार।\n2. जैव विविधता संरक्षण.\n3. उन्नत तटवर्ती क्षेत्र।\n4. ठोस अपशिष्ट में कमी.":"impact.mp3",

    }

def initialize_audio():
    pygame.mixer.init()
    pygame.mixer.set_num_channels(1)

def play_audio(response_text):
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

def cleanup_audio():
    pygame.mixer.quit()


