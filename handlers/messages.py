from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from telegram.helpers import escape_markdown

from handlers import constants


async def forward(update: Update, context: ContextTypes) -> None:
    user = update.effective_user
    group_id = context.bot_data.get("GROUP_ID")

    sender_info = f"_id:_ {user.id}\n" \
                  f"_name:_ {escape_markdown(user.full_name, version=2)}\n" \
                  f"_username:_ {escape_markdown('@' + user.username if user.username else '-', version=2)}"

    try:
        forwarded_message = await update.effective_message.forward(
            chat_id=group_id,
        )

        await context.bot.send_message(
            chat_id=group_id,
            text=sender_info,
            reply_to_message_id=forwarded_message.message_id,
            parse_mode = ParseMode.MARKDOWN_V2,
        )

        await forwarded_message.pin()

        await update.effective_message.reply_html(
            text=constants.SUCCESS_MESSAGE,
            quote=True,
        )
    except Exception as e:
        print(e)

        await update.effective_message.reply_html(
            text=constants.FAILURE_MESSAGE,
            quote=True,
        )
