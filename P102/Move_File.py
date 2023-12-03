import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Elv/Downloads"
to_dir = "C:/Users/Elv/Desktop/Python/P102/Arranged"

list_of_files = os.listdir(from_dir)
print(list_of_files)

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path)

                print("Downloaded" + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("Moving" + file_name + ".....")
                    shutil.move(path1, path3)
                    time.sleep(3)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving" + file_name + ".....")
                    shutil.move(path1, path3)
                    time.sleep(3)


event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()


try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()