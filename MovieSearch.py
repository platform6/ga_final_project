import imdb


class MovieSearch:

    def __init__(self, search_word):
        self.ia = imdb.IMDb()
        self.search_word = search_word
        self.results = self.search()

    def get_search_results(self):
        return self.results

    def search(self):
        return self.ia.search_movie(self.search_word)


movie = MovieSearch('ice')
print(movie.get_search_results())

# for each in movie.get_search_results():
#    print(each)


