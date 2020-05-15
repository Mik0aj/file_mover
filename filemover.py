"""project that moves files from downloads folder to designated folder based on file's extension"""
import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


IMAGES = ['jpeg', 'jpg', 'png', 'exif', 'bmp']
VIDEOS = ['mp4', 'avi', 'wmv']
DOCUMENTS = ['txt', 'pdf', 'docx']
class MyHandeler(FileSystemEventHandler):
    """handler class, defines what will happen when files are modified"""

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename.endswith(tuple(IMAGES)):
                path = os.path.expanduser('~/Pictures')
                move(filename, path)
            elif filename.endswith(tuple(VIDEOS)):
                path = os.path.expanduser('~/Videos')
                move(filename, path)
            elif filename.endswith(tuple(DOCUMENTS)):
                path = os.path.expanduser('~/Documents')
                move(filename, path)

def move(filename, path):
    """moves file specified with name to given location"""
    print('moving', filename, 'to', path)
    src = folder_to_track + "/" + filename
    new_destination = path + "/" + filename
    os.rename(src, new_destination)

# Do przeciążenia funkcji
# def move(self, src_path, filename, dest_path):
#     print('moving', filename, 'from', src_path, 'to', dest_path)
#     src = src_path + "/" + filename
#     new_destination = dest_path + "/" + filename
#     os.rename(src, new_destination)



if __name__ == "__main__":
    print("filemover is on")
    folder_to_track = os.path.expanduser('~/Downloads')
    event_handler = MyHandeler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
