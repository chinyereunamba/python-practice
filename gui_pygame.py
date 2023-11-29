import pygame
import sys
from random import randint


class TextBox:
    def __init__(self, x, y, width, height, font_size, tab_index):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)
        self.color = (0, 0, 0)
        self.active = False
        self.tab_index = tab_index

    def handle_event(self, event, all_boxes):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_TAB:
                next_box_index = (self.tab_index + 1) % len(all_boxes)
                self.active = False
                all_boxes[next_box_index].active = True
            else:
                self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))


class NumberGuessingGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 400
        self.screen_height = 300
        self.white = (255, 255, 255)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Number Guessing Game")
        self.font = pygame.font.Font(None, 36)

        self.guess_boxes = [
            TextBox(30, 100, 50, 50, 50, 0),
            TextBox(100, 100, 50, 50, 50, 1),
            TextBox(170, 100, 50, 50, 50, 2),
            TextBox(240, 100, 50, 50, 50, 3),
        ]

    def generate_number(self) -> list[int]:
        rnd_lst = set()

        while len(rnd_lst) < 4:
            rnd_lst.add(randint(0, 9))

        return list(rnd_lst)

    def draw_text(self, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def input_guess(self) -> list[int]:
        try:
            input_active = True
            current_box_index = 0

            while input_active:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    for box in self.guess_boxes:
                        box.handle_event(event, self.guess_boxes)

                self.screen.fill(self.white)
                self.draw_text("Enter your guess:", (0, 0, 0), 50, 50)
                for i, box in enumerate(self.guess_boxes):
                    box.draw(self.screen)
                    if box.active:
                        current_box_index = i

                pygame.display.flip()

            num_lst = [int(box.text) for box in self.guess_boxes]
            return num_lst

        except ValueError:
            raise ValueError("You must enter an integer")

    def start_game(self):
        life = 10
        guess_num = self.generate_number()

        while life > 0:
            guess = self.input_guess()
            life -= 1

            # Rest of your game logic here...

        pygame.quit()


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start_game()
