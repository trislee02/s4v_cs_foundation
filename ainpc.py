from npc import NPC
from const import *
black = (0,0,0)
white = (255,255,255)
class AiNPC(NPC):
    def __init__(self):
        super().__init__()
        self.sentences = ["[AI]: Ban can ve kim tu thap level 5","[AI]: Ve nao"]

    def congrat(self,window):
        def drawTalkBox():
            width = 600
            height = 100
            x = 10
            y = HEIGHT - 130
            pg.draw.rect(window, white, (x, y, width, height))
        drawTalkBox()
        img = font.render("[AI]: Chuc mung ban!!!!!", True, black)
        window.blit(img, (20, HEIGHT - 120))

    