from collections import defaultdict
import spacy

nlp_en = spacy.load("en_core_web_sm")
nlp_hi = spacy.load("xx_ent_wiki_sm")

intents = {
    "Objectives": [
        "What are the goals of NAMAMI Gange?",
        "Tell me the objectives of NAMAMI Gange.",
        "What is the purpose of the NAMAMI Gange project?",
        "goals of namami gange",
        "goals of namami ganga",
        "ganga project goal"
    ],
    "Impact": [
        "How has NAMAMI Gange impacted the environment?",
        "What is the influence of NAMAMI Gange on the ecosystem?",
        "how namami gange impacted the ganges river, environment and ecosystem?",
        "chacha chaudhary, how namami gange impacted the ganges river, environment and ecosystem?",
        "Chacha ji, What is the influence of NAMAMI Gange on the ecosystem?",
        "Chacha Chaudhary ji, How namami gange has impacted our ecosystem, rivers and environment?"
    ],
    "Contributions": [
        "How can I contribute to NAMAMI Gange?",
        "What actions can I take to support the project?",
        "Ways to support NAMAMI Gange project",
        "Chacha ji how can I support namami gange?",
        "how can people contribute to Namami",
        "how can we all contribute to Namami Gange Project"
        
    ],
    "Key Components": [
        "What are the key components of this project?",
        "What are the major aspects of namami gange?",
        "Chacha ji what are the aspects of this namami gange project?",
        "Tell me the main components/aspects of this ganga/gange program?",
        "Chacha explain us/we/me the major aspects/components of this program."
    ],
    "Features": [
        "What can you do chacha ji",
        "What are your features chacha ji?",
        "What are your MSP Chacha ji?",
        "What are your capabilities?",
        "What are the things you can do chacha ji?",
        "Tell us what can you do",
        "chacha what is your features",
        " what is your feature"
    ],
    "उद्देश्य": [
        "नमामि गंगे के उद्देश्य क्या हैं?",
       "चाचा नमामि गंगे का उद्देश्य क्या है?",
       "नमामि गंगे के उद्देश्य",
       "नमामि गंगे के मुख्य उद्देश्य",
       "नमामि गंगे के प्राथमिक उद्देश्य क्या हैं?",
       "नमामि गंगे के प्राथमिक उद्देश्य क्या हैं?",
       "नमामि गंगे के मुख्य उद्देश्य क्या हैं?",
       "नमामि गंगे के मुख्य उद्देश्य क्या हैं? "
    ],
    "परिचय": [
        "नमस्ते",
        "आप कौन हैं",
        "तुम क्या हो?",
        "मुझे अपने बारे में बताओ",
        

    ],

    "मूल":[
        "नमामि गंगे परियोजना क्या है?",
        "क्या है प्रोजेक्ट नमामि गंगे?",
        "मुझे नमामि गंगे के बारे में बताएं",
        "हमें नमामि गंगे के बारे में बताएं",
        "नमामि गंगे के बारे में जानकारी ",
    ],

    "विशेषता": [
        "मुझे अपनी विशेषताओं के बारे में बताएं",
        "आप हमारी कैसे मदद कर सकते हैं",
        "आप कैसे उपयोगी हो सकते हैं",
        "आप नमामि गंगे के लिए कैसे उपयोगी हो सकते हैं",
        "मुझे अपने एमएसपी के बारे में बताएं",
        "मुझे अपने मुख्य विक्रय बिंदुओं के बारे में बताएं",
        "हमें बताएं कि आप नमामि गंगे परियोजना के लिए कैसे उपयोगी हो सकते हैं",
    ],

    "नमामि गंगे विशेषता": [
        "'नमामि गंगे' की प्रमुख विशेषताएं क्या हैं?"
       
    ],
    
    "प्रभाव": [
        "नमामि गंगे का प्रकृति पर क्या प्रभाव है? "
        
    ],
    "आवश्यकता":[
        "इस परियोजना की क्या आवश्यकता है?",

    ],
    "शुरुआत":[
        "नमामि गंगे की शुरुआत कहाँ से हुई?",
    ],
    "अर्थ":[
        "'नमामि गंगे'नाम का क्या अर्थ है और यह क्या दर्शाता है? "
    ],
    "कदम":[
        "नदी को साफ रखने के लिए मुझे कुछ कदम सुझाएं।",
    ],
    "लक्ष्य":[
        "'नमामि गंगे' परियोजना का प्राथमिक लक्ष्य क्या है?",
    ],
    "समाधान":[
        "गंगा नदी से संबंधित मुद्दों के समाधान के लिए 'नमामि गंगे' को कैसे लागू किया गया है?",

    ],
    "अप्रत्यक्ष":[
        "गंगा में अप्रत्यक्ष रूप से किस प्रकार का कचरा जुड़ता है।",
    ],
    "चुनौतियाँ":[
        "गंगा नदी को पुनर्जीवित करने के प्रयासों में 'नमामि गंगे' परियोजना को किन चुनौतियों और बाधाओं का सामना करना पड़ा है और इसने उनसे कैसे पार पाने की कोशिश की है?",


    ],
}



responses = {
    "Objectives": "The primary objectives of the Namami Gange project are: \n1. To reduce pollution and maintain water quality.\n2. To promote sustainable sanitation practices. \n3. To conserve and rejuvenate the river's biodiversity.\n4. To ensure continuous water flow.\n5. To promote afforestation and wastewater management.",
    "Impact": "the namami gange project has had a significant impact, including:\n1. reduction in pollution levels.\n2. improved water quality.\n3. increased biodiversity.\n4. enhanced riverfront amenities.\n5. promotion of sustainable practices.",
    "Contributions": "You can contribute to the Namami Gange project by:\n1. Practicing responsible waste disposal.\n2. Avoiding the use of single-use plastics.\n3. Supporting local clean-up and awareness initiatives.\n4. Promoting water conservation in your community.\n5. Spreading awareness about the project's goals and achievements.",
    "Key Components": "The key components of the Namami Gange project include:\n1. Sewerage Treatment Plants (STPs) and Effluent Treatment Plants (ETPs).\n2. Riverfront Development.\n3. Afforestation and biodiversity conservation.\n4. Public awareness and community participation.\n5. Industrial pollution control measures.",
    "Features": "Well, I'm Chacha Chaudhary, your interactive river ambassador, and I'm here to make your experience with the Namami Gange Programme truly remarkable!\nHere's what I can do:\n1. Bilingual Brilliance: I can chat with you in both English and Hindi.\n2. Voice Magic: Just talk to me, and I'll respond—it's like having a real conversation.\n3. Mr. Multitasker: I'm multifunctional, whether you want info on Namami Gange or a good laugh.\n4. Voice of Warmth: I use pre-recorded voice responses for a friendly touch.\n5. Naturally Smart: Thanks to AIML, I understand your everyday language.\n6. Touch of Ease: I have a user-friendly touch panel interface.\n7. Interactive Guru: I provide info on Namami Gange, its goals, and its impact.\n8. School Kids' Pal: I love hanging out with school kids and teaching them about our rivers.\n9. Namami Gange Advocate: I'm on a mission to spread the word about Namami Gange.\n10. Low-Maintenance Pro: I'm low-maintenance and here for you anytime.\n11. Offline Superstar: I work even in places with spotty internet.\n12. Your Custom Assistant: I can customize my responses to suit your needs.\nSo, what would you like to explore today?",
    "उद्देश्य":"नमामि गंगे परियोजना के प्राथमिक उद्देश्य हैं:\n1. प्रदूषण को कम करना और पानी की गुणवत्ता बनाए रखना।\n2. स्थायी स्वच्छता प्रथाओं को बढ़ावा देना।\n3. नदी की जैव विविधता का संरक्षण और पुनर्जीवन करना।\n4. निरंतर जल प्रवाह सुनिश्चित करना।\n5. वनीकरण और अपशिष्ट जल प्रबंधन को बढ़ावा देना।",
    "परिचय":"मैं चाचा चौधरी एक आर्टिफिशियल इंटेलिजेंस आधारित इंटरैक्टिव वॉयस और टेक्स्ट सक्षम बॉट हूं, जिसे प्रोजेक्ट नमामि गंगे के बारे में जानकारी देने में आपकी सहायता के लिए बनाया गया है। आज मैं आपकी कैसे सहायता कर सकता हूँ?",
    "मूल":"नमामि गंगे, गंगा नदी को पुनर्जीवित और साफ़ करने के लिए भारत सरकार द्वारा शुरू की गई एक व्यापक परियोजना है।\nइसका उद्देश्य गंगा और उसकी सहायक नदियों के पारिस्थितिक संतुलन और पवित्रता को बहाल करना है।\nयह परियोजना प्रदूषण, अपशिष्ट प्रबंधन और नदी तट विकास सहित विभिन्न मुद्दों के समाधान के लिए शुरू की गई थी।",
    "विशेषता":"खैर, मैं चाचा चौधरी हूं, आपका इंटरैक्टिव नदी राजदूत, और मैं नमामि गंगे कार्यक्रम के साथ आपके अनुभव को वास्तव में उल्लेखनीय बनाने के लिए यहां हूं! यहाँ मैं क्या कर सकता हूँ:\n1. द्विभाषी प्रतिभा: मैं आपसे अंग्रेजी और हिंदी दोनों में चैट कर सकता हूं।\n2. आवाज का जादू: बस मुझसे बात करो, और मैं जवाब दूंगा—यह एक वास्तविक बातचीत करने जैसा है।\n3. मिस्टर मल्टीटास्कर: मैं मल्टीफंक्शनल हूं, चाहे आपको नमामि गंगे के बारे में जानकारी चाहिए या हंसी-मजाक।\n4. गर्मजोशी की आवाज: मैत्रीपूर्ण स्पर्श के लिए मैं पहले से रिकॉर्ड की गई आवाज प्रतिक्रियाओं का उपयोग करता हूं।\n5. स्वाभाविक रूप से स्मार्ट: एआईएमएल को धन्यवाद, मैं आपकी रोजमर्रा की भाषा समझता हूं।\n6. सहजता का स्पर्श: मेरे पास उपयोगकर्ता के अनुकूल टच पैनल इंटरफ़ेस है।\n7. इंटरएक्टिव गुरु: मैं नमामि गंगे, इसके लक्ष्यों और इसके प्रभाव के बारे में जानकारी प्रदान करता हूं।\n8. स्कूली बच्चों का दोस्त: मुझे स्कूली बच्चों के साथ घूमना और उन्हें हमारी नदियों के बारे में पढ़ाना अच्छा लगता है।\n9. नमामि गंगे अधिवक्ता: मैं नमामि गंगे के बारे में प्रचार-प्रसार करने के मिशन पर हूं।\n10. कम-रखरखाव प्रो: मैं कम-रखरखाव वाला हूं और किसी भी समय आपके लिए यहां हूं।\n11. ऑफलाइन सुपरस्टार: मैं खराब इंटरनेट वाली जगहों पर भी काम करता हूं।\n12. आपका कस्टम सहायक: मैं आपकी आवश्यकताओं के अनुरूप अपनी प्रतिक्रियाओं को अनुकूलित कर सकता हूं।\nतो, आज आप क्या जानना चाहेंगे?",
    "नमामि गंगे विशेषता":" 'नमामि गंगे' की प्रमुख विशेषताएं निम्नलिखित हैं:\n1. मलजल उपचार.\n2. औद्योगिक प्रवाह नियंत्रण।\n3. नदी की सतह की सफाई.\n4. जैव विविधता संरक्षण.\n5. जन जागरूकता और सामुदायिक सहभागिता।",
    "प्रभाव":"नमामि गंगे का प्रकृति पर प्रभाव:\n1. पानी की गुणवत्ता में सुधार।\n2. जैव विविधता संरक्षण.\n3. उन्नत तटवर्ती क्षेत्र।\n4. ठोस अपशिष्ट में कमी.",
    "आवश्यकता":"नमामि गंगे परियोजनाओं की आवश्यकता/मकसद निम्नलिखित हैं:\n1. पर्यावरण उन्नयन.\n2. सार्वजनिक स्वास्थ्य संबंधी चिंताएँ।\n3. सांस्कृतिक एवं धार्मिक महत्व।\n4. आर्थिक निहितार्थ और पारिस्थितिक परिणाम।\n5. अंतर्राष्ट्रीय प्रतिबद्धताएँ।\n6. शहरीकरण और औद्योगीकरण",
    "शुरुआत":"गंगा नदी उत्तराखंड, उत्तर प्रदेश, बिहार, झारखंड और पश्चिम बंगाल सहित उत्तरी भारत में क्रमिक संपदा में बहती है। ये राज्य विशेष रूप से उत्तराखंड और उत्तर प्रदेश उन क्षेत्रों में से हैं जहां कार्यक्रमों की प्रारंभिक परियोजनाएं और पहल की गईं।",
    "अर्थ":"'नमामि गंगे' एक संस्कृत वाक्यांश है जिसका अनुवाद मोटे तौर पर 'मैं गंगा को नमन करता हूं' या 'मैं गंगा को प्रणाम \nकरता हूं' के रूप में किया जा सकता है। 'नमामि' संस्कृत क्रिया 'म' से लिया गया है जिसका अर्थ है 'जाना या अर्पित करना' 'नमस्कार' और 'गंगे' का तात्पर्य 'गंगा नदी' से है",
    "कदम":"नदियों को साफ़ रखने के उपाय निम्नलिखित हैं:\n1. नदी के किनारे के समुदायों में एक प्रभावी अपशिष्ट प्रबंधन प्रणाली लागू करें।\n2. कचरे को नदी में जाने से रोकने के लिए उचित अपशिष्ट निपटान और पुनर्चक्रण को बढ़ावा दें।\n3. नदी में कचरा फेंकने से बचें.\n4. नदी में उर्वरक और कीटनाशकों के प्रवाह को कम करने के लिए टिकाऊ कृषि पद्धतियों को बढ़ावा देना।\n5. मिट्टी को स्थिर करने, कटाव को कम करने और वन्यजीवों को आवास प्रदान करने के लिए नदी के किनारे पेड़ और वनस्पति लगाएं। ",
    "लक्ष्य":"'नमामि गंगे' परियोजनाओं के लक्ष्य निम्नलिखित हैं:\n1. पानी की गुणवत्ता में सुधार करें।\n2. पारिस्थितिकी तंत्र को पुनर्स्थापित करें।\n3. सतत उपयोग को बढ़ावा देना।\n4. सांस्कृतिक एवं धार्मिक संरक्षण।\n5. जन जागरूकता",
    "समाधान":" नमामि गंगे परियोजना को विभिन्न रणनीतियों और गतिविधियों के माध्यम से कार्यान्वित किया गया है:\n1. सीवेज उपचार संयंत्र.\n2. औद्योगिक प्रवाह नियंत्रण।\n3. ठोस अपशिष्ट प्रबंधन।\n4. जैव विविधता संरक्षण.\n5. रिवर फ्रंट डेवलपमेंट.\n6. सार्वजनिक जागरूकता और सामुदायिक सहभागिता।",
    "अप्रत्यक्ष":"विभिन्न प्रकार के अपशिष्ट अप्रत्यक्ष रूप से गंगा में प्रवाहित होते हैं। उनमें से कुछ हैं:\n1. कृषि अपवाह.\n2. औद्योगिक अपवाह.\n3. शहरी अपवाह.\n4. निर्माण मलबा.\n5. बिना सीवर वाले क्षेत्रों का सीवेज।",
    "चुनौतियाँ":"कुछ प्रमुख चुनौतियाँ और परियोजना द्वारा उनसे पार पाने के लिए जिन तरीकों की तलाश की गई है उनमें शामिल हैं:\nचुनौतियाँ:\n1. सीवेज प्रदूषण.\n2. औद्योगिक प्रदूषण.\n3. अपशिष्ट प्रबंधन का संकेत दें।\n4. ग्रामीण एवं कृषि अपवाह।\nसमाधान:\n1. हमें उचित सीवेज प्रबंधन पर ध्यान देना होगा।\n2. औद्योगिक अपशिष्ट की निगरानी।\n3. नदी के किनारे सफाई अभियान शुरू करें और जन जागरूकता कार्यक्रम शुरू करें।\n4. किसानों को पर्यावरण-अनुकूल कृषि तकनीकों को लागू करने के लिए प्रोत्साहित करना।",

}

def recognize_intent(user_input, detected_language):
    intent_scores = defaultdict(float)

    if detected_language == "en":
        doc = nlp_en(user_input)
    elif detected_language == "hi":
        doc = nlp_hi(user_input)
    else:
        return None

    for intent, questions in intents.items():
        for question in questions:
            question_doc = nlp_en(question)  
            similarity = doc.similarity(question_doc)
            intent_scores[intent] = max(intent_scores[intent], similarity)

    recognized_intent = max(intent_scores, key=intent_scores.get)
    max_similarity = intent_scores[recognized_intent]

    if max_similarity >= 0.8:
        return recognized_intent
    else:
        return None
