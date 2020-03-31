import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from functools import wraps

whitelist = [userIdGoesHere]

def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in whitelist:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context, *args, **kwargs)
    return wrapped



updater = Updater(token="tokenGoesHere", use_context=True)
dispatcher = updater.dispatcher


@restricted
def somefunction(message, context):
    # TODO: your implementation goes here
    context.bot.send_message(chat_id=message.effective_chat.id, text="Define your handler in `bot.py`")
    pass

@restricted
def some_audio_function(message, context):
    # TODO: your implementation goes here
    # FIXME: remove open for content from URL
    # e.g. bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
    context.bot.send_voice(chat_id=message.effective_chat.id, voice=open("path/to/voice", "rb"))
    pass

@restricted
def welcome(message, context):
    # TODO: your implementation goes here
    context.bot.send_message(chat_id=message.effective_chat.id, text="Define your handler in `bot.py`")
    pass


@restricted
def inline_func(message, context):
    query = message.inline_query.query
    if not query:
        return
    results = list()
    """
    TODO: fill you result list here
    more info: https://core.telegram.org/bots/api#inline-mode
    """
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='InlineResponse',
            description="toUpperCase",
            input_message_content=InputTextMessageContent(query.upper())
        ))
    context.bot.answer_inline_query(message.inline_query.id, results)

inline_handler = InlineQueryHandler(inline_func)
dispatcher.add_handler(inline_handler)

cmd_handler_l_1 = CommandHandler("start", welcome)
dispatcher.add_handler(cmd_handler_l_1)
cmd_handler_l_2 = CommandHandler("stop", welcome)
dispatcher.add_handler(cmd_handler_l_2)

"""
Note: This handler must be added last (last of the CommandHandler). 
If you added it sooner, it would be triggered before the CommandHandlers 
had a chance to  look at the update.
"""
@restricted
def uknown_cmd_handler(message, context):
        context.bot.send_message(chat_id=message.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, uknown_cmd_handler)
dispatcher.add_handler(unknown_handler)


msg_handler_1 = MessageHandler(Filters.text, somefunction)
dispatcher.add_handler(msg_handler_1)
msg_handler_2 = MessageHandler(Filters.voice, some_audio_function)
dispatcher.add_handler(msg_handler_2)

if __name__ == "__main__":
    updater.start_polling()