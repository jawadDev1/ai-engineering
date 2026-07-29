from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser 
from pydantic import BaseModel, Field 
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda


load_dotenv()


groq_api_key = os.getenv("GROQ_API_KEY")


model = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-8b-instant")


class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative']  = Field(description="Give the sentiment of the feedback.")


parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="classify the sentiment of the following feedback text into positive, negative  \n {feedback} \n {format_instruction} .",
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write an appropiate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Write an appropiate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)


classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")  # default chain required
)

chain = classifier_chain  | branch_chain

# result = chain.invoke({'feedback': "this is a amazing phone"})

# print(result)


chain.get_graph().print_ascii()