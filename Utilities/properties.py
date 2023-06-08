import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getURL():
        url = config.get('common', 'URL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common', 'password')
        return password


