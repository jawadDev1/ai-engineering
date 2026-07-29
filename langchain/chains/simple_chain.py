
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


prompt = PromptTemplate(
    template="Generate 5 interisting fact about {topic}. each fact should have 1 line max",
    input_variables=['topic']
)


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.5 
)

parser = StrOutputParser()

#  | => Langchain expersion language
chain = prompt | model | parser

# result = chain.invoke({'topic': "anime"})

# print(result)

# print graph of chain
chain.get_graph().print_ascii()