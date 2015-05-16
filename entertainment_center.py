import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about toys that come to life.",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# print toy_story.storyline

boiler_room = media.Movie("Boiler Room", "A fast-talking guy dives into a sophisticated plot to steal money",
                          "http://images.moviepostershop.com/boiler-room-movie-poster-2000-1020186083.jpg",
                          "https://www.youtube.com/watch?v=6VoXMvNrQro")


bobalife = media.Movie("Boba Life", "A movie about the boba milk tea fad!",
                       "http://40.media.tumblr.com/tumblr_li0ek6EviE1qc2eojo1_1280.png",
                       "https://www.youtube.com/watch?v=zccNQPH7Xe0&list=RDzccNQPH7Xe0")

linsanity = media.Movie("Lin: Last Pick", "A movie about a child who aspires for more.",
                        "http://cdn.nikeblog.com/wp-content/uploads/2012/02/Jeremy-Lin-Posters-3.jpg",
                        "https://www.youtube.com/watch?v=u3cfLvCsm54")

boom_boom_pow = media.Movie("Boom Boom Pow", "A song about the future.",
                            "http://www.posterplanet.net/music/images/music-black-eyed-peas-boom-pow-poster-TR5229.jpg",
                            "https://www.youtube.com/watch?v=IyFiSyI2wng")

the_interview = media.Movie("The Interview", "A movie about world domination.",
                            "http://www.impawards.com/2014/posters/interview.jpg",
                            "https://www.youtube.com/watch?v=aVNUR0r-3KQ")

star_wars_battlefront = media.Movie("Star Wars Battlefront", "Honestly, it's a videogame!",
                                    "http://www.gamepur.com/files/images/2015/star-wars-battlefront-box-art-ps4.jpeg",
                                    "https://www.youtube.com/watch?v=ZwWLns7-xN8")

movies = [toy_story, boiler_room, bobalife, linsanity, boom_boom_pow, the_interview, star_wars_battlefront]
fresh_tomatoes.open_movies_page(movies)
