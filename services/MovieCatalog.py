from os import remove


class MovieCatalog:

    route_file = 'movies.txt'

    def __init__(self, route_file):
        MovieCatalog.route_file = route_file

    @classmethod
    def add_movie(cls, movie):
        with open(cls.route_file, 'a', encoding='utf8') as file:
            file.write(f'{movie}\n')

    @classmethod
    def list_movies(cls):
        with open(cls.route_file, 'r', encoding='utf8') as file:
            print('Catalog of movies'.center(50, '-'))
            print(file.read())

    @classmethod
    def remove(cls):
        remove(cls.route_file)
        print(f'Deleted file: {cls.route_file}')
