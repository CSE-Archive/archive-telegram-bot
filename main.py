import os
import logging

from commands import start
from messages import forward
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    app = ApplicationBuilder().token(os.getenv("TOKEN")).build()

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
