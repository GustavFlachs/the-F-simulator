import keyboard
import time
import threading

multiplier = 1
f_state = False
cashmoney = int()
price = 20
upgrade = 0
upgrade_prompt = 0

def money():
    print(f"You have:{cashmoney} $.")

def wait_for_upgrade():
    global upgrade_prompt #bez tohoto global by ze šedivěk upgrade_prompt na line 19 a přestal by fungovat
    print(f"+1 money gain available for {price}$ to buy press y.")
    time.sleep(2.5)
    upgrade_prompt = False

print("Press F to gain money.")

while True:
    if keyboard.is_pressed("f") and f_state == False:
        cashmoney += (multiplier)
        money()
        f_state = True
    elif keyboard.is_pressed("f") == False:
        f_state = False
        if cashmoney >= price and upgrade_prompt == False:
            threading.Thread(target=wait_for_upgrade).start() #pomocí tohoto jde klikat f a gainovat cash i když time.sleep(2.5) je aktivní (zapne ten def paralelně s hlavním programem)
            upgrade_prompt = True
    if keyboard.is_pressed("y") and cashmoney >= price:
        multiplier += 1
        cashmoney -= price
        price += 20
        money()
#add an upgrade that makes passive money