# AI Movie & TV Show Recommender

A Python application that uses the OpenAI Responses API to recommend movies or TV shows based on a user's favorite titles.

## About

This project collects a list of movies and TV shows that the user enjoys and uses an LLM to recommend a new title with similar themes, genres, or storytelling styles.

The recommendation is returned as a structured Python object using Pydantic, making the response easy to work with in code.

## Features

- Accepts multiple favorite movies and TV shows as user input.
- Uses the OpenAI Responses API to generate personalized recommendations.
- Returns structured data using Pydantic.
- Displays:
  - Title
  - Genre
  - IMDb Rating
  - Language
  - Release Date
  - Story/Synopsis

## Technologies Used

- Python
- OpenAI Python SDK
- Pydantic

## How It Works

1. The user enters movies or TV shows they like.
2. The program stores the user's favorites in a list.
3. The list is sent to the OpenAI API.
4. The model analyzes the user's preferences.
5. A recommendation is returned in a structured format.
6. The program displays the recommendation to the user.

## Example

### User Input

```text
Breaking Bad
Interstellar
The Dark Knight
0
```

### Example Output

```text
Title: True Detective

Genre: Crime, Drama, Mystery

IMDb Rating: 8.9

Language: English

Release Date: January 12, 2014

Story:
Season one follows two detectives investigating a series of ritualistic murders in Louisiana while uncovering a much larger mystery spanning decades.
```

## Concepts Learned

- OpenAI Responses API
- Prompt Engineering
- Structured Outputs
- Pydantic Models
- User Input Handling
- Data Validation
- Python Lists

## Future Improvements

- Recommend multiple movies instead of one.
- Allow users to choose between movies and TV shows.
- Filter recommendations by genre, language, or release year.
- Save user preferences for future recommendations.
- Add a graphical user interface.
- Integrate a real movie database (e.g., TMDb or OMDb) for posters and additional information.

## Author

Karam Alnajjar