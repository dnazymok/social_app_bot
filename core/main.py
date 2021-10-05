from automated_bot import AutomatedBot


def main():
    try:
        bot = AutomatedBot()
    except:  # todo custom errors about init
        pass
    else:
        try:
            bot.start()
        except:
            pass  # todo custom error


if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig('../logging.conf')
    main()
