import os
import logging
from dotenv import load_dotenv

from handlers.commands import start
from handlers.messages import forward
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters


load_dotenv()

TOKEN = os.environ.get('TOKEN')
GROUP_ID = os.environ.get('GROUP_ID')


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.bot_data = {"GROUP_ID": GROUP_ID}

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.ChatType.PRIVATE & ~(filters.COMMAND),
            forward,
        )
    )

    # Run the bot until the user presses Ctrl-C
    app.run_polling()


if __name__ == "__main__":
    main()
