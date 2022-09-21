import asyncio
import os
import sys
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
env_vars = {}
if os.path.isfile('.device'):
    with open('.device') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            env_vars[key] = value.replace("\"", "")
else:
  print("error device in the file")
  sys.exit()

os.system('pip install -U klldFNv3')
os.system('clear')

import klldFNv3


client = klldFNv3.klldBot(
  device_id=env_vars['DEVICE_ID'],
  account_id=env_vars['ACCOUNT_ID'],
  secret=env_vars['SECRET']
)

try:
    client.run()
except Exception as e:
    print(e)
    print("Can't login because your device auths is probably wrong.")
