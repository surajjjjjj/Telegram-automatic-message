from telethon import TelegramClient, events, sync
import time

#generate api id and hash on https://my.telegram.org
api_id = #enter api id
api_hash = #enter api hash
client = TelegramClient('session_name', api_id, api_hash)
client.start()
BCbot = client.get_entity('BTC_Faucet_freebot')
count=0
while 1:
    client.send_message(BCbot, 'Faucet bitchh')
    count=count+1
    print("Message sent | count = {0}".format(count))
    time.sleep(33)
end
