import keyboard
import time
import threading

multiplier = 1
f_state = False
cashmoney = int()
price = 20
auto_upgrade_prompt = 0
upgrade_prompt = 0
want_propmpt = 1
auto_price = 40
auto_mult_price = 50
auto_timer_price = 50
mult_price = 60
auto_cash_multiplier = 0
auto_cash_timer = 10.2
auto_upgrade_bought = 0
auto_mult_prompt = 0
auto_timer_prompt = 0
auto_cash_fuse = 0



def money():
    print(f"You have:{cashmoney}$.")

def wait_for_upgrade():
    global upgrade_prompt #bez tohoto global by ze šedivěk upgrade_prompt na line 19 a přestal by fungovat
    print(f"+1 money gain available for {price}$ to buy press Y. If you dont want to upgrade and want this pop up to stop showing press N.")
    time.sleep(4)
    upgrade_prompt = False
def no_want_propmpt():
    global want_propmpt
    print("the Pop up will stop showing but you are still able to upgrade with Y.")
    want_propmpt = 0
def wait_for_auto_upgrade():
    global auto_upgrade_prompt
    print(f"auto cash gain upgrade availabe for {auto_price}$ press  X  to buy.If you dont want to upgrade and want this pop up to stop showing press N.")
    time.sleep(4)
    auto_upgrade_prompt = False
def wait_for_auto_mult_upgrade():
    global auto_mult_price, auto_mult_prompt
    print(f"auto multiplier + 10 cash gain available for {auto_mult_price}$ press  X  to buy.If you dont want to upgrade and want this pop up to stop showing press N.")
    time.sleep(4)
    auto_mult_prompt = False
def wait_for_auto_timer_upgrade():
    global auto_timer_price, auto_timer_prompt
    print(f"auto timer reduce by 0.3 seconds for {auto_timer_price}$ press  C  to buy.If you dont want to upgrade and want this pop up to stop showing press N.")
    time.sleep(4)
    auto_timer_prompt = False
def auto_upgrade_store():
    global auto_cash_multiplier, auto_upgrade_bought, auto_cash_timer, auto_price
    auto_cash_multiplier += 10
    auto_upgrade_bought = 1
    auto_cash_timer -= 0.2
    auto_price += auto_cash_multiplier
def auto_cash_multiplier_store():
    global auto_cash_multiplier, auto_mult_price
    auto_mult_price += 50
    auto_cash_multiplier += 10
def auto_cash_timer_store():
    global auto_timer_price, auto_cash_timer, cashmoney
    auto_timer_price += 50
    auto_cash_timer -= 0.3
    if auto_cash_timer <= 0:
        auto_cash_timer =0.1
def auto_cash():
    global cashmoney, auto_cash_timer, auto_cash_fuse
    while auto_cash_fuse == 1:
        time.sleep(auto_cash_timer)
        print(f"You gained {auto_cash_multiplier}$ from Auto Cash. Current balance: {cashmoney}$. Next payout in {auto_cash_timer} seconds.")
        cashmoney += auto_cash_multiplier
        auto_cash_fuse = 0



print("Press Q to Quit")
print("Press F to Gain Money.")

while True:
    if auto_upgrade_bought == 1 and auto_cash_fuse == 0:
        auto_cash_fuse = 1
        threading.Thread(target=auto_cash).start()
    if keyboard.is_pressed("f") and f_state == False:
        cashmoney += (multiplier)
        money()
        f_state = True
    elif keyboard.is_pressed("f") == False:
        f_state = False
        while cashmoney >= price and upgrade_prompt == False and want_propmpt == 1:
            threading.Thread(target=wait_for_upgrade).start() #pomocí tohoto jde klikat f a gainovat cash i když time.sleep(2.5) je aktivní (zapne ten def paralelně s hlavním programem)
            upgrade_prompt = True
        if keyboard.is_pressed("n") and want_propmpt == 1 and cashmoney >= price:
            threading.Thread(target=no_want_propmpt).start()
            time.sleep(0.2)
            breakpoint
    if keyboard.is_pressed("y") and cashmoney >= price:
        multiplier += 1
        cashmoney -= price
        price += 20
        want_propmpt = 1
        money()
        time.sleep(0.2)
    while cashmoney >= auto_price and auto_upgrade_prompt == False and want_propmpt == 1 and auto_upgrade_bought == 0:
        threading.Thread(target=wait_for_auto_upgrade).start()
        auto_upgrade_prompt = True
    while cashmoney >= auto_mult_price and auto_mult_prompt == False and want_propmpt == 1 and auto_upgrade_bought == 1:
        threading.Thread(target=wait_for_auto_mult_upgrade).start()
        auto_mult_prompt = True
    while cashmoney >= auto_timer_price and auto_timer_prompt == False and want_propmpt == 1 and auto_upgrade_bought == 1:
        threading.Thread(target=wait_for_auto_timer_upgrade).start()
        auto_timer_prompt = True
    if keyboard.is_pressed("x") and cashmoney >= auto_mult_price and auto_upgrade_bought == 1:
        cashmoney -= auto_mult_price
        threading.Thread(target=auto_cash_multiplier_store).start()
        money()
        time.sleep(0.2)
    if keyboard.is_pressed("C") and cashmoney >= auto_timer_price and auto_upgrade_bought == 1:
        cashmoney -= auto_timer_price
        threading.Thread(target=auto_cash_timer_store).start()
        money()
        time.sleep(0.2)
    if keyboard.is_pressed("x") and cashmoney >= auto_price and auto_upgrade_bought == 0:
        cashmoney -= auto_price
        threading.Thread(target=auto_upgrade_store).start()
        money()
        time.sleep(0.2)
    if keyboard.is_pressed("Q"):
        break


#add an upgrade that makes passive moneyf DONE
#add a 2x times to all multipliers upgrade or smth
#add html page so it dont run in visual code studio no more