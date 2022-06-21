from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, _: ContextTypes) -> None:
    user = update.effective_user
    text = f"سلام {user.mention_html()}\n" \
            "انتقاد، پیشنهاد، فایل یا هرچیزی که می‌خوای بدست ما برسه رو در ادامه بفرست یا فوروارد کن. (اگر فایل می‌فرستی، اینکه چیه و مال چه نیمسالی هست هم بگو کنارش)\n" \
            "ممنون ♡"

    await update.message.reply_html(
        text,
    )
