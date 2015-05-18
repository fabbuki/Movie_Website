'''
Movie class stores the following information in string format:
1. Movie Title
2. Movie Storyline summary
3. Poster image URL
4. Youtube trailer URL

The Movie class can also open a browser and show its own youtube trailer, via the show_trailer() method.
'''

import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)