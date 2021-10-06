from exceptions import BotApiException, BotConfigNotFoundError

from automated_bot import AutomatedBot


def main():
    try:
        bot = AutomatedBot()
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
