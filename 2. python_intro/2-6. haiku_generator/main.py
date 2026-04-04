""""Assignment
Write a program to create a Haiku, using ai.



A haiku is a type of very short poem that originated in Japan. It has three lines. The first line has 5 syllables, the second has 7 syllables, and the third has 5 syllables again. Haiku usually describe a moment in nature or a feeling, using clear, simple images. Even though it is brief, a good haiku often gives the reader a quiet, thoughtful feeling.



Prompt the user to enter their name, and a topic. Then make use call_gpt to turn the name and topic into a haiku. We leave it up to you to come up with the prompt! Here are some sample runs:



Enter your name: Freya
Enter a topic: Rain in the forest
Creating your haiku...

Freya roams the woods,  
Whispers dance with gentle rain,  
Nature's song remains.



Enter your name: Chris
Enter a topic: a global python classroom
Creating your haiku...

In the global space,  
Chris guides minds through Python's flow,  
Code unites us all.



For this problem you are going to need to use the call_gpt function:

# make a call to gpt and get a response
response = call_gpt("Your prompt here...")


This is optional. Have fun!"""
pip install anthropic
set ANTHROPIC_API_KEY=your_key_here
import anthropic
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[{"role": "user", "content": "your prompt here"}]
)
print(message.content[0].text)


def main():
    # TODO: your code here
    name=input("Enter your name: ")
    topic=input("Enter a topic: ")
    print("Creating your haiku...")
    response=call_gpt(f" turn the {name} and {topic} into a haiku")
    print(response)
    pass


if __name__ == "__main__":
    main()