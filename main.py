import imdb
hr= imdb.IMDb()
movie_name= input("Enter the movie name: ")
movie= hr.search_movie(str(movie_name))
index = movie[0].getID()
movie = hr.get_movie(index)
title= movie['title']
year= movie['year']
cast= movie['cast']
list_of_cast= ',' .join(map(str, cast))
print("title", title)
print("year of release: ",year)
print("full cast: ",list_of_cast)
