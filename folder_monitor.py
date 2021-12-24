import time
from collections import deque
import os
import shutil
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class TestEventHandler(PatternMatchingEventHandler):
    def __init__(self, *args, **kwargs):
        super(TestEventHandler, self).__init__(*args, **kwargs)
        self.events = deque(maxlen=5)

    def created(self, event):
        pass

    def mondified(self, event):
        pass

    def delted(self, event):
        pass

    def moved(self, event):
        pass

    def on_any_event(self, event):
        super().on_any_event(event)
        path = event.src_path
        event_type = event.event_type
        self.events.append((event_type, datetime.now().timestamp()))

        if event_type == 'created':
            print(f'Created: {path}')
        elif event_type == 'modified':
            print(f'modified: {path}')
        elif event_type == 'deleted':
            print(f'deleted: {path}')
        elif event_type == 'moved':
            print(f'moved: {path}')

        print(self.events)
        print('\n\n')


if __name__ == '__main__':

    path = '/Users/zach/Developer/1_Projects/CaseDigtial/folder-monitor'
    # target_dir = "C:\\Temp\\2017\\07\\25"
    # src_dir = "C:\\Temp2\\2017\\07\\25"
    # filename = 'test.xml'

    # target = os.path.join(target_dir, filename)
    # src = os.path.join(src_dir, filename)

    event_handler = TestEventHandler(patterns=["*"])
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    # if not os.path.exists(target_dir):
    #     os.makedirs(target_dir)

    # if os.path.exists(target):
    #     os.unlink(target)

    # for i in range(3):
    #     shutil.copy2(src, target_dir)    

    try:
       while True:
           time.sleep(1)
    except KeyboardInterrupt:
       observer.stop()
    observer.join()