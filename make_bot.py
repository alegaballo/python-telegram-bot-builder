from jinja2 import Environment, PackageLoader, select_autoescape
import os
import yaml
from typing import Dict
from collections import defaultdict

CONFIG_DIR =  "config"
CONFIG_FILE = "conf.yml"

def get_handlers(bot_config : Dict):
    handlers = defaultdict(list)
    for handler in bot_config["handlers"]:
        h_type = handler["type"]
        handlers[h_type].append(handler)
    return handlers

env = Environment(
    loader=PackageLoader(CONFIG_DIR, 'templates')
)
env.trim_blocks = True
env.lstrip_blocks = True

config_file =  os.path.join(CONFIG_DIR, CONFIG_FILE)

with open(config_file) as f:
    bot_config = yaml.safe_load(f)

handlers = get_handlers(bot_config)
template = env.get_template('bot_template.py.jinja')
t = template.render(cmd_handlers=handlers["cmd"], msg_handlers=handlers["msg"], **bot_config)


with open("bot.py", 'w') as f:
    f.write(t)
