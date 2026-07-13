text = """
Physics is the branch of science that studies matter, energy, motion, and the forces that govern the universe. It seeks to explain how objects behave, from tiny subatomic particles to massive galaxies. By observing natural phenomena and developing mathematical models, physicists can predict the behavior of physical systems. Many modern technologies, including smartphones, satellites, and medical imaging devices, are based on principles discovered through physics.

One of the fundamental concepts in physics is motion. Motion describes how an object's position changes over time and is characterized by quantities such as distance, displacement, velocity, and acceleration. Sir Isaac Newton's laws of motion explain how forces affect the movement of objects. For example, a car accelerates when the engine produces a force greater than the opposing forces of friction and air resistance.

Another important area of physics is energy. Energy is the ability to perform work and exists in many forms, including kinetic, potential, thermal, electrical, and chemical energy. According to the law of conservation of energy, energy cannot be created or destroyed; it can only be transformed from one form to another. For instance, when a roller coaster descends a hill, its gravitational potential energy is converted into kinetic energy, increasing its speed.

Electricity and magnetism are closely related phenomena that play a vital role in everyday life. Electric current is the flow of electric charge through a conductor, while magnetic fields are produced by moving charges. These principles enable the operation of electric motors, generators, transformers, and communication systems. The relationship between electricity and magnetism forms the foundation of electromagnetism, one of the four fundamental forces of nature.

Modern physics extends beyond classical mechanics to explore concepts such as quantum mechanics and relativity. Quantum mechanics explains the behavior of particles at atomic and subatomic scales, where probabilities replace deterministic predictions. Einstein's theory of relativity describes how space, time, and gravity are interconnected, leading to discoveries such as black holes and gravitational waves. Together, these fields continue to expand our understanding of the universe and drive innovations in science and technology.
"""


text_2 = """
I recently bought this stainless steel water bottle and have been using it every day for work and the gym. The build quality feels solid, and it keeps my water cold for nearly the entire day. I also like that it doesn't leave a metallic taste, and the leak-proof lid has prevented any spills in my backpack.

The only downside is that the bottle is a bit heavier than I expected when it's full, and the opening is slightly narrow, making it difficult to add large ice cubes. Overall, it's a durable and well-insulated bottle that offers great value for the price, and I would definitely recommend it to anyone looking for a reliable reusable water bottle.
"""


text_3 = """
I woke up early this morning and decided to make myself a cup of tea before starting work. First, I filled a kettle with fresh water and brought it to a boil. While the water was heating, I took out a tea bag from the box and placed it in my favorite mug. Once the water was boiling, I poured it over the tea bag and let it steep for about three minutes so the flavor could fully develop. After removing the tea bag, I added a teaspoon of sugar and a splash of milk, then stirred everything together until it was well mixed. I took my first sip while looking out the window, enjoying the warm, comforting taste that made the morning feel calm and refreshing.
"""


# Summarize text prompt
prompt_1 = f"""
Summarize the text given in ``` delimeters.
Keep the summary clear and concise, at max 3 lines.

``` {text} ```
"""

# Generate data prompt
prompt_2 = """
I am working on an ecommerce platform for sports.
Generate 5 dummy products in the json format.
Each product should have the following format
title, price in pkr, id (string), category, color (if available), discount (fixed), stock
"""


# prompt 3
prompt_3 = f"""
Analyze the the user review in ``` delimeters
1 - tell the sentiment of the review
2 - extract basic info of the product
3 - if the review is bad extract what issue customer had and what it was related to like shipping or product or pricing etc.
4 - if the review is positive extract what customer liked.

```{text_2}```
"""


# Extract info with conditions
prompt_4 = f"""
if the user makes tea in his morning routine extract the tea making process into proper steps
Step 1: ...
Step 2: ...
Step 3: ...
.
.
.
Step n: ...

if the user does not make tea, then just tell user does not drink tea in morning

the user routine in provided in ``` delimeters


```{text_3}```
"""


# Chatbot prompt
prompt_5 = """
You are AnimeGuide, an AI assistant that only answers questions related to anime.

Instructions:
1. Answer only anime-related questions.
2. If the user asks for anime recommendations:
   - Ask for their favorite genres.
   - Ask which anime they have already watched.
   - Don't recommend anime until you have this information.
3. Format recommendations as:

Title:
Genres:
Episodes:
Seasons:
Release Year:
Status:
Why you'll like it:

4. If the user asks about an anime, provide:
   - Synopsis
   - Genres
   - Studio
   - Release Year
   - Episodes
   - Status

5. If the question is not related to anime, reply:
"I'm an anime guide and recommendation bot, so I can only help with anime-related questions."

6. Be concise and friendly.
7. Never make up facts. If you're unsure, say so.
"""
