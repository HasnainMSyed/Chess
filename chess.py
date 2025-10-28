import pygame

pygame.init()

Width = 500
Height = 450
screen = pygame.display.set_mode([Width, Height])
pygame.display.set_caption("Two Player Pygame Chess")
font = pygame.font.Font('freesansbold.ttf', 10)
big_font = pygame.font.Font('freesansbold.ttf', 25)

timer = pygame.time.Clock()
fps = 60

# Game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []


# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
PIECES = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
COLORS = ['black', 'white']
SIZES = {'large' : (40, 40), 'large_pawn':(32.5, 32.5), 'small': (22.5, 22.5)}

PIECES_IMAGES = {}
PIECES_SMALL_IMAGES = {}

for color in COLORS:
    for piece in PIECES:
        file_name = f"Assets/{color}_{piece}.png"

        try:
            base_image = pygame.image.load(file_name)
        except pygame.error as e:
            print(f"Error loading {file_name}, {e}")
            continue
    
        if piece == 'pawn':
            large_size = SIZES['large_pawn']
        else:
            large_size = SIZES['large']

        PIECES_IMAGES[f'{color}_{piece}'] = pygame.transform.scale(base_image, large_size)
        PIECES_SMALL_IMAGES[f'{color}_{piece}'] = pygame.transform.scale(base_image, SIZES['small'])


# check variables/ flashing counter
counter = 0
winner = ''
game_over = False


# Draw board function
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [300 - (column * 100), row * 50, 50, 50])
        else:
            pygame.draw.rect(screen, 'light gray', [350 - (column * 100), row * 50, 50, 50])
        pygame.draw.rect(screen, 'gray', [0, 400, Width, 50])
        pygame.draw.rect(screen, 'gold', [0, 400, Width, 50], 5)
        pygame.draw.rect(screen, 'gold', [400, 0, 100, Height], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (10, 410))

        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 50 * i),  (400, 50 * i), 2)
            pygame.draw.line(screen, 'black', (50 * i, 0),  (50 * i, 400), 2)



run = True
while (run):
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()