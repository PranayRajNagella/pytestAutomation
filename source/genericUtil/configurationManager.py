import configparser
import os
from symtable import Class

from source.genericUtil.fileUtils import FileUtils


class ConfigurationManager:

    @classmethod
    def getConfiguration(self):
        if os.getenv('test_env')=='qa' or os.getenv('test_env') is None:
            config = configparser.ConfigParser()
            file_path =str(FileUtils.getProjectDir())+f'/resources/apiconfig.properties'
            config.read(file_path)
            if os.getenv('test_env') is None:
                return config['qa']
            else:
                return config[os.getenv('test_env')]


    def getProperty(propert_key):
        return ConfigurationManager.getConfiguration()[propert_key]




