# 🧠 QR ID Bot (24x7 Free Telegram Bot)

यह Telegram बॉट हर बार जब आप इसे कोई QR कोड फोटो भेजते हैं, उस फोटो का **file_id** निकालता है।  
यह setup **Render + UptimeRobot** पर चलता है ताकि यह कभी sleep न हो।  

---

## 🚀 Deployment Steps

### 1️⃣ GitHub पर Upload करें
1. यह पूरा folder (`qr-id-bot`) GitHub पर upload करें।  
2. सभी फाइलें रहनी चाहिए:
   - `qr_id_bot.py`
   - `keep_alive.py`
   - `requirements.txt`
   - `render.yaml`

---

### 2️⃣ Render पर Deploy करें
1. [https://render.com](https://render.com) खोलें  
2. GitHub से लॉगिन करें  
3. “New Web Service” → अपना repo चुनें  
4. ये settings डालें 👇  

| Field | Value |
|-------|--------|
| Environment | Python |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python qr_id_bot.py` |
| Plan | Free |

5. नीचे **Environment Variables** में डालें:
   - Key: `BOT_TOKEN`
   - Value: `<अपना Telegram Bot Token>`

6. “Deploy” पर क्लिक करें ✅  

Render deploy होने के बाद आपको एक URL मिलेगा जैसे:  
```
https://qr-id-bot.onrender.com
```

---

### 3️⃣ UptimeRobot Setup (24x7 Active रखने के लिए)
1. [https://uptimerobot.com](https://uptimerobot.com) पर जाएं  
2. Account बनाएं → “Add New Monitor” पर क्लिक करें  
3. Type चुनें: `HTTP(s)`  
4. URL डालें: Render वाला URL  
5. Interval: 5 minutes  
6. Save करें ✅  

अब UptimeRobot हर 5 मिनट में Render को ping करेगा, जिससे बॉट कभी sleep नहीं होगा 🚀  

---

### ✅ Done!
अब आपका QR ID Bot हमेशा चालू रहेगा (Free Forever) 💯
