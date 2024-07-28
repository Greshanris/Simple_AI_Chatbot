# To interact with ollama, we import ollamaLLM(class)
from langchain_ollama import OllamaLLM
# Complicate script on how we can pass some context to the model, how we can make this a more user-friendly, and have a full chat user-interface to interact with
# Langchaing is something that allows us to interact with LLMs easily
from langchain_core.prompts import ChatPromptTemplate

# And one of the thing we can do is to create a template that will pass to the LLM that contains our special query or prompt
# This way we can give some descriptions and instructions what it should do
# So, Here we are giving a template for how it should behave or respond to queries
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Here, we can connect ollama, and specify the model we want to work with
model = OllamaLLM(model="llama3")

# Now, we have a model, so we will create some prompts
prompt = ChatPromptTemplate.from_template(template)
# Now, we have a prompt that follows the templare, next thing to do is to chain them together using langchain
chain = prompt | model # | is pipe operator. what this will do is create a chain of these two operation

# All that's great, but we want to continually talk to the model, and store the history
# let's first define a function that handles the conversation
def handle_conversation():
    context = ""
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        # Now, we can use this model, to use this, we can use model.invoke, and then pass the prompt to act upon (here input = str)
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)
        # store all the information on context so that the bot has conversation history and respond previous things that has been said
        context = f"\nUser: {user_input}\nAI: {result}"

# Now, all that needed is to call the function
# This means that we are directly executing this python file
if __name__== "__main__":
    handle_conversation()