from pyrogram import Client, filters
import threading
import schedule
import time

garants = { -1001200599203: "@getgarantbot", -1001264988679:"@DWDGARANTBOT",  -1001266598286: "@scrooge_garantbot", -1001332422950:"@lolzteam_garant_bot", -1001270089374:"@SynPro_bot", -1001263979488:"@AnonymusA_D_M_garant", -1001138196574:"@getgarantbot", -1001149599434:"@getgarantbot", -1001299642556:"@getgarantbot", -1001219032351:"@getgarantbot", -1001149743676:"@getgarantbot", -1001109809268:"@getgarantbot", -1001136430288:"@getgarantbot", -1001272479401:"@lolzteam_garant_bot"}

text = '''
💰 Продам комплект для пиара с помощью автопостинга

В комплект входит:
📨 Автопостинг
👤 Аккаунт с чатами
🧭 Хостинг для автопостинга

Цена: 500₽

Связь: @sqltop
Гарант: '''

app = Client("my_account")

def mailing():
    for i in garants.keys():
        garant = garants[i]
        try:
            app.send_photo(chat_id = i, photo = "banner.jpg" , caption = text + garant)
        except Exception as e:
            try:
                app.send_message(chat_id = i, text = text + garant)
            except Exception as e:
                pass


schedule.every(10).minutes.do(mailing)

def timer():
    while 1:
        schedule.run_pending()
        time.sleep(1)

t = threading.Thread(target=timer, name="тест")
t.start()

app.run();

