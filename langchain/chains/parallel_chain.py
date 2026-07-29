
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()


prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text} the notes should not be longer then 10 lines.",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate  5 short question answers from the following text \n {text} .",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes ->  {notes} and quiz -> {quiz} .",
    input_variables=['notes', 'quiz']
)


groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-8b-instant")


parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model | parser, 
    'quiz': prompt2 | model | parser, 
})

merge_chain = prompt3 | model | parser 

chain = parallel_chain | merge_chain

text = """
Anime, short for animation in Japan, has evolved from a niche regional craft into a massive global cultural phenomenon. Its roots trace back to the early 20th century, but the medium truly found its modern identity in the 1960s under the influence of pioneers like **Osamu Tezuka**, often called the "God of Manga." Tezuka adapted cinematic framing, sequential visual storytelling, and distinctive character designs to overcome budget constraints, laying the groundwork for a distinct art form that prioritizes atmosphere, emotional depth, and intricate character development over simple slapstick comedy.

Unlike many Western animation traditions that historically targeted younger audiences, anime spans an extraordinary dynamic range of genres and demographics. Content is tailored to specific age groups and interests, categorized into styles like **Shonen** (action and adventure aimed at young males), **Shojo** (romance and character-driven drama for young females), **Seinen** (complex narratives for adult men), and **Josei** (slice-of-life and mature drama for adult women). This classification framework allows creators to tackle heavy philosophical themes, psychological thrillers, fantastical adventures, and grounded human relationships with equal gravity.

Visually, anime is defined by its expressive aesthetic choices and cinematic pacing. Character designs frequently feature large, expressive eyes that convey subtle emotional nuance, stylized hair, and deliberate color symbolism. Animators intentionally balance limited frame rates with dynamic camera angles, dramatic lighting, and dramatic visual pauses to build tension. Directors like **Hayao Miyazaki** of Studio Ghibli have elevated this technique to fine art, capturing quiet, breathtaking moments of realism alongside sweeping, hand-drawn fantasy landscapes.

The global expansion of anime accelerated in the late 20th century through iconic television broadcasts of shows like *Dragon Ball*, *Sailor Moon*, and *Pokemon*, before reaching unprecedented heights in the digital streaming era. Platforms dedicated to anime have made simultaneous worldwide releases the industry standard, fostering a massive international fan community. Today, anime influences global fashion, video games, contemporary music, and Hollywood filmmaking, driven by active fan engagement through cosplay, conventions, and digital media sharing.

As technology evolves, the anime industry continues to blend classic hand-drawn techniques with sophisticated computer-generated imagery (CGI). Studios seamlessly incorporate digital backgrounds and 3D modeling into classic 2D animation, enabling more fluid action sequences and complex visual effects. anime remains a vibrant canvas for artistic innovation, continually pushing storytelling boundaries while cementing its place as one of the world's most influential forms of popular media.
"""

# result = chain.invoke({'text': text})

# print(result)

# print graph of chain
chain.get_graph().print_ascii()