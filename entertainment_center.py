import fresh_tomatoes
import media

"""Stores details of movies and displays them on a website."""

good_will_hunting = media.Movie("Good Will Hunting", "An unrecognized genius confronts his past and future.",
                        "https://upload.wikimedia.org/wikipedia/id/6/69/Good_Will_Hunting_film.jpg",
                        "https://www.youtube.com/watch?v=QSMvyuEeIyw")


django_unchained = media.Movie("Django Unchained", "A slave and eccentric bounty hunter's " +
                        "journey to rescue the slave's wife from a vicious plantation owner.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=eUdM9vrCbow")

sing_street = media.Movie("Sing Street", "A high school boy starts a band to impress a girl in 1980s Ireland.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEzODA3MDcxMl5BMl5BanBnXkFtZTgwODgxNDk3NzE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=C_YqJ_aimkM")

the_usual_suspects = media.Movie("The Usual Suspects", "Five conmen are brought together for one last job.",
                        "http://www.impawards.com/1995/posters/usual_suspects_ver2.jpg",
                        "https://www.youtube.com/watch?v=oiXdPolca5w")

wreck_it_ralph = media.Movie("Wreck It Ralph", "An arcade villain rebels against his role and embraces his dream of being a hero.",
                        "http://vignette3.wikia.nocookie.net/disney/images/4/4b/Ralphnew002.jpeg/revision/latest?cb=20140317004919",
                        "https://www.youtube.com/watch?v=87E6N7ToCxs")

my_cousin_vinny = media.Movie("My Cousin Vinny", "A newly minter lawyer defends his nephew and friend on murder charges in rural Alabama.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQxNDYzMTg1M15BMl5BanBnXkFtZTgwNzk4MDgxMTE@._V1_UY1200_CR89,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=SL4HdaZXuOw")


""" Stores the Movie objects in a list. """
movies = [good_will_hunting, django_unchained, sing_street, the_usual_suspects, wreck_it_ralph, my_cousin_vinny]

"""Opens the movie website in the user's browser; features the movies above."""
fresh_tomatoes.open_movies_page(movies)
