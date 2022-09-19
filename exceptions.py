class EnvVarMissingException(Exception):
    pass


class IncorrectAPIResponseException(Exception):
    def __init__(self, message='Некорректный ответ API'):
        super().__init__(message)


class APIUnavailableException(Exception):
    def __init__(self, message='API недоступен'):
        super().__init__(message)
