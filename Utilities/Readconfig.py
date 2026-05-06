import configparser
import os

config = configparser.RawConfigParser()

config.read(os.path.join(os.path.abspath(os.curdir), 'configurations', 'config.ini'))

class readconfig():
    @staticmethod
    def GetAppURL():
        url=config.get('commonInfo','BaseURL')
        return url

