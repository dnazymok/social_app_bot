from core.exceptions import BotApiException, ConfigNotFoundError
from core.automated_bot import AutomatedBot
from requests.exceptions import ConnectionError


def main():
    try:
        bot = AutomatedBot()
    except ConfigNotFoundError as e:
        logging.error(e)
    else:
        try:
            bot.start()
        except (ConnectionError, BotApiException) as e:
            logging.error(e)


if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig('logging.conf')
    main()
