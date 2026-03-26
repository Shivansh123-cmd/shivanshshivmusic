<h1 align="center">  
    ─˹ 𝐘ᴜᴋɪ ꭙ ᴍᴜsɪᴄ ˼─  
</h1>  <p align="center">  
  <img src="https://readme-typing-svg.herokuapp.com/?lines=WELCOME+TO+YUKI+MUSIC+REPO;THIS+IS+AN+ADVANCED+MUSIC+BOT;POWERED+BY+SUDEEP+BOSS" alt="Typing SVG">  
</p>  <p align="center">  
  <img src="https://graph.org/file/90ef1bc444de679d65209-335d94a31975f4eda6.jpg" width="600" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">  
</p>  <p align="center">  
  <img src="https://readme-typing-svg.herokuapp.com/?lines=FORK+THIS+REPO+BEFORE+DEPLOY;STAR+THIS+REPO+IF+YOU+LIKE+IT" alt="Typing SVG">  
</p>  ---

⚠️ 𝗗𝗜𝗦𝗖𝗟𝗔𝗜𝗠𝗘𝗥

«Note: Please don't use your real/main Telegram account as an assistant.
The assistant account might leave all groups & channels automatically.
You may lose group ownership/admin rights.
Always use a spare/fake account.»

---

🖇 Generating Pyrogram String Session

Before deploying, generate a Pyrogram V2 String Session:

<p align="center">  
<a href="https://t.me/SessionStringZbot">  
<img src="https://img.shields.io/badge/Generate%20String%20Session-blueviolet?style=for-the-badge&logo=appveyor" width="250"/>  
</a>  
</p>  ---

<h2 align="center">─「 ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅs 」─</h2>🚀 DEPLOY ON HEROKU

<p align="center">  
<a href="https://dashboard.heroku.com/new?template=https://github.com/SUDEEPBOTS/YUKIMUSIC">  
<img src="https://img.shields.io/badge/Deploy%20On%20Heroku-green?style=for-the-badge&logo=heroku" width="220">  
</a>  
</p>  ---

💻 DEPLOY ON VPS / LOCALHOST (Python 3.11 + VENV)

1️⃣ Update System

sudo apt update && sudo apt upgrade -y

---

2️⃣ Install Python 3.11

sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

sudo apt install python3.11 python3.11-venv python3.11-dev -y

---

3️⃣ Install Required Packages

sudo apt install ffmpeg git curl nano nodejs npm -y

---

4️⃣ Install PM2

sudo npm install -g pm2

---

5️⃣ Clone Repository

git clone https://github.com/SUDEEPBOTS/YUKIMUSIC.git
cd YUKIMUSIC

---

6️⃣ Create Virtual Environment (IMPORTANT)

python3.11 -m venv venv
source venv/bin/activate

---

7️⃣ Install Requirements

pip install --upgrade pip
pip install -r requirements.txt

---

8️⃣ Setup Environment Variables

cp sample.env .env
nano .env

---

9️⃣ Start Bot (PM2 - 24/7)

pm2 start "venv/bin/python -m YUKIMUSIC" --name YukiBot
pm2 save

---

🔍 Check Logs

pm2 logs YukiBot

---

<h2 align="center">─「 ᴄᴏɴᴛᴀᴄᴛ & sᴜᴘᴘᴏʀᴛ 」─</h2><p align="center">  
<a href="https://t.me/Zcziiy">  
<img src="https://img.shields.io/badge/Owner-Telegram-blue?style=for-the-badge&logo=telegram">  
</a>  
</p>  <p align="center">  
<b>Owner Telegram:</b> <a href="https://t.me/Zcziiy">@Zcziiy</a>  
</p>
