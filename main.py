import nltk
from nltk.chat.util import Chat, reflections
import random
import requests
from datetime import datetime


# Recommendations lists
books = [
    "To Kill a Mockingbird by Harper Lee", "1984 by George Orwell", "Pride and Prejudice by Jane Austen",
    "The Great Gatsby by F. Scott Fitzgerald", "Moby-Dick by Herman Melville"
]
movies = [
    "Inception", "The Shaw shank Redemption", "The Godfather", "The Dark Knight", "Forrest Gump"
]
songs = [
    "Bohemian Rhapsody by Queen", "Hotel California by Eagles", "Stairway to Heaven by Led Zeppelin",
    "Imagine by John Lennon", "Hey Jude by The Beatles"
]

# Define a comprehensive set of pairs for daily life and routine interactions
pairs = [
    # Greetings
    (r"hi|hey|hello", ["Hello!", "Hey there!", "Hi, how can I help you today?", "Greetings!"]),

    # Asking the bot's name
    (r"what is your name?", ["I am a chatbot created using NLTK.", "You can call me Chatbot."]),

    # Asking how the bot is doing
    (r"how are you?|how r u|what are you doing", ["I'm just a bunch of code, but I'm functioning as expected!",
                                                  "I'm doing great, thank you!"]),

    # Asking what are you doing
    (r"what are you doing|where are you busy", ["I am having talk with you"]),

    # showing excites
    (r"wow|great|nice", ["Thank you!","Than you for appreciation","Yeah!"]),

    # Expressing gratitude
    (r"thank you|thanks", ["You're welcome!", "No problem!", "Glad I could help!", "Anytime!"]),

    # Saying goodbye
    (r"bye|goodbye|see you", ["Goodbye! Have a nice day!", "See you later!", "Take care!"]),

    # Asking for a joke
    (r"tell me a joke", ["Why don’t scientists trust atoms? Because they make up everything!",
                         "Why did the math book look sad? Because it had too many problems.",
                         "Why don’t some couples go to the gym? Because some relationships don’t work out."]),

    # Asking for the time
    (r"what time is it?|what is time|time now|time", ["It's currently {time}.", "The time is {time}.",
                                                      "Right now, it's {time}."]),

    # Asking for the date
    (r"what is date today?|what is date|date now|date", ["Today's date is {date}.", "It's {date} today.",
                                                         "The date is {date}."]),

    # Asking for news
    (r"what's the news today?|any news?|what is the news today", ["You can check the latest news at your preferred news"
                                                                  " website.","I'm not connected to a news service right now, but you can find news quit"
                                                                              "on various platforms."]),

    # Asking for the bot's location
    (r"where are you?|what's your location?", ["I'm a virtual assistant, so I don't have a physical location.",
                                               "I exist in the digital world, accessible from anywhere!"]),

    # Asking about the bot's hobbies
    (r"what are your hobbies?",
     ["I like helping people with their queries!", "My hobby is chatting with users like you."]),

    # Asking who created the bot
    (r"who created you?|who is your creator?", ["I was created by a developer using Python and NLTK.",
                                                "A developer programmed me to assist with various tasks."]),

    # Asking for a motivational quote
    (r"give me a quote|motivate me", [
        "Believe in yourself and all that you are. Know that there is something inside you"
        " that is greater than any obstacle.",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. "
        "If you love what you are doing, you will be successful."]),

    # Asking for a fact
    (r"tell me a fact", [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over "
        "3,000 years old and still edible.",
        "Bananas are berries, but strawberries aren't.",
        "A day on Venus is longer than a year on Venus."]),

    # Asking about the bot's age
    (r"how old are you?",
     ["I was created recently, so I am quite young!", "Age is just a number, especially for a bot like me."]),

    # Asking for a recommendation
    (r"recommend me a (book|movie|song)",
     ["You should try reading {book}.", "How about watching {movie}?", "Listen to {song}, it's a classic!"]),

    # Asking for advice
    (r"can you give me advice?", ["Sure, always stay positive and keep learning new things.",
                                  "Remember to take breaks and take care of your mental health."]),

    # Asking for the bot's purpose
    (r"what do you do?|what's your purpose?",
     ["I'm here to assist you with information and tasks.", "My purpose is to help you with any queries you have."]),

    # Asking for the meaning of life
    (r"what is the meaning of life?",
     ["The meaning of life is a philosophical question that has been debated for centuries.",
      "42 is often cited as the answer to the ultimate question of life, the universe, and everything, "
      "according to Douglas Adams."]),

    # Asking for fun facts
    (r"tell me a fun fact", ["Octopuses have three hearts.", "Butterflies taste with their feet.",
                             "A group of flamingos is called a 'flamboyance'."]),

    # Fallback response
    (r"(.*)", ["I'm not sure I understand. Can you please rephrase?", "Sorry, I didn't get that."])
]


# Function to get current time
def get_current_time():
    return datetime.now().strftime("%H:%M")


# Function to get current date
def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")


# Function to replace placeholders in responses
def replace_placeholders(response, user_input):
    if "{time}" in response:
        return response.format(time=get_current_time())
    elif "{date}" in response:
        return response.format(date=get_current_date())
    elif "{book}" in response:
        return response.format(book=random.choice(books))
    elif "{movie}" in response:
        return response.format(movie=random.choice(movies))
    elif "{song}" in response:
        return response.format(song=random.choice(songs))
    return response


# Custom response function to handle placeholder replacements
def custom_response(user_input, pairs):
    for pattern, responses in pairs:
        if nltk.re.search(pattern, user_input):
            response = random.choice(responses)
            return replace_placeholders(response, user_input)
    return "I'm not sure I understand. Can you please rephrase?"


# Define the Chat class
class CustomChat(Chat):
    def respond(self, user_input):
        return custom_response(user_input, self._pairs)


# Create a chatbot instance
chatbot = CustomChat(pairs, reflections)


def run_chatbot():
    print("Hi! I am a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! Have a nice day!")
            break

        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    run_chatbot()
