from exceptions import BotApiException, ConfigNotFoundError
from automated_bot import AutomatedBot
from factories.user_factories import FakeUserFactory
from factories.post_factories import FakePostFactory
from config import Config


def main():
    try:
        bot = AutomatedBot(FakeUserFactory, FakePostFactory, Config)
    except ConfigNotFoundError as e:
        logging.error(e)
    else:
        try:
            bot.start()
        except BotApiException as e:
            logging.error(e)


if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig('../logging.conf')
    main()
