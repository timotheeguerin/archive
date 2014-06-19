import os
import yaml
import logging


class Platform:
    data_file = os.path.join(os.path.dirname(__file__), '../data/platform.yml')
    platforms = {}

    @staticmethod
    def load():
        stream = open(Platform.data_file, 'r')
        Platform.platforms = yaml.load(stream)


    @staticmethod
    def is_in_platform(platform, parent):
        """
            This will check if the platform given is a subplatform of the parent one
        """
        if platform == parent:
            return True
        parent_element = Platform.get_element(Platform.platforms['platforms'], parent)
        if parent_element is None:
            logging.error('The given platform is unknown: `%s`', parent_element)
            return False
        else:
            return not Platform.get_element(parent_element, platform) is None

    @staticmethod
    def get_element(hash, element):
        if type(hash) is dict:
            for key in hash:
                if key == element:
                    return hash[key]
                else:
                    result = Platform.get_element(hash[key], element)
                    if not result is None:
                        return result
        elif type(hash) is list:
            for e in hash:
                if e == element:
                    return e
        elif hash == element:
            return hash

        return None


Platform.load()
