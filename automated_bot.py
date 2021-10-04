from clients import RestApiClient


class AutomatedBot:
    def __init__(self):
        self.client = RestApiClient()

    def __call__(self, *args, **kwargs):
        pass  # todo
