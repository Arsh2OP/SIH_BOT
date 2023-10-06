import aiml
import os

AIML_EN_DIRECTORY = "aiml_en"
AIML_HI_DIRECTORY = "aiml_hi"

def initialize_aiml():
    english_kernel = aiml.Kernel()
    hindi_kernel = aiml.Kernel()
    english_kernel.learn(os.path.join(AIML_EN_DIRECTORY, "English.aiml"))
    hindi_kernel.learn(os.path.join(AIML_HI_DIRECTORY, "Hindi.aiml"))
    english_kernel.respond("LOAD AIML B")
    hindi_kernel.respond("LOAD AIML B")
    return english_kernel, hindi_kernel

def respond_to_user_input(user_input_text, english_kernel, hindi_kernel, detected_language):
    aiml_kernel = english_kernel if detected_language == "en" else hindi_kernel
    response = aiml_kernel.respond(user_input_text)
    return response
