# !/usr/bin/python
# -*- coding:utf-8 -*-
from rasa.core.agent import Agent
from rasa.core.policies.keras_policy import KerasPolicy
from rasa.core.policies.memoization import MemoizationPolicy
if __name__ == '__main__':
    agent = Agent("/home/user/xiaoqq/chat_robot/rasa_learn/configs/domain.yml", policies=[MemoizationPolicy(), KerasPolicy()])

    agent.visualize("/home/user/xiaoqq/chat_robot/rasa_learn/data/stories/stories.md",
                    output_file="graph.html", max_history=2)