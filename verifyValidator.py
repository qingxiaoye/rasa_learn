# !/usr/bin/python
# -*- coding:utf-8 -*-
import logging
from rasa import utils
from rasa.core.validator import Validator

logger = logging.getLogger(__name__)

utils.configure_colored_logging('DEBUG')

validator = Validator.from_files(domain_file='configs/domain.yml',
                                 nlu_data='data/nlu/nlu_data.md',
                                 stories='data/stories/stories.md')

print(validator.verify_all())
