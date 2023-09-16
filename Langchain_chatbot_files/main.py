'''AUDIO FEATURE ENABLED!

import langchain
from langchain.chat_models import ChatOpenAI  
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
import streamlit as st
from streamlit_chat import message
from utils import *

# scheduler
import schedule
import time
import os

def main():

  st.subheader("Welcome to Kanayo Justice Chatbot with Langchain, ChatGPT, Pinecone, and Streamlit project")

  # Initialize buffer_memory if not present in session_state
  if 'buffer_memory' not in st.session_state:
      st.session_state['buffer_memory'] = ConversationBufferWindowMemory(k=3, return_messages=True)

  if 'responses' not in st.session_state:
      st.session_state['responses'] = ["How can I assist you?"]

  if 'requests' not in st.session_state:
      st.session_state['requests'] = []

  llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key="")

  system_msg_template = SystemMessagePromptTemplate.from_template(template="""Answer the question as truthfully as possible using the provided context,
  and if the answer is not contained within the text below, say 'I don't know'""")

  human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

  prompt_template = ChatPromptTemplate.from_messages([system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])

  conversation = ConversationChain(memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)

  # container for chat history
  response_container = st.container()

  # container for text box
  textcontainer = st.container()

  # Add a checkbox to control audio playback
  play_audio = st.checkbox("Play Audio Response", value=True)

  with textcontainer:
      query = st.text_input("Query: ", key="input")
      if query:
          with st.spinner("typing..."):
              conversation_string = get_conversation_string()
              refined_query = query_refiner(conversation_string, query)
              st.subheader("Refined Query:")
              st.write(refined_query)
              context = find_match(refined_query)

              response_text = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")

              # Convert response to audio
              response_audio = gTTS(response_text, lang='en') 

              st.write("Bot Response:")
              st.write(response_text)

              temp_audio_file = f"temp_audio.mp3"
              response_audio.save(temp_audio_file)

              if play_audio:
                  st.audio(temp_audio_file, format='audio/mpeg')

          st.session_state.requests.append(query)
          st.session_state.responses.append(response_text)

  with response_container:
      if st.session_state['responses']:
          for i in range(len(st.session_state['responses'])):
              message(st.session_state['responses'][i], key=str(i))  
              if i < len(st.session_state['requests']):
                  message(st.session_state["requests"][i], is_user=True, key=str(i) + '_user')

if __name__ == "__main__":
    main() 
'''

# AUDIO FEATURE ENABLED!

import langchain
from langchain.chat_models import ChatOpenAI  
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
import streamlit as st
from streamlit_chat import message
from utils import *

# scheduler
import schedule
import time
import os

def main():

  st.subheader("Welcome to Kanayo Justice Chatbot with Langchain, ChatGPT, Pinecone, and Streamlit project")

  # Initialize buffer_memory if not present in session_state
  if 'buffer_memory' not in st.session_state:
      st.session_state['buffer_memory'] = ConversationBufferWindowMemory(k=3, return_messages=True)

  if 'responses' not in st.session_state:
      st.session_state['responses'] = ["How can I assist you?"]

  if 'requests' not in st.session_state:
      st.session_state['requests'] = []

  llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)

  system_msg_template = SystemMessagePromptTemplate.from_template(template="""Answer the question as truthfully as possible using the provided context,
  and if the answer is not contained within the text below, say 'I don't know'""")

  human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

  prompt_template = ChatPromptTemplate.from_messages([system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])

  conversation = ConversationChain(memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)

  # container for chat history
  response_container = st.container()

  # container for text box
  textcontainer = st.container()

  # Add a checkbox to control audio playback
  play_audio = st.checkbox("Play Audio Response", value=True)

  with textcontainer:
      query = st.text_input("Query: ", key="input")
      if query:
          with st.spinner("typing..."):
              conversation_string = get_conversation_string()
              refined_query = query_refiner(conversation_string, query)
              st.subheader("Refined Query:")
              st.write(refined_query)
              context = find_match(refined_query)

              response_text = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")

              # Convert response to audio
              response_audio = gTTS(response_text, lang='en') 

              st.write("Bot Response:")
              st.write(response_text)

              temp_audio_file = f"temp_audio.mp3"
              response_audio.save(temp_audio_file)

              if play_audio:
                  st.audio(temp_audio_file, format='audio/mpeg')

          st.session_state.requests.append(query)
          st.session_state.responses.append(response_text)

  with response_container:
      if st.session_state['responses']:
          for i in range(len(st.session_state['responses'])):
              message(st.session_state['responses'][i], key=str(i))  
              if i < len(st.session_state['requests']):
                  message(st.session_state["requests"][i], is_user=True, key=str(i) + '_user')

if __name__ == "__main__":
    main()
