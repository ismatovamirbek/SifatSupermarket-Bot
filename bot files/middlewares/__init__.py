from aiogram import Dispatcher
from .cheksub import BigBrother
from loader import dp
from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(BigBrother())
