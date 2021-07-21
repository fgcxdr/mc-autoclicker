import pyautogui
import time
import keyboard
import pydirectinput
import sys
import os



ENCHANTMENT_BOOK_IMAGES = os.listdir("enchantment_books")


def pause_screen_active():
    resume_button_location = pyautogui.locateOnScreen('resume.png', confidence=0.9)
    return resume_button_location is not None

def get_enchantment_book():
    book_location = None
    for image in ENCHANTMENT_BOOK_IMAGES:
        book_location = pyautogui.locateOnScreen(f"enchantment_books/{image}", confidence=0.7)
        if book_location:
            print(image, book_location)
            return (image, book_location)
    

def trades():

    while not pause_screen_active():
        # go backwards off of pressure plate
        keyboard.press('s')
        time.sleep(0.5)
        keyboard.release('s')
        time.sleep(0.75)
        # go forwards onto pressure plate
        keyboard.press('w')
        time.sleep(0.75)
        keyboard.release('w')
        # wait for villager to get new job
        time.sleep(4)
        pydirectinput.click(button='right')
        time.sleep(0.25)
        trading_arrow_location = pyautogui.locateOnScreen("trading_arrow.png", confidence=0.9)
        # after clicking on the villager, move the mouse away so it's not over the trade
        pydirectinput.moveTo(100, 100)
        time.sleep(0.25)
        #   Validate the villager is trading books by finding the book trade image.
        #   Confidence is how close the book_trade.png image needs to be to the image on screen -
        # Its not realistic for it to be a 100% match.  It may need to be lower depending on testing.
        book_trade_location = pyautogui.locateOnScreen("book_trade.png", confidence=0.9)
        if book_trade_location:
            # move to the book trade, then move to the right to mouse over the enchanted book.
            # I don't try to find the enchanted book image because its animated and is hard to match.
            book_trade_location_center = pyautogui.center(book_trade_location)
            pydirectinput.moveTo(book_trade_location_center.x+100, book_trade_location_center.y)
            pydirectinput.move(2, 2)
            book_image, book_location = get_enchantment_book()
            # Tf the book is not in the list of book images, the script exits.  This is useful so for adding more images to the list.
            # If the image for desired book is already saved (such as Efficiency V), the code would be: 
            # if book_image == "efficiency_5.png":
            if not book_location:
                sys.exit()
        # exit the villager trading menu if it is open
        if trading_arrow_location:
            keyboard.press_and_release('e')

if __name__ == "__main__":
    time.sleep(5)
    trades()
