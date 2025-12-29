from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types import User
import json
import asyncio

# data dari my.telegram.org
api_id = '38' 
api_hash = 'e85'
phone_number = '+6285'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    print("Mengambil daftar kontak...")
    contacts = []
    
    result = await client(GetContactsRequest(hash=0))
    
    for contact in result.users:
        
        if isinstance(contact, User):
            contact_data = {
                'id': contact.id,
                'first_name': contact.first_name,
                'last_name': contact.last_name,
                'username': contact.username,
                'phone': contact.phone
            }
            contacts.append(contact_data)
    
    filename = 'contacts.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)
        
    print(f"Berhasil mengekspor {len(contacts)} kontak ke {filename}")

if __name__ == '__main__':
    client.start(phone=phone_number)
    
    with client:
        client.loop.run_until_complete(main())
