import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*The model you're using has no word vectors loaded.*")
warnings.filterwarnings("ignore", category=UserWarning, message=".*Evaluating Doc.similarity based on empty vectors.*")
import spacy


nlp_en = spacy.load("en_core_web_sm")
nlp_hi = spacy.load("xx_ent_wiki_sm")

intents = {
    "Objectives": {
        "en": [
            "What are the goals of NAMAMI Gange?",
            "Tell me the objectives of NAMAMI Gange.",
            "What is the purpose of the NAMAMI Gange project?",
            "goals of namami gange",
            "goals of namami ganga",
            "ganga project goal"
        ],
        "hi": [
            "नमामि गंगे के उद्देश्य क्या हैं?",
            "चाचा नमामि गंगे का उद्देश्य क्या है?",
            "नमामि गंगे के उद्देश्य",
            "नमामि गंगे के मुख्य उद्देश्य",
            "नमामि गंगे के प्राथमिक उद्देश्य क्या हैं?",
            "नमामि गंगे के प्राथमिक उद्देश्य क्या हैं?",
            "नमामि गंगे के मुख्य उद्देश्य क्या हैं?",
            "नमामि गंगे के मुख्य उद्देश्य क्या हैं? "
        ],
    },
    "Impact": {
        "en": [
            "How has NAMAMI Gange impacted the environment?",
            "What is the influence of NAMAMI Gange on the ecosystem?",
        ],
        "hi": [
            "नमामि गंगे का प्रकृति पर प्रभाव क्या है?",
            "नमामि गंगे के पारिस्थितिकी पर क्या प्रभाव होता है?",
            "नमामि गंगे का प्रकृति पर प्रभाव?",
        ],
    },
}

responses = {
    "Objectives": {
        "en": "The primary objectives of the Namami Gange project are: ...",
        "hi": "नमामि गंगे' परियोजनाओं के लक्ष्य निम्नलिखित हैं: ...",
    },
    "Impact": {
        "en": "The namami gange project has had a significant impact, including: ...",
        "hi": "नमामि गंगे का प्रकृति पर प्रभाव:\n1. पानी की गुणवत्ता में सुधार।\n2. जैव विविधता संरक्षण.\n3. उन्नत तटवर्ती क्षेत्र।\n4. ठोस अपशिष्ट में कमी.",
    },
}

def recognize_intent(user_input, detected_language):
    intent_scores = {}
    if detected_language not in ["en", "hi"]:
        return None

    user_input_doc = nlp_en(user_input) if detected_language == "en" else nlp_hi(user_input)

    for intent, questions in intents.items():
        intent_scores[intent] = 0

        for lang, question_list in questions.items():
            for question in question_list:
                question_doc = nlp_en(question) if lang == "en" else nlp_hi(question)
                similarity = user_input_doc.similarity(question_doc)
                intent_scores[intent] = max(intent_scores[intent], similarity)

    recognized_intent = max(intent_scores, key=intent_scores.get)
    max_similarity = intent_scores[recognized_intent]

    if max_similarity >= 0.8:
        return recognized_intent  # Return the recognized intent name as a string
    else:
        return None
