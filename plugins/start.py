from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel ❤️", url="https://t.me/anonymousbotz")],
        [InlineKeyboardButton("Group 🔰", url="https://t.me/anonymousbotzchat")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/networkchukka")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name} </b> I'm Youtube Download Bot. I Can Simply Download Any Youtube Single Video. I'll Not Support Playlist. Thank You For Start Me\n/help for More info 🙈"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
