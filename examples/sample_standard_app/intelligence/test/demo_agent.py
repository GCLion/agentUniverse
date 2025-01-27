# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/5/8 11:41
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: peer_chat_bot.py
from agentuniverse.llm.llm_manager import LLMManager

from agentuniverse.base.agentuniverse import AgentUniverse
from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager


import os
current_file_path = os.path.abspath(__file__)

# 提取当前 Python 文件所在的目录路径
current_directory = os.path.dirname(current_file_path)

# 将工作路径切换到当前文件所在的目录
os.chdir(current_directory)

AgentUniverse().start(config_path='../../config/config.toml') # , core_mode=True


def chat(question: str):
    """ Peer agents example.

    The peer agents in agentUniverse become a chatbot and can ask questions to get the answer.
    """
    instance: Agent = AgentManager().get_instance_obj('demo_agent')
    output_object = instance.run(input=question)
    res_info = f"\nDemo agent execution result is :\n"
    res_info += output_object.get_data('output')
    print(res_info)


if __name__ == '__main__':
    chat("分析下巴菲特减持比亚迪的原因")
