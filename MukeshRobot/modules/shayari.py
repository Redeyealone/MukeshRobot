import random
import asyncio
from pyrogram import filters
from MukeshRobot import pbot as MukeshRobot




ROMANTIC_STRINGS = [
                     'Meri chahat dekhni hai? \nTo mere dil par apna dil rakhkar dekh\nteri dhadkan naa bhadjaye to meri mohabbat thukra dena...',
                     'Tere ishq me is tarah mai neelam ho jao\naakhri ho meri boli aur main tere naam ho jau...',
                     'Nhi pta ki wo kabhi meri thi bhi ya nhi\nmujhe ye pta hai bas ki mai to tha umr bas usi ka rha...',
                     'Tumne dekha kabhi chand se pani girte hue\nmaine dekha ye manzar tu me chehra dhote hue...',
                     'Tera pata nahi par mera dil kabhi taiyar nahi hoga\nmujhe tere alawa kabi kisi aur se pyaar nhi hoga...',
                     'Lga ke phool haathon se usne kaha chupke se\nagar yaha koi nahi hota to phool ki jagah tum hote...',
                     'Jab Dhadkano Ko Tham Leta Hai Koi\nJab Khayalo Mein Naam Hamara Leta Hai koi,\nYaade Tab aur Yaadgar Ban Jaati Hai,\nJab Hume Humse Behtar Jaan Leta Hai Koi.',
                     'Love is not what the mind thinks, but what the heart feels',
                     'You Smile When You Happy I Smile When I See You Happy.',
                     'Never Forget About The Ones That Love You Back \n 💓 @Mukhushi_official',
                     'Loving The Right Person Will Make You The Strongest And The Most Confident Person.\n 💓 @Mukhushi_official ',
                     'Come live in my heart and pay no rent \n @💓 @Mukhushi_official',
                     'What You Say And What You Do Both Matters When You Are In Love.\n 💓 @Mukhushi_official',
                     'Falling In Love Is Easy But Keeping A Relationship Together Isn’t Easy.\n 💓 @Mukhushi_official',
                     'Start Spreading Love Instead Of Searching For It.\n 💓 @Mukhushi_official',
                     'Love Is In The Purest Form When There Are No Conditions In It.\n 💓 @Mukhushi_official',
                     'Loving Someone Constantly Forever Is Very Difficult, If You Can Do That Then No Force Can Bring You Down.\n 💓 @Mukhushi_official',
                     'I May Not Be Your First Love, But I Will Be Your Last Love.\n 💓 @Mukhushi_official',
                     'It Was My Dream To Wake Up Next To You, And Today My Dream Come True\n 💓 @Mukhushi_official',
                     'Love Can Make A Difference In Every Second Of Your Life.\n 💓 @Mukhushi_official',
                     'You Will Understand The Real Meaning Of Closeness Only When You Are Distant From Your Lover.\n 💓 @Mukhushi_official',
                     'The meeting of two personalities like the contact of two chemical substances: \nif there is any reaction, both are transformed.\n 💓 @Mukhushi_official',
                     'Every moment spent with you is a moment I treasure\n 💓 @Mukhushi_official',
                     'You are the first and last thing on my mind each and every day\n 💓 @Mukhushi_official',
                     'There is a peace when there is a love, Let’s love to create a peace\n 💓 @Mukhushi_official',
                     'I don’t want to be your number one, I want to be your only one.\n 💓 @Mukhushi_official',
                   ]


@MukeshRobot.on_message(filters.command("romantic", "love", "khushi"))
async def lel(bot, message):
    ran = random.choice(ROMANTIC_STRINGS)
    await bot.send_chat_action(message.chat.id, "Mukesh is typing")
    await asyncio.sleep(1.5)
    return await message.reply_text(text=ran)

__mod_name__ = "sʜᴀʏᴀʀɪ"

__help__ = """

ᴍᴀᴋᴇs ᴀ sʜᴀʏᴀʀɪ ғᴏʀ ᴜʀ ɢɪʀʟғʀɪᴇɴᴅ ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ.

❍ /romantic or /love *:* ᴡʀɪᴛᴇ sʜᴀʏᴀʀɪ 

 """
