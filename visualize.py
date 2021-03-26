# Created by Kamir Walton
#  Finished on 19Dec2020
# Implementing the sorting algorithms into a visualization
# Pure spaghetti code but hey, it works


import copy
import pygame
import random
import sys
import time


class Sorting:
    def __init__(self, array):
        self.array = array
        self.begin = 0
        self.end = len(array) - 1

    def show_bars(self, shade, x1, y1, wide):

        for num in range(len(self.array)):
            rect = pygame.Rect(x1 + 40 * num, y1, wide, -self.array[num])
            pygame.draw.rect(window, shade, rect)
        pygame.draw.rect(window, (0, 0, 0), (0, 400, 550, 7))

    def bubble_sort(self):
        global render, color, xx, xx2, vel
        color = (150, 50, 50)
        while True:

            for i in range(len(self.array)-1):

                for j in range(len(self.array) - i - 1):
                    if self.array[j] > self.array[j+1]:
                        t = self.array[j]
                        self.array[j] = self.array[j + 1]
                        self.array[j + 1] = t

                        render = font.render('Sorted!', True, (255, 255, 255))
                        window.fill(color=(0, 0, 0))
                        window.blit(image, (xx, 0))
                        window.blit(image, (xx2, 0))
                        if xx <= -500:
                            xx = 0
                        if xx2 <= 0:
                            xx2 = 500
                        else:
                            xx -= vel + 2.25
                            xx2 -= vel + 2.25
                        self.show_bars(color, x, y, width)

                        # Adding a delay between each swap
                        pygame.time.delay(100)

                        clock.tick(60)
                        # Updating the screen
                        pygame.display.update()

            color = (100, 255, 0)
            return self.array

    def insertion_sort(self):
        global color, render, xx, xx2, vel
        for i in range(1, len(self.array)):
            val = self.array[i]
            j = i - 1

            while j >= 0 and self.array[j] > val:
                color = (170, 170, 170)
                self.array[j+1] = self.array[j]
                j -= 1

                self.array[j+1] = val

                window.fill(color=(0, 0, 0))
                window.blit(image, (xx, 0))
                window.blit(image, (xx2, 0))
                if xx <= -500:
                    xx = 0
                if xx2 <= 0:
                    xx2 = 500
                else:
                    xx -= vel + 2.25
                    xx2 -= vel + 2.25
                self.show_bars(color, x, y, width)

                # Adding a delay between each swap
                pygame.time.delay(100)

                # Updating the screen
                pygame.display.update()
        color = (100, 255, 0)
        render = font.render('Sorted!', True, (255, 255, 255))

        # Updating the screen
        pygame.display.update()
        return self.array

    def quick_sort(self, end, begin=0):
        global render, color
        if begin >= end:
            color = (100, 255, 0)
            render = font.render('Sorted!', True, (255, 255, 255))
            pygame.display.update()
            return self.array

        color = (255, 153, 51)
        index = self.partition(self.array, begin, end)
        self.quick_sort(index - 1, begin)
        self.quick_sort(end, index + 1)

    def partition(self, arr, begin, end):
        pivot_index = begin
        pivot_val = arr[end]
        for i in range(begin, end):
            if arr[i] < pivot_val:
                self.swap(arr, i, pivot_index)
                pivot_index += 1

        self.swap(arr, pivot_index, end)

        return pivot_index

    @staticmethod
    def swap(arr, a, bb):
        global xx, xx2, vel
        time.sleep(0.05)
        temp = arr[a]
        arr[a] = arr[bb]
        arr[bb] = temp
        window.fill(color=(0, 0, 0))
        window.blit(image, (xx, 0))
        window.blit(image, (xx2, 0))
        if xx <= -500:
            xx = 0
        if xx2 <= 0:
            xx2 = 500
        else:
            xx -= vel + 1.5
            xx2 -= vel + 1.5
        b.show_bars(color, x, y, width)
        pygame.display.update()


def main_screen():
    global window, click, xx, xx2, vel
    vel = 0.5
    xx = 0
    xx2 = 825
    window = pygame.display.set_mode(size=(550, 400))

    bubble_button = pygame.Rect(50, 300, 100, 40)
    insertion_button = pygame.Rect(200, 300, 100, 40)
    quick_button = pygame.Rect(350, 300, 100, 40)

    box2 = render.get_rect(center=(165, 40))
    render_bubble = pygame.font.SysFont('arial', 15).render('Bubble Sort', True, (0, 0, 0))
    render_insertion = pygame.font.SysFont('arial', 15).render('Insertion Sort', True, (0, 0, 0))
    render_quick = pygame.font.SysFont('arial', 15).render('Quick Sort', True, (0, 0, 0))
    box_bubble = render_bubble.get_rect(center=(100, 318))
    box_insertion = render_insertion.get_rect(center=(250, 318))
    box_quick = render_quick.get_rect(center=(400, 318))
    window.blit(render_bubble, box_bubble)
    window.blit(render_insertion, box_insertion)
    window.blit(render_quick, box_quick)

    while True:
        pos = pygame.mouse.get_pos()
        window.fill((0, 0, 0))
        window.blit(image2, (xx, 0))
        window.blit(image2, (xx2, 0))
        pygame.draw.rect(window, (255, 255, 255), bubble_button)
        pygame.draw.rect(window, (255, 255, 255), insertion_button)
        pygame.draw.rect(window, (255, 255, 255), quick_button)
        window.blit(render_bubble, box_bubble)
        window.blit(render_insertion, box_insertion)
        window.blit(render_quick, box_quick)
        window.blit(font.render('Welcome to my Sorting Visualization!', True, (255, 255, 255)),
                    box2)

        if xx <= -825:
            xx = 0
        if xx2 <= 0:
            xx2 = 825
        else:
            xx -= vel
            xx2 -= vel

        click = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        # Determining the clicking event for each box
        if bubble_button.collidepoint(pos):
            pygame.draw.rect(window, (255, 255, 0), bubble_button)
            window.blit(render_bubble, box_bubble)
            if click:
                bubble_screen()
        if insertion_button.collidepoint(pos):
            pygame.draw.rect(window, (0, 255, 255), insertion_button)
            window.blit(render_insertion, box_insertion)
            if click:
                insertion_screen()
        if quick_button.collidepoint(pos):
            pygame.draw.rect(window, (255, 0, 255), quick_button)
            window.blit(render_quick, box_quick)
            if click:
                quick_screen()

        pygame.display.update()
        clock.tick(60)


def bubble_screen():
    global click, keys, start, xx, xx2, vel, temp_array, b, render
    running = True
    vel = 0.5
    xx = 0
    xx2 = 500
    window.fill((0, 0, 0))
    arrow_button = pygame.Rect(arrow.get_rect())

    while running:

        window.blit(image, (xx, 0))
        window.blit(image, (xx2, 0))
        window.blit(arrow, (0, 0))
        b.show_bars(color, x, y, width)
        window.blit(render, box)
        pos = pygame.mouse.get_pos()

        if arrow_button.collidepoint(pos):
            if click:
                temp_array = copy.deepcopy(rectangles)
                b = Sorting(temp_array)
                b.show_bars(color, x, y, width)
                render = font.render('Press Space To Sort', True, (255, 255, 255))
                pygame.display.update()
                running = False
        # Exit Strategy
        click = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    temp_array = copy.deepcopy(rectangles)
                    b = Sorting(temp_array)
                    b.show_bars(color, x, y, width)
                    render = font.render('Press Space To Sort', True, (255, 255, 255))
                    pygame.display.update()
                    running = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        if xx <= -500:
            xx = 0
        if xx2 <= 0:
            xx2 = 500
        else:
            xx -= vel
            xx2 -= vel

        start = False

        # Seeing what keys are pressed
        keys = pygame.key.get_pressed()

        # Starting the sort when the space key is pressed
        if keys[pygame.K_SPACE]:
            start = True

        # What happens when the game has started
        if start:
            b.bubble_sort()

        pygame.display.update()
        clock.tick(60)


def insertion_screen():
    global click, keys, start, xx, xx2, vel, render, b, temp_array
    running = True
    vel = 0.5
    xx = 0
    xx2 = 500
    window.fill((0, 0, 0))
    arrow_button = pygame.Rect(arrow.get_rect())

    while running:

        window.blit(image, (xx, 0))
        window.blit(image, (xx2, 0))
        window.blit(arrow, (0, 0))
        b.show_bars(color, x, y, width)
        window.blit(render, box)

        pos = pygame.mouse.get_pos()

        if arrow_button.collidepoint(pos):
            if click:
                temp_array = copy.deepcopy(rectangles)
                b = Sorting(temp_array)
                b.show_bars(color, x, y, width)
                render = font.render('Press Space To Sort', True, (255, 255, 255))
                pygame.display.update()
                running = False

        # Exit Strategy
        click = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    temp_array = copy.deepcopy(rectangles)
                    b = Sorting(temp_array)
                    b.show_bars(color, x, y, width)
                    render = font.render('Press Space To Sort', True, (255, 255, 255))
                    pygame.display.update()
                    running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        if xx <= -500:
            xx = 0
        if xx2 <= 0:
            xx2 = 500
        else:
            xx -= vel
            xx2 -= vel

        start = False

        # Seeing what keys are pressed
        keys = pygame.key.get_pressed()

        # Starting the sort when the space key is pressed
        if keys[pygame.K_SPACE]:
            start = True

        # What happens when the game has started
        if start:
            b.insertion_sort()

        pygame.display.update()
        clock.tick(60)


def quick_screen():
    global click, keys, start, xx, xx2, vel, render, b, temp_array
    running = True
    vel = 0.5
    xx = 0
    xx2 = 500
    window.fill((0, 0, 0))
    arrow_button = pygame.Rect(arrow.get_rect())

    while running:

        window.blit(image, (xx, 0))
        window.blit(image, (xx2, 0))
        window.blit(arrow, (0, 0))
        b.show_bars(color, x, y, width)
        window.blit(render, box)

        pos = pygame.mouse.get_pos()

        if arrow_button.collidepoint(pos):
            if click:
                temp_array = copy.deepcopy(rectangles)
                b = Sorting(temp_array)
                b.show_bars(color, x, y, width)
                render = font.render('Press Space To Sort', True, (255, 255, 255))
                pygame.display.update()
                running = False

        # Exit Strategy
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    temp_array = copy.deepcopy(rectangles)
                    b = Sorting(temp_array)
                    b.show_bars(color, x, y, width)
                    render = font.render('Press Space To Sort', True, (255, 255, 255))
                    pygame.display.update()
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if xx <= -500:
            xx = 0
        if xx2 <= 0:
            xx2 = 500
        else:
            xx -= vel
            xx2 -= vel

        start = False

        # Seeing what keys are pressed
        keys = pygame.key.get_pressed()

        # Starting the sort when the space key is pressed
        if keys[pygame.K_SPACE]:
            start = True

        # What happens when the game has started
        if start:
            b.quick_sort(len(rectangles)-1)

        pygame.display.update()
        clock.tick(60)


pygame.init()

# Creating window size
window = pygame.display.set_mode(size=(550, 500))

# Screen Title
pygame.display.set_caption('Sorting Algorithms')

# Font
font = pygame.font.SysFont('arial', 30)

# Displaying the Text
render = font.render('Press Space To Sort', True, (255, 255, 255))
box = render.get_rect(center=(250, 40))

# Positions
x = 40
y = 400
xx = 0
xx2 = 825
vel = 0.5

clock = pygame.time.Clock()

# Width of the bar
width = 20

# Color of the bars
color = (100, 255, 0)

# Array of rectangles
rectangles = []

for rand in range(12):
    r = random.randrange(10, 300)
    rectangles.append(r)

# I have to copy the array so it's possible to sort with the other algorithms
temp_array = copy.deepcopy(rectangles)
b = Sorting(temp_array)

# Initializing background images
image = pygame.image.load('pixel_bg.jpg')
image2 = pygame.image.load('main_pixel_bg.jpg')
arrow = pygame.image.load('arrow.png')

image = pygame.transform.scale(image, (550, 400))
image2 = pygame.transform.scale(image2, (825, 400))
arrow = pygame.transform.scale(arrow, (100, 50))
arrow.set_colorkey((0, 0, 0))

# Various housekeeping variables that keep the program from throwing any errors
start = False
click = False
keys = pygame.key.get_pressed()

# This is the start of the main game loop
main_screen()
