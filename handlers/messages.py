import os

from telegram import Update
from telegram.ext import ContextTypes
from telegram.helpers import escape_markdown
from telegram.constants import ParseMode


async def forward(update: Update, context: ContextTypes) -> None:
    user = update.effective_user
    sender_info = f"_id:_ {user.id}\n" \
                  f"_name:_ {escape_markdown(user.full_name, version=2)}\n" \
                  f"_username:_ {escape_markdown('@' + user.username if user.username else '-', version=2)}"

    try:
        forwarded_message = await update.effective_message.forward(
            chat_id=os.getenv("GROUP_ID"),
        )

        await context.bot.send_message(
            chat_id=os.getenv("GROUP_ID"),
            text=sender_info,
            reply_to_message_id=forwarded_message.message_id,
            parse_mode = ParseMode.MARKDOWN_V2,
        )

        await forwarded_message.pin()

        await update.effective_message.reply_markdown_v2(
            text="_✓ ارسال شد_",
            quote=True,
        )
    except Exception as e:
        print(e)

        await update.effective_message.reply_html(
            text=f"_✗ ارسال نشد. متن خطا:_\n{escape_markdown(str(e), version=2)}",
            quote=True,
        )
