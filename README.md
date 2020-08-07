- 说明
- 推荐文章 
    - https://blog.csdn.net/andrexpert/article/details/104328946
    - https://blog.csdn.net/u012526436/article/details/82911565
- 主要的步骤
    - `安装rasa`
         - pip --default-timeout=500 install -U rasa
         - pip instal jieba 
         - pip install mitie
    - `rasa init --no-prompt` 
        - Creates a new project with example training data, actions, and config files.
    - `启动rasa`
        - rasa shell    

- 文件说明
    - actions code for your custom actions
    - configs
        - config.yml  &emsp;  configuration of your NLU and Core models  训练NLU和Core模型配置文件：
        - credentials.yml &emsp; details for connecting to other services
        - domain.yml 
            - 说明 domain.yml文件相当于AI助手的大脑，记录了系统所有的信息。
            - domain 包含了整个对话场景下的意图，动作，以及对应动作所反馈的内容模板：
        - endpoints.yml &emsp; details for connecting to channels like fb messenger

    - data
        - nlu.md：NLU模型训练样本数据：
            - intents	意图
            - actions	动作
            - templates	回答模板
            - entities	实体
            - slots	词槽
        - stories
            - 说明 stories里面设计了对话场景 
               -  `##`	story 标题
               - `*` 意图
               - `-`动作
*	

    - models
        - <timestamp>.tar.gz	your initial model

- train model
    - 同时训练NLU和Core模型
    - rasa train --config ./configs/config.yml --domain ./configs/domain.yml --data data/
        - data\total_word_feature_extractor_zh.dat 放在指定的目录下

- 启动rasa
    - python -m rasa run --port 5005 
    - --endpoints configs/endpoints.yml 
    - --credentials configs/credentials.yml --debug


- rasa run --port 9900 --debug

- rasa run actions --port 9901 --actions actions --debug 