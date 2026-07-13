# AI Recipe Generator
A small Python project exploring OpenAI's Structured Outputs feature using the OpenAI Responses API and Pydantic.
## About
This project uses an LLM to generate recipes and return the response in a structured format instead of plain text.
The goal of this project was to learn how to make AI responses more reliable and easier to use inside Python applications.
## Technologies Used
- Python
- OpenAI Python SDK
- Pydantic
## How It Works
1. A prompt is sent to the OpenAI model requesting a recipe.
2. A Pydantic model defines the structure of the expected response.
3. The AI returns the recipe in the required format.
4. The response is automatically parsed into a Python object.
## Example
Input:

Give me a sample recipe for scrambled eggs

Output:
```json
{
  "name": "Scrambled Eggs",
  "ingredients": [
    "3 eggs",
    "butter",
    "salt",
    "pepper"
  ],
  "minutes_to_cook": 5
}

Concepts Learned

* OpenAI Responses API
* Structured Outputs
* Pydantic models
* Data validation
* Converting AI responses into usable Python objects

Code Example

class Recipe(BaseModel):
    name: str
    ingredients: list[str]
    minutes_to_cook: int

The model is guided to return data matching this structure, allowing the program to reliably access:

recipe.name
recipe.ingredients
recipe.minutes_to_cook

Future Improvements

Possible improvements:

* Add a user interface
* Allow users to specify available ingredients
* Generate recipes based on dietary preferences
* Connect to a recipe database
* Add image generation for recipes

Author

Karam Alnajjar