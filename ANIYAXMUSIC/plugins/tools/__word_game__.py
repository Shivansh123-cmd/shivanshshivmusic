import random
import io
import os
import json
from pyrogram import filters
from pyrogram.enums import ChatType
from ANIYAXMUSIC import app
from PIL import Image, ImageDraw, ImageFont
from ANIYAXMUSIC.core.mongo import mongodb

worddb = mongodb.wordgame_points
game_db = {}

# ------------------ DATABASE ------------------ #
async def add_score(user_id, chat_id, points):
    user = await worddb.find_one({"user_id": user_id, "chat_id": chat_id})
    
    if user:
        await worddb.update_one(
            {"user_id": user_id, "chat_id": chat_id},
            {"$inc": {"points": points}}
        )
    else:
        await worddb.insert_one({
            "user_id": user_id,
            "chat_id": chat_id,
            "points": points
        })

# ------------------ WORD LOAD ------------------ #
words_path = "ANIYAXMUSIC/assets/word.txt"

if os.path.exists(words_path):
    with open(words_path, "r", encoding="utf-8") as f:
        try:
            raw_words = json.load(f)
        except:
            f.seek(0)
            raw_words = f.read().splitlines()

    WORDS = [str(w).strip().upper() for w in raw_words if len(str(w).strip()) > 2]
else:
    WORDS = ["PYTHON", "TELEGRAM", "MUSIC", "BOT"]

# ------------------ GRID ------------------ #
def generate_grid(word):
    size = 10
    cell = 45
    img_size = size * cell

    grid = [['' for _ in range(size)] for _ in range(size)]

    r, c = random.randint(0, size-1), random.randint(0, size-len(word))
    for i in range(len(word)):
        grid[r][c+i] = word[i]

    for r in range(size):
        for c in range(size):
            if grid[r][c] == '':
                grid[r][c] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    img = Image.new('RGB', (img_size, img_size), color=(20, 20, 20))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    for r in range(size):
        for c in range(size):
            d.text((c*cell+12, r*cell+8), grid[r][c], fill=(255, 255, 255), font=font)
            d.rectangle([c*cell, r*cell, (c+1)*cell, (r+1)*cell], outline=(50, 50, 50))

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf

# ------------------ START GAME ------------------ #
@app.on_message(filters.command(["wordgame"]))
async def start_game(_, message):
    chat_id = message.chat.id

    if chat_id in game_db:
        return await message.reply_text("⚠️ Game already running!")

    word = random.choice(WORDS)
    hint = f"Starts: {word[0]} | Ends: {word[-1]} | Length: {len(word)}"

    img = generate_grid(word)

    msg = await message.reply_photo(
        img,
        caption=f"🧠 WORD GAME\n\n💡 {hint}\n🏆 1st=5pt | others=3pt\n⏳ No time limit"
    )

    game_db[chat_id] = {
        "word": word,
        "winners": []
    }

    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        try:
            await msg.pin()
        except:
            pass

# ------------------ ANSWER ------------------ #
@app.on_message(filters.text & ~filters.command(["wordgame", "stopword", "leaderboard"]))
async def check(_, message):
    chat_id = message.chat.id

    if chat_id not in game_db:
        return

    if not message.text or not message.from_user:
        return

    word = game_db[chat_id]["word"]

    if message.text.strip().upper() == word:
        user_id = message.from_user.id

        if user_id in game_db[chat_id]["winners"]:
            return

        game_db[chat_id]["winners"].append(user_id)

        pos = len(game_db[chat_id]["winners"])
        pts = 5 if pos == 1 else 3

        await add_score(user_id, chat_id, pts)

        await message.reply_text(f"🌟 {message.from_user.mention} got it! (+{pts})")

        if pos >= 5:
            await end_game(message, chat_id)

# ------------------ END GAME ------------------ #
async def end_game(message, chat_id):
    winners = game_db[chat_id]["winners"]

    text = "🏁 <b>Game Over!</b>\n\n🏆 <b>Winners:</b>\n"

    for i, uid in enumerate(winners, start=1):
        text += f"{i}. <a href='tg://user?id={uid}'>Player</a>\n"

    del game_db[chat_id]

    await message.reply_text(text, disable_web_page_preview=True)

# ------------------ STOP ------------------ #
@app.on_message(filters.command("stopword"))
async def stop(_, message):
    chat_id = message.chat.id

    if chat_id in game_db:
        word = game_db[chat_id]["word"]
        del game_db[chat_id]
        await message.reply_text(f"🛑 Stopped! Word: {word}")

# ------------------ LEADERBOARD ------------------ #
@app.on_message(filters.command("leaderboard"))
async def leaderboard(_, message):
    args = message.text.split()

    mode = args[1] if len(args) > 1 else "chat"
    chat_id = message.chat.id

    text = "🏆 <b>Leaderboard</b>\n\n"

    if mode == "global":
        users = worddb.find().sort("points", -1).limit(10)
        text += "🌍 Global Top\n\n"

    else:
        users = worddb.find({"chat_id": chat_id}).sort("points", -1).limit(10)
        text += "👥 Chat Top\n\n"

    i = 1
    async for user in users:
        text += f"{i}. <a href='tg://user?id={user['user_id']}'>User</a> - {user['points']} pts\n"
        i += 1

    await message.reply_text(text, disable_web_page_preview=True)