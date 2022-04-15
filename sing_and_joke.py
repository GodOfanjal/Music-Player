import random

from telegram import Update

from telegram.ext import CallbackContext, run_async

import MashaRoBot.modules.sing_and_joke_string as sing_and_joke_string

from MashaRoBot import dispatcher

from MashaRoBot.modules.disable import DisableAbleCommandHandler

@run_async

def truth(update: Update, context: CallbackContext):

    context.args

    update.effective_message.reply_text(random.choice(sing_and_joke_string.SING))

@run_async

def dare(update: Update, context: CallbackContext):

    context.args

    update.effective_message.reply_text(random.choice(sing_and_fun_string.JOKE))

TRUTH_HANDLER = DisableAbleCommandHandler("sing", sing)

DARE_HANDLER = DisableAbleCommandHandler("joke", joke)

dispatcher.add_handler(SING_HANDLER)

dispatcher.add_handler(JOKE_HANDLER)
