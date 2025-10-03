# Advanced Rule-Based Chatbot using if-else

import datetime

def chatbot():
    print("Chatbot: Hello! I'm your smart chatbot. Type 'bye' anytime to exit.")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if "bye" in user_input or "exit" in user_input or "quit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Greetings
        elif any(greet in user_input for greet in ["hi", "hello", "hey"]):
            print("Chatbot: Hi there! How can I help you today?")

        # Time-based greeting
        elif "good morning" in user_input:
            print("Chatbot: Good morning! Hope you have a productive day ahead.")
        elif "good afternoon" in user_input:
            print("Chatbot: Good afternoon! How’s your day going?")
        elif "good night" in user_input:
            print("Chatbot: Good night! Sweet dreams :)")

        # Name-related
        elif "your name" in user_input:
            print("Chatbot: I'm Chatbot, your simple assistant built using Python.")

        # How are you
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing fine! How about you?")

        # Weather related
        elif "weather" in user_input:
            print("Chatbot: I can’t check the weather, but I hope it's sunny where you are!")

        # Age
        elif "how old are you" in user_input or "your age" in user_input:
            print("Chatbot: I was created recently, so you can say I'm quite young!")

        # Date & time
        elif "time" in user_input:
            now = datetime.datetime.now()
            print("Chatbot: Current time is:", now.strftime("%H:%M:%S"))
        elif "date" in user_input:
            today = datetime.date.today()
            print("Chatbot: Today's date is:", today.strftime("%B %d, %Y"))

        # Hobbies
        elif "hobby" in user_input or "do for fun" in user_input:
            print("Chatbot: I love chatting with humans and learning new responses!")

        # Default response
        else:
            print("Chatbot: Sorry, I don’t understand that. Can you try asking differently?")

# Run chatbot
chatbot()
