from django.core.files.storage import FileSystemStorage
import os

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name: str, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(self.location,name))
        return name