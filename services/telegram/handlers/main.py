from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InlineQueryResultArticle, InputTextMessageContent, InlineQuery, Message, \
    InlineKeyboardMarkup

from services.AI.main import get_answer

router = Router()

@router.message(F.text)
async def find_command(message: Message):
    await message.answer(get_answer(message.text))
