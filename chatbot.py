def chatbot():
    print("Hello I am the super chatbot. How can I help you today?.  You can ask me anything")
    print("Type 'exit' to know me you are leaving")
    while True:
        user=input("You: ").lower()
        if user=='exit':
            print("Chatbot: Ok I think you are about to leave Bye!.  Thanks for the conversation.")
        elif user in['hi','hello','hey','hey chat']:
            print("Chatbot: Hello there! How can I help you?")
        elif "Your name" in user:
            pirnt("Chatbot: I'm a super chatbot created to help you. So ask me anything")
        elif "help" in user:
            print("Chatbot: I can respond to greetings, questions about me, and do simple queries")
        elif "birds" in user:
            print("""Rare birds are unique and often critically endangered species found in isolated or shrinking habitats around the world.
One such bird is the Kakapo, a large, flightless, nocturnal parrot from New Zealand that is known for its owl-like face and critically low population.
The Philippine Eagle, also called the monkey-eating eagle, is one of the largest and most powerful eagles, found only in the Philippines, and is under severe threat due to deforestation.
In Madagascar, the Madagascar Pochard, a diving duck once thought extinct, was rediscovered and remains one of the rarest ducks globally.
India is home to the elusive Forest Owlet, a small owl that vanished for over a century before being rediscovered in 1997.
The Northern Bald Ibis, with its bald head and curved beak, is another striking bird, once widespread but now surviving only due to dedicated conservation efforts.
Meanwhile, the Yellow-eyed Penguin of New Zealand stands out with its pale yellow eyes and shy nature, and is one of the rarest penguin species in the world.
These birds not only highlight the beauty of biodiversity but also emphasize the urgent need for conservation to protect Earth's most vulnerable species.""")
        elif "bye" in user:
            print("Chatbot: Bye! It was nice to have chat with you")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand what you ask me. Try again something else")

if __name__=="__main__":
    chatbot()
