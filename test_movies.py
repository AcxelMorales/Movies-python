from domain.Movie import Movie
from services.MovieCatalog import MovieCatalog as cp

option = None

while option != 4:
    try:
        print('''
            Options: \n
            1. Add movie\n
            2. List movies\n
            3. Remove catalog of movies\n
            4. Exit
        ''')

        option = int(input('Enter your choice (1-4): '))

        if option == 1:
            name_movie = input('Enter name of movie: ')
            movie = Movie(name_movie)
            cp.add_movie(movie.name)
        elif option == 2:
            cp.list_movies()
        elif option == 3:
            cp.remove()
    except Exception as e:
        print(e)
        option = None
else:
    print('End to app')
