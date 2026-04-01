from database.models import Post


class Notifier:
    """Класс для отправки уведомлений в Telegram."""
    
    def __init__(self, bot_token: str, chat_id: str):
        self.bot_token = bot_token
        self.chat_id = chat_id
        pass
    
    async def send(self, post: Post):
        """Отправляет один пост в Telegram."""

        pass
    
    async def send_many(self, posts: list):
        """Отправляет несколько постов."""

        pass
    
    async def close(self):
        """Закрывает сессию бота."""

        pass
