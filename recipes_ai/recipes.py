from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()


class Recipe(BaseModel):
    name: str
    ingredients: list[str]
    minutes_to_cook: int


response = client.responses.parse(
    model="gpt-5.5",
    input="give me a recipe for butter chicken",
    text_format=Recipe
)

recipe = response.output_parsed
print(recipe.name)
print(recipe.ingredients)
print(f"minutes: recipe.minutes_to_cook")
