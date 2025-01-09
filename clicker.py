import keyboard
import time
import threading

multiplier = 1
f_state = False
cashmoney = int()
price = 50
upgrade = 0
upgrade_prompt = 0

def money():
    print(f"You have:{cashmoney} $.")

def wait_for_upgrade():
    global upgrade_prompt
    print(f"+1 money gain available for {price}$ to buy press y.")
    time.sleep(5)
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
            threading.Thread(target=wait_for_upgrade).start()
            upgrade_prompt = True
    if keyboard.is_pressed("y") and cashmoney >= price:
        multiplier += 1
        cashmoney -= price
        price += 50
        money()
#add an upgrade that makes passive money