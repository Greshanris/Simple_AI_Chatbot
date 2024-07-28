**AI Simple ChatBot using Ollama LLM**

**Ollama LLM Download Page:** 
[Ollama LLM](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbU1vNkhSQlhJVDJoUU9SQ09hdUpkLVNTbndJZ3xBQ3Jtc0trTm92SXFVQWF2MGRyWC1Jb3FiZTZudjZvZnd0V1l4Qy1Da055bldWQmE0aG9mTm5HdXkwcm1kUlU3NGw0VTFIUmoyYWZIc2p0QVZIOTlNbVVjS1cwNS10OHFtNHFaeGNkeHVPTF82empWSEdHTU56SQ&q=https%3A%2F%2Follama.com%2F&v=d0o89z134CQ)
[GitHub Repo:](https://github.com/ollama/ollama)

**This AI chatbot project is based on the TechwithTim YouTube AI chatbot tutorial for learning purposes**

[TechwithTim](https://www.youtube.com/watch?v=d0o89z134CQ&t=309s)

After installing the LLM (windows):
- create a virtual environment: python3 -m venv chatbot
- Activate the new virtual environment: .\chatbot\scripts\Activate.ps1
- Install required dependencies: pip install langchain langchain-ollama ollama
- The main.py file is the python code that runs on this langchain and ollama3 model 

**main.py**
- It imports ollamaLLM class
- connect to ollama3 model
- create a predefined template
- use this template to create the prompts for the chatbot
- chain the prompt to the connected model
- create conversation_handler that uses user input and LLM to give response and store it in the context
- previous conversations are also stored and based on it, give required response
