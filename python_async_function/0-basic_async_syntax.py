#!/usr/bin/env python3
"""
A module containing an asynchronous coroutine that
takes in an integer argument
named wait_random that waits for a random
delay between 0 and max_delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that takes in an integer argument
    named wait_random that waits for a random delay between 0 and max_delay
    """
    delay = random.uniform(0.0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    max_delay = 5
    delay = asyncio.run(wait_random(max_delay))
    print(f"Waited for {delay:.2f} seconds")
