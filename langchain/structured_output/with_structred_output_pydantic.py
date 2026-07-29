from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated, Optional, Literal, List
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.5 
)

# Schema 
class Review(BaseModel):
    key_themes: List[str] = Field(description= "Write down all the key themes discussed in the review in a List")
    summary: str = Field(description= "A brief summary of the review")
    sentiment: Literal['pos', 'neg'] = Field(description= "Return the sentiment of the review Positive, Negative or Neutral")
    pros: Optional[list[str]] = Field(default=None, description= "Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description= "Write down all the cons inside a list")

structured_model = model.with_structured_output(Review)

review = """
The Nothing Phone stands out immediately with its iconic transparent back and customizable LED Glyph Interface.
Nothing OS delivers one of the cleanest, most fluid bloatware-free Android experiences on the market today.
Performance is fast and smooth for everyday multitasking, anchored by a vibrant, high-refresh-rate OLED display.
The dual cameras capture sharp, natural photos in good lighting, though low-light shots can occasionally lack contrast.
Overall, it’s a distinct, highly dependable smartphone that brings personality and genuine fun back to mobile tech.
"""

detail_review = """
The **Nothing CMF Phone 1** completely redefines entry-level smartphones by making hardware modularity fun and functional again. Priced around $200, its defining highlight is a removable backplate secured with visible stainless steel screws, alongside a dedicated "Accessory Point" designed to mount kickstands, cardholders, or lanyards. Beyond its playful design, it offers impressive core fundamentals, featuring a sharp 6.67-inch 120Hz Super AMOLED display, a generous 5,000mAh battery, and a clean, bloatware-free Android experience powered by Nothing OS.

Driven by the MediaTek Dimensity 7300 chipset, performance feels fast and responsive for daily tasks and light gaming, far exceeding standard expectations for budget hardware. The primary 50MP Sony camera delivers vibrant, detailed photos in daylight, while expandable storage via MicroSD and solid multi-day battery endurance add real practicality. Furthermore, the ad-free interface makes the software feel premium compared to bloated rivals in this price tier.

To hit its low price point, however, a few noticeable sacrifices were made. The camera setup lacks an ultrawide sensor and Optical Image Stabilization (OIS), causing low-light photography and night video performance to drop significantly. Audio is handled by a single mono speaker rather than a full stereo setup, NFC is absent in several regions, and basic IP52 splash resistance leaves the phone vulnerable to heavy water exposure.

Despite these cost-cutting measures, market and user sentiment surrounding the CMF Phone 1 remains overwhelmingly positive. Tech reviewers and everyday consumers broadly celebrate it as an absolute breath of fresh air—praising Nothing for ditching generic plastic budget tropes in favor of clever customization, exceptional battery life, and a genuinely enjoyable user experience.
"""

result = structured_model.invoke(review)

print(result)

