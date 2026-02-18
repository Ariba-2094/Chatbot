#streamlit + langchain + ollama(LLM- gemma2:2b model)\
#import required libraries

import os
import streamlit as st
#imports python built in os module 
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#step1:Create prompt template
#this define how AI should behave and how it receives user input

prompt = ChatPromptTemplate.from_messages(
    [
        #system message defines AI behaviour
        ("system","you are a helpful assistant. please respond clearly to the question asked"),
        #user message contains placeholder {question}

        ("user", "Question : {question}")
    ]
)

#Step 2: Streamlit App UI

#App title
st.title("langchain demo with gemma model(Ollama)")


#text input box for user question
input_text= st.text_input("What question do you have in your mind?")

#step 3: Load ollama model 

#load local gemma model
llm = Ollama(model="gemma2:2b")

#condition : convert output model to string
Output_parser= StrOutputParser()

#create langchain piplene(prompt--> model--> output_parser)
chain= prompt| llm |Output_parser

#step 4: run the model where inputs the question
if input_text:
    response=chain.invoke({"question":input_text})
    st.write(response)
