from telegram import Update
from telegram.ext import ContextTypes

from handlers import constants


async def start(update: Update, _: ContextTypes) -> None:
    user = update.effective_user
    text = constants.START_MESSAGE.format(user=user.mention_html())
    await update.message.reply_html(text)
