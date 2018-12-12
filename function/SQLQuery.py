from os.path import abspath, basename, splitext
import json, subprocess

class SQLQuery:
    def __init__(self, configPath):
        self.jsonContent = ''
        with open(configPath, 'rb') as f:
            self.jsonContent = f.read()
            self.jsonContent = json.loads(jsonContent)
            f.close()
        

    def handle(self, path):
        if basename(dirname(path)) in :