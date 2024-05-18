# This file was created by: Daniel Barandica

'''
# Sources: 
Geeks for Geeks: https://www.geeksforgeeks.org/working-images-python/?ref=gcse
ChatGPT OpenAI
'''


'''
Passions/Interests: 
- Food - Bellarmine
Project Title:
- Bellarmine
Goals: 
- be able to collect as many memories from Bellarmine as possible
- have all years available
- be able to import images of campus and friends
- have a number counter to count how many greetings/memories are collected, one for total
'''
import pygame
import sys

class HamburgerHerder:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 880, 640 #frame of screen
        self.FPS = 60 #frames per second of the game
        self.WHITE = (255, 255, 255) #RGB colors 
        self.MENU_ITEMS = ["Freshman", "Sophomore", "Junior", "Senior", "Graduation"] # list of menu items
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) #pygame display, with coordinates 
        pygame.display.set_caption("Hamburger Herder")
        self.item_images = { #map with images, each corresponding to one item
            "Freshman": pygame.image.load("double_double.png"), #every picture for every item section imported
            "Sophomore": pygame.image.load("cheeseburger.png"),
            "Junior": pygame.image.load("burger.png"),
            "Senior": pygame.image.load("fries.png"),
            "Graduation": pygame.image.load("shakes.png")
        } # all the images for the menu items, imported to display
    
        self.font = pygame.font.Font(None, 36) #any font, with size 36
        self.total_items = 0 #starting score count
        self.selected_item = None #store currently selected menu item
        self.current_screen = "menu" #indicates current location, either menu or item
        self.clock = pygame.time.Clock() #controlls frame rate


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.current_screen == "menu" and self.selected_item is not None:
                    self.current_screen = "item"
                    self.total_items += 1 #score from each initial click
                elif self.current_screen == "item":
                    self.handle_item_screen_click()



    def handle_item_screen_click(self):
        if 50 < pygame.mouse.get_pos()[0] < 200 and 50 < pygame.mouse.get_pos()[1] < 100:
            self.current_screen = "menu"
            self.selected_item = None
        else:
            self.total_items += 1 #how much your score increases every click


    def draw_menu_screen(self):
        self.screen.blit(pygame.image.load("menu.png"), (0, 0)) #any vertical or horizontal shifts for menu image
        menu_text = self.font.render("Welcome!", True, (0, 0, 0)) #makes font color black, can change with RGB numbers, displays greeting
        self.screen.blit(menu_text, (50, 0)) #vertical or horizontal shifts for the greeting, "welcome"
        for i, item in enumerate(self.MENU_ITEMS):
            text = self.font.render(item, True, (0, 0, 0)) #makes menu items in font color black
            self.screen.blit(text, (50, 40 + i * 110)) #starting coordinate for first menu item, spacing for each word after
            if pygame.Rect(50, 40 + i * 110, text.get_width(), text.get_height()).collidepoint(pygame.mouse.get_pos()): #location where the clicks register for each item
                self.selected_item = item #



    def draw_item_screen(self):
        self.screen.blit(self.item_images[self.selected_item], (60, 60)) #coordinates of menu button for return
        item_text = self.font.render(f"You got {self.selected_item} year! Click for more!", True, (255, 0, 0)) #text and color of what you ordered and to click more
        self.screen.blit(item_text, (220, 50)) #coordinates the text presented of what you ordered
        back_button = pygame.draw.rect(self.screen, (200, 0, 0), (50, 50, 150, 50)) #coordinates and color of button 
        back_text = self.font.render("Menu", True, (255, 255, 255)) # color and coordinates of the text "Menu"
        self.screen.blit(back_text, (60, 60))


    def draw_total_items_counter(self):
        counter_text = self.font.render(f"Total Items: {self.total_items}", True, (255, 0, 0)) #color of item tracker
        self.screen.blit(counter_text, (50, self.HEIGHT - 100))



    def update_display(self):
        pygame.display.flip()
        self.clock.tick(self.FPS)


    def run(self):
        self.running = True
        while self.running:
            self.screen.fill(self.WHITE)
            self.handle_events()
            if self.current_screen == "menu":
                self.draw_menu_screen()
            elif self.current_screen == "item":
                self.draw_item_screen()
            self.draw_total_items_counter()
            self.update_display()
        pygame.quit()
        sys.exit()


# Run the game
game = HamburgerHerder()
game.run()
