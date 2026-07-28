
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.7 
)

st.header("Research Tool")
# user_input = st.text_input('Enter your prompt')

paper_input = st.selectbox("Select Research Paper name", ["Select...", "Attention is All You Need", "GPT-3: Language Models are Few-Shot Learners"])
style_input = st.selectbox("Select Explaination Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length_input = st.selectbox("Select Explaination Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explianation)"])

research_prompt_template = """
    Please summarize the research paper "{paper_input}" with the following specifications:
    Explaination style: {style_input}
    Explaination length: {length_input}
    1. Mathematcial Details:
        - Include relavent mathematical equations if present in the paper,
        - Explain the mathematical concepts using simple, intuitive code snippets where applicable
    2. Analogies:
        - Use relateable analogies to simplify complex ideas.
    If certain information is not available in paper, respond with "Insufficient information available" instead of guessing.
    Ensure the summary is clear, accurate, and aligned with the provided style and length.
"""

template = PromptTemplate(
    template=research_prompt_template,
    input_variables=['paper_input', "style_input", "length_input"]
)

# fill the placeholders
prompt = template.invoke({
    'paper_input': paper_input, 
    "style_input": style_input, 
    "length_input": length_input
})

if st.button("Summarize"):
    try:
        if prompt:
            result = model.invoke(prompt)
            st.write(result.content)
        else:
            st.write("Invalid input")
    except Exception as e:
        st.exception(e) 
        # st.write(e)
        print("Error in model invoke:: ", e)

