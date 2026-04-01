from typing import List

from database.models import Post


class RSSParser:
    """Парсер RSS-ленты."""
    
    def __init__(self, rss_url: str):
        self.rss_url = rss_url
        pass
    
    async def fetch(self):
        """Загружает и парсит RSS-ленту."""

        pass
