# python-telegram-bot-template
Template for Telegram bots built with  python-telegram-bot 

1. Create a bot using [@BotFather](https://telegram.me/BotFather)
2. Set your bot parameters in `config/conf.yml`
3. Run `make_bot.py` to create `bot.py`
4. Run `python bot.py` to run your bot

## NOTE:
At the moment the bot token is in clear text in `bot.py`, this is a dangerous behavior if you want to version your bot. Once you have generated the token, export it in an environment variable and use that in `bot.py`.

__Example:__  

.bashrc
```bash
export MY_BOT_TOKEN='S0m3HexString'
```  

bot.py
```python
updater = Updater(token=os.environ["MY_BOT_TOKEN"], use_context=True)

```

