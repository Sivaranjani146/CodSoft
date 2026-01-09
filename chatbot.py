# CODSOFT - Artificial Intelligence Internship
# Task 1: Rule-Based Chatbot

print("===================================")
print(" Chatbot: Hello! I am a simple chatbot 🤖")
print(" Chatbot: Type 'bye' to exit.")
print("===================================\n")

while True:
    user_input = input("You: ").lower()

    # Greeting
    if user_input == "hi" or user_input == "hello":
        print("Chatbot: Hello! How can I help you?")

    # Asking about chatbot
    elif "how are you" in user_input:
        print("Chatbot: I am doing great! Thanks for asking 😊")

    elif "your name" in user_input:
        print("Chatbot: I am a rule-based chatbot created for CODSOFT Task 1.")

    elif "who created you" in user_input:
        print("Chatbot: I was created by a CODSOFT AI intern using Python.")

    # Help option
    elif "help" in user_input:
        print("Chatbot: I can respond to greetings, my name, and simple questions.")

    # Exit condition
    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a wonderful day 👋")
        break

    # Unknown input
    else:
        print("Chatbot: Sorry, I didn't understand that. Please try again.")
