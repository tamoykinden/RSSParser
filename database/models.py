from datetime import datetime
import hashlib
from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class Post(Base):
    """Модель поста."""
    
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    link = Column(String, unique=True, nullable=False)
    published = Column(DateTime, nullable=False)
    content_hash = Column(String, unique=True, nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    
    @staticmethod
    def compute_hash(title: str, link: str) -> str:
        """Вычисляет хэш от заголовка и ссылки."""

        unique_string = f'{title}{link}'
        return hashlib.sha256(unique_string.encode()).hexdigest()
    
    def __repr__(self) -> str:
        return f'Post(id={self.id}, title={self.title[:30]}...)'
