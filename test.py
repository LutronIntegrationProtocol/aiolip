import asyncio
import logging

from aiolip import LIP
from aiolip.data import LIPMode

_LOGGER = logging.getLogger(__name__)


async def main():
    lip = LIP()

    logging.basicConfig(level=logging.DEBUG)

    await lip.async_connect("192.168.1.2")

    def message(msg):
        _LOGGER.warning(msg)

    lip.set_callback(message)
    task = asyncio.create_task(lip.async_run())
    await lip.query(LIPMode.OUTPUT, 31, 1)
    #await lip.async_stop()
    await task

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
