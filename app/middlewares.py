import time
import logging
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


logger = logging.getLogger(__name__)


class TestMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        print("Actions before")
        start_time = time.time()
        user_id = event.from_user.id if event.from_user else "Unknown"
        try:
            result = await handler(event, data)
        except Exception as e:
            logger.error(f"Error while processing event for user {user_id}: {e}")
            raise

        elapsed_time = time.time() - start_time - start_time
        logger.info(f"Event for user {user_id} processed in {elapsed_time:.3f} seconds")


        return result

