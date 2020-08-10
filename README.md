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
            -  包含意图intents、`实体entities`、`插槽slots`、动作actions、回复templates
                - intents、entities在NLU训练样本中定义
                - slots对应于entities类型，只是表现形式不同。
            - 文件组成
                - intents	意图
                - `entities	实体`
                    - entities，即实体，类似于输入文本中的关键字，需要在NLU样本中进行标注，
                    - 然后Bot进行实体识别，并将其填充到Slot槽中，便于后续进行相关的业务操作
                - session_config 
                    - 一次会话的超时时间和超时后进行下一次会话的行为
                    - carry_over_slots_to_new_session
                        - 每次会话的超时时间，
                        - 当设置为0时，会一直等待，直到用户输入
                        - 如果在X秒没有输入任何东西会话，，则开始一轮新的会话。
                    - carry_over_slots_to_new_session
                       - 为True将上一次会话的Slot值拷贝过来
                       - 为False舍弃上一次会话Slot的值
                - slots 插槽
                    - 相当于机器人的内存(memory)，它们以键值对的形式存在，用于存储用户输入时消息时比较重要的信息，
                    而这些信息将为Action的执行提供关键数据。
                    - Slots的定义位于domain.yaml文件中，它们通常与Entities相对应，
                    即Entities有哪些，Slots就有哪些，并且Slots存储的值就是NLU模型提取的Entities的值。
                    - 定义
                        - 在domain.yml中定义，有多种格式
                    - set
                        - Slots Initial
                            - 在domain中，通过initial_value设置初始值：initial_value: "human"
                        - stories.md
                            - 在stories.md文件添加一个包含-slot{"slot_name":"slot_value"}的story
                    
                - actions 动作
                    - 当Rasa NLU识别到用户输入Message的意图后
                    - Rasa Core对话管理模块就会对其作出回应，而完成这个回应的模块就是action。
                    - Rasa Core支持三种action，即default actions、utter actions以及 custom actions。
                        -  DefaultAction：Rasa Core默认的一组actions，我们无需定义它们，直接可以story和domain中使用。包括以下三种action：
                            - action_listen：监听action，Rasa Core在会话过程中通常会自动调用该action；
                            - action_restart：重置状态，比初始化Slots(插槽)的值等；
                            - action_default_fallback：当Rasa Core得到的置信度低于设置的阈值时，默认执行该action；
                        -   UtterAction：以utter_为开头，仅仅用于向用户发送一条消息作为反馈的一类actions。
                            - 定义UtterAction：在domain.yml文件中的actions:字段定义以utter_为开头的action即可，
                            而具体回复内容将被定义在templates:部分，这个我们下面有专门讲解。
                        -   custom actions
                            -   CustomAction，即自定义action
                - templates	回答模板

        - endpoints.yml &emsp; details for connecting to channels like fb messenger

    - data
        - nlu.md：NLU模型训练样本数据：
        - stories.md
            - 说明 stories里面设计了对话场景 
               -  `##`	story 标题(描述作用没有任何意义)
               - `*` 意图：在nlu.md定义
               - `-` 动作：在domain.yml中定义
*	

    - models
        - <timestamp>.tar.gz	your initial model

- train model
    - 同时训练NLU和Core模型
    - rasa train --config ./configs/config.yml --domain ./configs/domain.yml --data data/
        - data\total_word_feature_extractor_zh.dat 放在指定的目录下

- 启动rasa
    - python -m rasa run --port 5005 
        --endpoints configs/endpoints.yml 
      --credentials configs/credentials.yml --debug


- rasa run --port 9900 --debug

- rasa run actions --port 9901 --actions actions --debug 