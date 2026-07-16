from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()
liked = []

while True:
    ans = input("Name a movie/show that you like: (Exit: 0)")

    if ans == "0":
        break

    liked.append(ans)


class Movies(BaseModel):
    title: str
    genre: str
    rating: int
    release_year: int
    story: str


response = client.responses.parse(
    model="gpt-5.5",
    input=f"""

The user likes these movies and TV shows:

{liked}

Recommend one show they will probably enjoy.

""",
    text_format=Movies
)

movie = response.output_parsed
print(movie.title)
print(movie.genre)
print(movie.rating)
print(movie.release_year)
print(movie.story)
