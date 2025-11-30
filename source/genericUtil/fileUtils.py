import os


class FileUtils:
    @classmethod
    def getProjectDir(self):
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
