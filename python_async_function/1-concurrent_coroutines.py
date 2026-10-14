#!/usr/bin/env python3
"""
A module containing an async coroutine spawner
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    A function that spawns wait_random n times with the specified max_delay
    and returns a list of the delays in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]


if __name__ == "__main__":
    n = 5
    max_delay = 5
    delays = asyncio.run(wait_n(n, max_delay))
    print(f"Delays: {delays}")
