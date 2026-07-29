from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.7, max_output_tokens=10
)

result = model.invoke("What is the capital of german?")

print(result.content)
