import os

from dotenv import load_dotenv


class Config:
    """Конфигурация проекта. Загружает настройки из .env файла."""
    
    def __init__(self):
        """Загружает переменные окружения."""

        load_dotenv()
        
        self.RSS_URL = os.getenv('RSS_URL')
        self.TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
        self.TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
        self.DATABASE_URL = os.getenv('DATABASE_URL')
        self.POLL_INTERVAL_MINUTES = int(os.getenv('POLL_INTERVAL_MINUTES', '5'))


class DBConfig:
    """Настройки подключения к БД."""
    
    def __init__(self):
        """Загружает настройки БД из .env."""

        load_dotenv()
        
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')
    
    @property
    def database_url(self):
        """Возвращает строку подключения к PostgreSQL."""
        
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
