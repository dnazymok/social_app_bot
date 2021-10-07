from exceptions import BotApiException, BotConfigNotFoundError
from automated_bot import AutomatedBot
from factories.user_factories import FakeUserFactory
from factories.post_factories import FakePostFactory


def main():
    try:
        bot = AutomatedBot(FakeUserFactory, FakePostFactory)
    except BotConfigNotFoundError as e:
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
