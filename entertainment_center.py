import media
import fresh_tomatoes

# Instantiate 7 movies and/or clips with the media.Movie class.
# Note: Image URLs are customized to work with a local folder called "images".
toy_story = media.Movie("Toy Story",
                        "A story about toys that come to life.",
                        "images/toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

boiler_room = media.Movie("Boiler Room", "A fast-talking guy dives into a sophisticated plot to steal money",
                          "images/boiler_room.jpg",
                          "https://www.youtube.com/watch?v=6VoXMvNrQro")


bobalife = media.Movie("Boba Life", "A movie about the boba milk tea fad!",
                       "images/boba.png",
                       "https://www.youtube.com/watch?v=zccNQPH7Xe0&list=RDzccNQPH7Xe0")

linsanity = media.Movie("Lin: Last Pick", "A movie about a child who aspires for more.",
                        "images/linsanity.jpg",
                        "https://www.youtube.com/watch?v=u3cfLvCsm54")

boom_boom_pow = media.Movie("Boom Boom Pow", "A song about the future.",
                            "images/boom.jpg",
                            "https://www.youtube.com/watch?v=IyFiSyI2wng")

the_interview = media.Movie("The Interview", "A movie about world domination.",
                            "images/interview.jpg",
                            "https://www.youtube.com/watch?v=aVNUR0r-3KQ")

star_wars_battlefront = media.Movie("Star Wars Battlefront", "Honestly, it's a videogame!",
                                    "images/star_wars.jpg",
                                    "https://www.youtube.com/watch?v=ZwWLns7-xN8")

# Create an array of movie objects
movies = [toy_story, boiler_room, bobalife, linsanity, boom_boom_pow, the_interview, star_wars_battlefront]

# Use the fresh_tomatoes library to create and open the movies HTML page with the movie data.
# This will also create an index.html file that you can drag into your web folder.
fresh_tomatoes.open_movies_page(movies)
