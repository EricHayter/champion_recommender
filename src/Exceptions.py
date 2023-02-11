class InvalidPUUIDError(Exception):
    def __init__(self, str: puuid, Response: res):
        message = f'Got an unknown value PUUID of {puuid}'
        self.res = res
        super().__init__(message)