import spacy
from collections import defaultdict
import warnings
warnings.filterwarnings("ignore", message="[W007]", category=UserWarning)
nlp = spacy.load("en_core_web_md")


intents = {
    "Objectives": [
        "What are the goals of NAMAMI Gange?",
        "Tell me the objectives of NAMAMI Gange.",
        "What is the purpose of the NAMAMI Gange project?",
        "goals of namami gange",
        "goals of namami ganga","ganga project goal"
        
    ],
    "Impact": [
        "How has NAMAMI Gange impacted the environment?",
        "What is the influence of NAMAMI Gange on the ecosystem?",
        "how namami gange impacted the ganges river, envornment and ecosystem?",
        "chacha chaudhary, how namami gange impacted the ganges river, envornment and ecosystem?",
        "Chacha ji, What is the influence of NAMAMI Gange on the ecosystem?",
        "Chacha Chaudhary ji, How namami gange has impacted our ecosystem, rivers and envornment?"
        
    ],
    "Contributions": [
        "How can I contribute to NAMAMI Gange?",
        "What actions can I take to support the project?",
        "Ways to support NAMAMI Gange project",
        "Chacha ji how can i support namami gange?"
    ],
    
    "Key Components": [
        "What are the key components of this project?",
        "What are the major aspects of namai gange?",
        "Chacha ji what are the aspects of this namami gange project?",
        "Tell me the main components/aspects of this ganga/gange program?"
        "Chacha explain us/we/me the major aspects/components of this program."
    ],
    
    "Features": [
        "What can you do chacha ji",
        "What are your featurs chacha ji?",
        "What are your MSP Chacha ji?",
        "What are your capability?",
        "What are the things you can do chacha ji?",
        "Tell us what can you do",
        "chacha what is your features",
        " what is your feature"
    ],
    
    
    
}


responses = {
    "Objectives": "The primary objectives of the Namami Gange project are: \n1. To reduce pollution and maintain water quality.\n2. To promote sustainable sanitation practices. \n3. To conserve and rejuvenate the river's biodiversity.\n4. To ensure continuous water flow.\n5. To promote afforestation and wastewater management.",
    "Impact": "the namami gange project has had a significant impact, including:\n1. reduction in pollution levels.\n2. improved water quality.\n3. increased biodiversity.\n4. enhanced riverfront amenities.\n5. promotion of sustainable practices.",
    "Contributions": "You can contribute to the Namami Gange project by:\n1. Practicing responsible waste disposal.\n2. Avoiding the use of single-use plastics.\n3. Supporting local clean-up and awareness initiatives.\n4. Promoting water conservation in your community.\n5. Spreading awareness about the project's goals and achievements.",
    "Key Components":"The key components of the Namami Gange project include:\n1. Sewerage Treatment Plants (STPs) and Effluent Treatment Plants (ETPs).\n2. Riverfront Development.\n3. Afforestation and biodiversity conservation.\n4. Public awareness and community participation.\n5. Industrial pollution control measures.",
    "Features": "Well, I'm Chacha Chaudhary, your interactive river ambassador, and I'm here to make your experience with the Namami Gange Programme truly remarkable!\nHere's what I can do:\n1. Bilingual Brilliance: I can chat with you in both English and Hindi.\n2. Voice Magic: Just talk to me, and I'll respond—it's like having a real conversation.\n3. Mr. Multitasker: I'm multifunctional, whether you want info on Namami Gange or a good laugh.\n4. Voice of Warmth: I use pre-recorded voice responses for a friendly touch.\n5. Naturally Smart: Thanks to AIML, I understand your everyday language.\n6. Touch of Ease: I have a user-friendly touch panel interface.\n7. Interactive Guru: I provide info on Namami Gange, its goals, and its impact.\n8. School Kids' Pal: I love hanging out with school kids and teaching them about our rivers.\n9. Namami Gange Advocate: I'm on a mission to spread the word about Namami Gange.\n10. Low-Maintenance Pro: I'm low-maintenance and here for you anytime.\n11. Offline Superstar: I work even in places with spotty internet.\n12. Your Custom Assistant: I can customize my responses to suit your needs.\nSo, what would you like to explore today? "
}

def recognize_intent(user_input):
    intent_scores = defaultdict(float)

    user_input_doc = nlp(user_input)

    for intent, questions in intents.items():
        for question in questions:
            question_doc = nlp(question)
            similarity = user_input_doc.similarity(question_doc)
            intent_scores[intent] = max(intent_scores[intent], similarity)


    recognized_intent = max(intent_scores, key=intent_scores.get)
    max_similarity = intent_scores[recognized_intent]

    if max_similarity >= 0.8:
        return recognized_intent
    else:
        return None
