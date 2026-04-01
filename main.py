import asyncio

from config import Config, DBConfig
from database.crud import PostCrud
from logger import setup_logger
from notifier import Notifier
from rss_parser import RSSParser

logger = setup_logger(__name__)


async def poll_rss(rss_parser: RSSParser, post_crud: PostCrud, notifier: Notifier):
    """Основная задача: парсит RSS, сохраняет новые посты, отправляет в Telegram."""

    pass


async def main():
    """Главная функция."""

    logger.info('Запуск RSS Telegram бота...')
    
    config = Config()
    db_config = DBConfig()
    
    try:
        while True:
            await asyncio.sleep(60)
    except KeyboardInterrupt:
        logger.info('Получен сигнал остановки...')
    finally:
        pass


if __name__ == '__main__':
    asyncio.run(main())
