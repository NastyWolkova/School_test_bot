import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from config import Config, load_config
from all_handlers import out_test, in_test_rus, in_test_log 
import logging

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                '[%(asctime)s] - %(name)s - %(message)s')
    file_handler = logging.FileHandler('logs.log', mode= 'w')
    file_handler.setFormatter(format)
    logger.addHandler(file_handler)

    storage = MemoryStorage()
    # Загружаем конфиг в переменную config
    config: Config = load_config('.env')
    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)


    # Регистриуем роутеры в диспетчере
    dp.include_router(out_test.router)
    dp.include_router(in_test_rus.router)
    dp.include_router(in_test_log.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    #await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())