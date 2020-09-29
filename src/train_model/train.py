# !/usr/bin/python
# -*- coding:utf-8 -*-
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter

from rasa.core.policies.keras_policy import KerasPolicy

# agent=Agent(domain=None, policies=None, interpreter=None, generator=None,
# tracker_store=None, lock_store=None, action_endpoint=None,
# fingerprint=None, model_directory=None, model_server=None, remote_storage=None, path_to_model_archive=None)

if __name__ == '__main__':
    domain_file = '/home/user/xiaoqq/chat_robot/rasa_learn/configs/domain_slot.yml'
    agent = Agent(domain_file, policies=[KerasPolicy(validation_split=0.0, epochs=400)])
    training_data_file = '/home/user/xiaoqq/chat_robot/rasa_learn/data/nlu/nlu_slot.md'
    training_data = agent.load_data(training_data_file)

    model_path = '/home/user/xiaoqq/chat_robot/rasa_learn/data/models'
    agent.train(training_data
                )
    agent.persist(model_path)
