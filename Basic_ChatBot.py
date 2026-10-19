print("----------Welcome to the ChatBot!----------")
def Chatbot():
    print("")
    while True:
        msg=str(input()).lower()
        if msg == "hello":
            print("Hi!")
        elif msg ==  "how are you":
            print("I'm fine, thanks!")
        elif msg == "bye":
            print("Goodbye!")
        else:
            print("Sorry, I don't understand.")

        if msg.lower() == "stop":
            print("Loop stopped!")
            break

Chatbot()