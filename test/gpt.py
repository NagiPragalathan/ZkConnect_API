import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define a function to interact with the chatbot
def chat_with_bot(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    if len(response.choices) > 0:
        return response.choices[0].text.strip()
    return "Sorry, I didn't understand that."

# Chat with the bot
while True:
    user_input = input("User: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    bot_response = chat_with_bot(user_input)
    print("Chatbot:", bot_response)
