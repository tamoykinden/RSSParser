from typing import List

from database import Database
from database.models import Post


class PostCrud:
    """CRUD-операции для работы с постами в БД."""
    
    def __init__(self, db: Database):
        self.db = db
        pass
    
    async def is_new_post(self, content_hash: str) -> bool:
        """Проверяет, есть ли пост с таким хэшем в БД."""

        pass
    
    async def save_new_posts(self, posts: List[Post]) -> List[Post]:
        """Сохраняет только новые посты (которых ещё нет в БД)."""

        pass
    
    async def get_all_posts(self, limit: int = 50) -> List[Post]:
        """Получает последние посты (для отладки)."""

        pass
