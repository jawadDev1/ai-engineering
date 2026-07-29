
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


prompt1 = PromptTemplate(
    template="Generate a report on {topic}. the report should not be longer then 10 lines.",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a 5 pointer summary from the following text \n {text} .",
    input_variables=['text']
)


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.5 
)

parser = StrOutputParser()

#  
chain = prompt1 | model | parser | prompt2 | model | parser

# result = chain.invoke({'topic': "anime"})

# print(result)

# print graph of chain
chain.get_graph().print_ascii()