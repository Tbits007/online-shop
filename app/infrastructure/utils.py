from fastapi_cache import FastAPICache


async def clear_cache():
    """
    Очистка кеша.
    """
    await FastAPICache.clear()