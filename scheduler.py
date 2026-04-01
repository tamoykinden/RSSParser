from apscheduler.schedulers.asyncio import AsyncIOScheduler


class Scheduler:
    """Планировщик для периодического запуска задач."""
    
    def __init__(self, interval_minutes: int):

        self.interval_minutes = interval_minutes
        self.scheduler = AsyncIOScheduler()
        self._job = None
        pass
    
    def add_job(self, func, *args, **kwargs):
        """Добавляет задачу для периодического выполнения."""

        pass
    
    def start(self):
        """Запускает планировщик."""

        pass
    
    def stop(self):
        """Останавливает планировщик."""

        pass
