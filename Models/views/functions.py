import os


def clean_up(path):
    to_remove = f'media/submitted_pictures/{path}'
    return os.remove(to_remove)

