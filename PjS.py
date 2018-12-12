from watchdog.observers import Observer
from watchdog.events import *
from os.path import abspath, basename, splitext
import json, subprocess, time

# FileSystemEventHandler繼承自watch.events
# 監聽位置的class後面一定要加FileSystemEventHandler
class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        print("PjS start")
    
    # 判斷移動方式(繼承自FileSystemEventHandler)然後判斷是否為directory(繼承自watchdog.event)
    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            handle(event.src_path)
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))
    
if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    # 綁定監聽位置與監聽程序
    observer.schedule(event_handler, '../Data/', True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    # 更新監聽
    observer.join()
