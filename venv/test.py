import imdb

ia = imdb.IMDb()

search = ia.get_movie('1510984')
year = search['year']


print(search['title'] + ":" + str(year))



