import speech_recognition as sr
import pyttsx3
import logging
from datetime import datetime
from typing import Dict, List

# Setup logging
logging.basicConfig(
    filename='sales_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class VoiceSalesBot:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Adjust speech rate
        self.recognizer = sr.Recognizer()
        self.conversation_history: List[Dict] = []
        
        # Enhanced response system
        self.responses = {
            "price": "Our premium plan starts at 499 rupees only. Would you like to know more?",
            "features": "You get AI automation, 24/7 customer support, and real-time analytics dashboard.",
            "trial": "Yes, we offer a free 7-day trial with full access to all features.",
            "buy": "Excellent choice! Visit our website at example.com or I can email you a link.",
            "support": "Our support team is available 24/7. You can reach us via chat or phone.",
            "default": "Can you please tell me more about what you need?"
        }
        
        self.keywords = {
            "price": ["price", "cost", "expensive", "cheap", "afford"],
            "features": ["features", "service", "include", "provide", "what do you"],
            "trial": ["trial", "demo", "free", "test"],
            "buy": ["buy", "purchase", "subscribe", "sign up", "order"],
            "support": ["support", "help", "contact", "issue", "problem"]
        }

    def speak(self, text: str):
        """Text-to-speech with logging"""
        print(f"Bot: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        logging.info(f"Bot response: {text}")

    def listen(self, timeout: int = 10) -> str:
        """Listen with timeout and better error handling"""
        try:
            with sr.Microphone() as source:
                print("Listening... (speak now)")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout)
            
            user_text = self.recognizer.recognize_google(audio)
            logging.info(f"User said: {user_text}")
            return user_text
            
        except sr.UnknownValueError:
            logging.warning("Could not understand audio")
            self.speak("Sorry, I couldn't quite catch that. Could you repeat?")
            return ""
        except sr.RequestError as e:
            logging.error(f"API error: {e}")
            self.speak("I'm having trouble connecting to the service. Please try again.")
            return ""
        except sr.Timeout:
            self.speak("I didn't hear anything. Please speak up.")
            return ""

    def get_intent(self, user_text: str) -> str:
        """Improved intent detection"""
        user_text = user_text.lower()
        
        # Check for matches
        for intent, keywords in self.keywords.items():
            if any(keyword in user_text for keyword in keywords):
                return intent
        
        return "default"

    def get_response(self, intent: str) -> str:
        """Get appropriate response"""
        return self.responses.get(intent, self.responses["default"])

    def run(self):
        """Main conversation loop"""
        self.speak("Hello! I am your AI sales assistant. How can I help you today?")
        
        conversation_count = 0
        max_turns = 10  # Limit conversation length
        
        while conversation_count < max_turns:
            user_text = self.listen()
            
            if not user_text:
                continue
            
            print(f"You: {user_text}")
            
            # Check for exit phrases
            if any(word in user_text.lower() for word in ["exit", "bye", "quit", "goodbye"]):
                self.speak("Thank you for visiting. Have a great day!")
                logging.info("Conversation ended by user")
                break
            
            # Get and deliver response
            intent = self.get_intent(user_text)
            response = self.get_response(intent)
            self.speak(response)
            
            # Track conversation
            self.conversation_history.append({
                "user": user_text,
                "intent": intent,
                "response": response
            })
            
            conversation_count += 1
        
        logging.info(f"Session ended after {conversation_count} turns")

if __name__ == "__main__":
    bot = VoiceSalesBot()
    bot.run()
