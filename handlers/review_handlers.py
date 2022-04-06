from fastapi import Query
from errors.errors import Endpoint5xxException


def load_review_handlers(app, data_manager):

    # Review filter endpoint
    @app.get("/reviews")
    async def get_reviews(
            title: list[str] or None = Query(None),
            author: list[str] or None = Query(None),
            genre: list[str] or None = Query(None),
            rating: list[str] or None = Query(None),
            emotion: list[str] or None = Query(None),
    ):
        filters = [
            ('title', title),
            ('author', author),
            ('genre', genre),
            ('rating', rating),
            ('emotion', emotion),
        ]

        try:
            return {
                'reviews': data_manager.get_reviews(filters)
            }
        except Exception as e:
            raise Endpoint5xxException(e)

    # Review search endpoint
    # Review filter endpoint
    @app.get("/search/")
    async def get_reviews(
            title: list[str] or None = Query(None),
            author: list[str] or None = Query(None),
            genre: list[str] or None = Query(None),
            rating: list[str] or None = Query(None),
            emotion: list[str] or None = Query(None),
    ):
        filters = [
            ('title', title),
            ('author', author),
            ('genre', genre),
            ('rating', rating),
            ('emotion', emotion),
        ]

        try:
            return {
                'reviews': data_manager.get_reviews(filters, strict=False)
            }
        except Exception as e:
            raise Endpoint5xxException(e)