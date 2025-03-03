import os
import getpass

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")
_set_env("OPENAI_API_KEY")

#Chatbot
from langchain_openai import ChatOpenAI

gpt4o_chat = ChatOpenAI(model = "gpt-4o", temperature = 0)
gpt35_chat = ChatOpenAI(model = "gpt-3.5-turbo-0125", temperature = 0)

from langchain_core.messages import HumanMessage

#create a message
msg = HumanMessage(content = "Hello World", name = "Shabnam")

#Message List
messages = [msg]

#Invoke the model with a list of messages
gpt4o_chat.invoke(messages)

gpt4o_chat.invoke("hello world")

gpt35_chat.invoke("hello world")