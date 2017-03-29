import fresh_tomatoes
import media

"""Stores details of movies and displays them on a website."""

toy_story = media.Movie("Toy Story", "Boy and toys.", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

""" Stores the Movie objects in a list. """
movies = [toy_story, avatar]

"""Opens the movie website in the user's browser; features the movies above."""
fresh_tomatoes.open_movies_page(movies)
