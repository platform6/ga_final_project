import imdb


class MovieSearch:

    def __init__(self, search_word):
        self.ia = imdb.IMDb()
        self.search_word = search_word
        self.search_results = self.search()
        self.list_of_id = self.get_list_of_movie_id()
        self.create_movie_search_dataframe()

    # the following searches the api by the search word
    def search(self):
        return self.ia.search_movie(self.search_word)

    # this gets the movie id from the search results
    def get_list_of_movie_id(self):
        list_of_id = []
        for i in range(len(self.search_results)):
            list_of_id.append(self.search_results[i].movieID)
        print(list_of_id)
        return list_of_id

    def create_movie_search_dataframe(self):
        id = []
        title = []
        year = []
        for i in range(len(self.search_results)):
            movie = self.ia.get_movie(self.list_of_id[i])
            id.append(self.list_of_id[i])
            title.append(movie.get('title'))
            year.append(movie.get('year'))
        data = {'id': id,
                'title': title,
                'year': year}
        print(data)


instance = MovieSearch('ice cream')
