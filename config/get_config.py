import os

import yaml


def get_config(Loader):
    with open(os.path.join("config", "base.yaml"), "r") as file:
        config = yaml.load(file, Loader)
    return config
