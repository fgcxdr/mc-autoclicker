import pyautogui
import time
import keyboard
import pydirectinput
import sys
import os

time.sleep(2)

# default afk
def default():
    # while True:
    pyautogui.click()
    time.sleep(30)


def pause_screen_active():
    resume_button_location = pyautogui.locateOnScreen('resume.png', confidence=0.9)
    return resume_button_location is not None
    
# stone farm / corral farm
def stone():
    d = 0
    pyautogui.mouseDown()
    while d<300000 and not pause_screen_active():
        d+=1
        time.sleep(1)
    pyautogui.mouseUp()
    return
        

def kelp_xp():
    # xp farm
    no_roasted_kelp_count = 0
    def wait_for_kelp():
        while True:
            arrow_part_location = pyautogui.locateOnScreen('smoker_10.png', confidence=0.70)
            roasted_kelp_top_location = pyautogui.locateOnScreen('roasted_kelp_top.png', confidence=0.90)
            if arrow_part_location and arrow_part_location:
                return True
            time.sleep(.01)
    while True:
        # use smoker
        pyautogui.click(button='right')
        # wait_for_kelp()
        # get roasted kelp screen location
        roasted_kelp_top_location = pyautogui.locateOnScreen('roasted_kelp_top.png', confidence=0.9)
        if roasted_kelp_top_location:
            no_roasted_kelp_count = 0
            roasted_kelp_top_center = pyautogui.center(roasted_kelp_top_location)
            # pyautogui.moveTo(roasted_kelp_top_center.x, roasted_kelp_top_center.y)
            pydirectinput.moveTo(roasted_kelp_top_center.x, roasted_kelp_top_center.y)
            # time.sleep(0.1)
            # move mouse scroll wheel to highlight roasted kelp
            # pyautogui.scroll(5)
            # time.sleep(1)
            # get roasted kelp from smoker, can be <1
            pyautogui.keyDown('shift') 
            pyautogui.click(button='right')
            pyautogui.keyUp('shift')
            # time.sleep(0.1)
            pydirectinput.moveTo(roasted_kelp_top_center.x-100, roasted_kelp_top_center.y-100)
            # exit smoker
        pyautogui.press('e')
        time.sleep(0.1)
        
            # time.sleep(1.0)
        # else:
        #     no_roasted_kelp_count += 1
        #     print(f"No roasted kelp found ({no_roasted_kelp_count}).")
        #     time.sleep(1.0)

    # total wait time is 5 seconds, which is how long it takes to roast kelp
    

            # return True
    # if roasted_kelp_top_location:
    #     no_roasted_kelp_count = 0
    #     roasted_kelp_top_center = pyautogui.center(roasted_kelp_top_location)
    #     # pyautogui.moveTo(roasted_kelp_top_center.x, roasted_kelp_top_center.y)e
    #     pydirectinput.moveTo(roasted_kelp_top_center.x, roasted_kelp_top_center.y)
    #     time.sleep(0.1)
    #     # move mouse scroll wheel to highlight roasted kelp
    #     # pyautogui.scroll(5)
    #     # time.sleep(1)
    #     # get roasted kelp from smoker, can be <1
    #     pyautogui.keyDown('shift') 
    #     pyautogui.click(button='right')
    #     pyautogui.keyUp('shift')
    #     time.sleep(0.1)
    #     pydirectinput.moveTo(roasted_kelp_top_center.x-100, roasted_kelp_top_center.y)
    #     # exit smoker
    #     pyautogui.press('e')
    # else:
    #     no_roasted_kelp_count += 1
    #     print(f"No roasted kelp found ({no_roasted_kelp_count}).")
    #     time.sleep(1.0)

    # # total wait time is 5 seconds, which is how long it takes to roast kelp
    # time.sleep(3)

def default():
    while True:
        pyautogui.click()
        time.sleep(30)

def forward():
    while True:
        pyautogui.keyDown('w')
        time.sleep(5)

def spider_farm():
    while not keyboard.is_pressed('esc'):
        pyautogui.click()
        time.sleep(0.1)

def tree_farm():
    while not keyboard.is_pressed('esc'):
        pyautogui.click(button='right')
        time.sleep(10)


def snow():
    while not pause_screen_active():
        craft_snow_location = pyautogui.locateOnScreen("craft_snow.png", confidence=0.95)
        if craft_snow_location:
            craft_snow_location_center = pyautogui.center(craft_snow_location)
            pydirectinput.moveTo(craft_snow_location_center.x, craft_snow_location_center.y)
            pyautogui.keyDown('shift') 
            pyautogui.click(button='right')
            pyautogui.keyUp('shift')
            pydirectinput.moveTo(craft_snow_location_center.x-100, craft_snow_location_center.y-100)
        time.sleep(1)

def raid_farm():
    def discard_item(location):
        location_center = pyautogui.center(location)
        pydirectinput.moveTo(location_center.x, location_center.y)
        time.sleep(0.1)
        pyautogui.keyDown('ctrl') 
        pyautogui.keyDown('q') 
        pyautogui.keyUp('q')
        pyautogui.keyUp('ctrl')
        time.sleep(0.1)

    items_to_discard = ["saddle.png","crossbow.png","enchanted_crossbow.png","enchanted_iron_axe.png","iron_boots.png","iron_chestplate.png"]
    while not keyboard.is_pressed('esc'):
        inventory_location = pyautogui.locateOnScreen("inventory.png", confidence=0.9)
        large_chest_location = pyautogui.locateOnScreen("large_chest.png", confidence=0.9)
        for item_to_discard in items_to_discard:
            item_location = pyautogui.locateOnScreen(item_to_discard, confidence=0.8)
            print(item_to_discard, item_location , inventory_location , large_chest_location , pyautogui.center(item_location).y > pyautogui.center(inventory_location).y , pyautogui.center(item_location).y < pyautogui.center(large_chest_location).y)
            if item_location and inventory_location and large_chest_location and pyautogui.center(item_location).y > pyautogui.center(inventory_location).y and pyautogui.center(item_location).y < pyautogui.center(large_chest_location).y:
                discard_item(item_location)
        # crossbow_location = pyautogui.locateOnScreen('crossbow.png', confidence=0.5)
        # if crossbow_location:
        #     discard_item(crossbow_location)

        # total wait time is 5 seconds, which is how long it takes to roast kelp
        time.sleep(3)


ENCHANTMENT_BOOK_IMAGES = os.listdir("enchantment_books")

def get_enchantment_book():
    book_location = None
    for image in ENCHANTMENT_BOOK_IMAGES:
        book_location = pyautogui.locateOnScreen(f"enchantment_books/{image}", confidence=0.7)
        if book_location:
            print(image, book_location)
            return (image, book_location)
    

def trades():

    while not pause_screen_active():
        keyboard.press('s')
        time.sleep(0.5)
        keyboard.release('s')
        time.sleep(0.75)
        keyboard.press('w')
        time.sleep(0.75)
        keyboard.release('w')
        time.sleep(2)
        pyautogui.click(button='right')
        time.sleep(0.25)
        pydirectinput.moveTo(100, 100)
        time.sleep(0.25)
        book_trade_location = pyautogui.locateOnScreen("book_trade.png", confidence=0.9)
        if book_trade_location:
            book_trade_location_center = pyautogui.center(book_trade_location)
            pydirectinput.moveTo(book_trade_location_center.x+100, book_trade_location_center.y)
            pydirectinput.move(2, 2)
            book_image, book_location = get_enchantment_book()
            if not book_location:
                sys.exit()
        keyboard.press_and_release('e')
    # keyboard.press_and_release('esc')
        # time.sleep(3)

trades()

# def test():
#     time.sleep(5)
#     d=pyautogui.locateOnScreen("efficiency_4.png", confidence=0.7) 
#     print(d)
# wait_for_kelp()

# get_enchantment_book()

# for i in range(0,5000):
#     pyautogui.scroll(5)
#     time.sleep(3)