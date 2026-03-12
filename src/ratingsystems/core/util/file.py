import os


config_path = os.path.join(os.path.expanduser("~"), ".ratingsystems")

if not os.path.exists(config_path):
    os.mkdir(config_path)
