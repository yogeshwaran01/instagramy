""" Caches Management """

import os
import json

cache_dir = ".instagramy_cache"


class Cache:

    """ Class for caches Management """

    def __init__(self, key: str):
        self.key = key
        if not os.path.isdir(cache_dir):
            os.mkdir(cache_dir)
        with open(cache_dir + "/CACHEDIR.TAG", "w") as file:
            file.write(
                "# This file is a cache directory tag created by instagramy." + "\n"
            )

    def is_exists(self, name: str) -> bool:
        return os.path.isfile(cache_dir + f"/{name}_{self.key}" + ".json")

    def make_cache(self, name: str, data: dict):
        with open(cache_dir + f"/{name}_{self.key}" + ".json", "w") as file:
            json.dump(data, file)

    def read_cache(self, name: str) -> dict:
        with open(cache_dir + f"/{name}_{self.key}" + ".json", "r") as file:
            return json.load(file)
