from src.exception import WowException
import re


class ConfigFormat:
    """
        Contains format validation for the config file
    """

    config_required_attributes = []
    config_attributes_regex = []

    def validate_presence_of(self, object):
        if isinstance(object, list):
            for name in object:
                self.config_required_attributes.append(name)
        else:
            self.config_required_attributes.append(object)

    def validate_with(self, name, regex, message):
        self.config_attributes_regex.append({'name': name, 'regex': regex, 'message': message})

    def validate(self, config):
        for key in self.config_required_attributes:
            if not key in config:
                raise WowException("Config file is missing the attribute `%s`" % key)

        for hash in self.config_attributes_regex:
            name = hash['name']
            regex = hash['regex']
            if not re.match(regex, config[name]):
                raise WowException(hash['message'])
