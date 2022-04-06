from fastapi import Query
from errors.errors import Endpoint5xxException


def load_field_handlers(app, data_manager):
    # Dropdown/Field Endpoints

    @app.get('/titles')
    async def get_titles(title=None):
        try:
            return {
                'titles': data_manager.get_field_values('titles', title)
            }
        except Exception as e:
            raise Endpoint5xxException(e)

    @app.get('/authors')
    async def get_authors(author=None):
        try:
            return {
                'authors': data_manager.get_field_values('authors', author)
            }
        except Exception as e:
            raise Endpoint5xxException(e)

    @app.get('/ratings')
    async def get_ratings(rating=None):
        try:
            return {
                'ratings': data_manager.get_field_values('ratings', rating)
            }
        except Exception as e:
            raise Endpoint5xxException(e)

    @app.get('/annotations')
    async def get_annotations(annotation=None):
        try:
            return {
                'annotations': data_manager.get_field_values('annotations', annotation)
            }
        except Exception as e:
            raise Endpoint5xxException(e)

    @app.get('/genres')
    async def get_genres(genre=None):
        try:
            return {
                'genres': data_manager.get_field_values('genres', genre)
            }
        except Exception as e:
            raise Endpoint5xxException(e)
