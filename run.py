from telethon.sync import TelegramClient
import asyncio
import random

# data dari my.telegram.org
api_id = '38' 
api_hash = 'e85'
phone_number = '+6285'

import json
import os

def load_targets():
    try:
        with open('contacts.json', 'r', encoding='utf-8') as f:
            contacts = json.load(f)
            loaded_targets = [c['phone'] for c in contacts if c.get('phone')]
            return loaded_targets
    except FileNotFoundError:
        print("File contacts.json tidak ditemukan! Menggunakan list default.")
        return []

targets = load_targets()

if not targets:
    print("Tidak ada target yang ditemukan.")
    exit()

print(f"Berhasil memuat {len(targets)} target dari contacts.json")
pesan = "Halo! Ini adalah pesan otomatis dari program saya (testing)."

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    for target in targets:
        try:
            print(f"Mengirim pesan ke {target}...")
            await client.send_message(target, pesan)
            print(f"Berhasil terkirim ke {target}")
            
            delay = random.randint(15, 30)
            print(f"Menunggu {delay} detik...")
            await asyncio.sleep(delay)
            
        except Exception as e:
            print(f"Gagal mengirim ke {target}: {e}")

if __name__ == '__main__':
    client.start(phone=phone_number)
    
    with client:
        client.loop.run_until_complete(main())