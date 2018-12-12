from os.path import abspath, basename, splitext
import json, subprocess

class SQLQuery:
    def __init__(self, configPath, loginPath):
        self.jsonContent = ''
        with open(configPath, 'rb') as f:
            self.jsonContent = f.read()
            self.jsonContent = json.loads(self.jsonContent)
            f.close()

        with open(loginPath, 'rb') as f:
            self.loginInfo = f.read()
            self.loginInfo = json.loads(self.loginInfo)
            f.close()

    def handle(self, path):
        if basename(dirname(path)) in self.jsonContent:
            subprocess.call("sqlcmd -S {0} -Q \"USE {1};EXEC {2} @PATH = '{3}', @FILENAME = '{4}';\"".format(self.loginInfo['User'], self.loginInfo['DBName'], self.jsonContent[self.jsonContent.keys().index(basename(dirname(path)))], abspath(path), splitext(basename(path))[0]))