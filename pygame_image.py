import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01-20230613/fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk2_img = pg.transform.rotozoom(kk_img,10,1.0)
    sur = [kk_img,kk2_img]
    tmr = 0
    rad = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(sur[tmr%2],[300,200])
        tmr += 1    
        rad += 1
        if rad >= 10:
            rad *= -1
        if rad <= 0:
            rad *= -1
        pg.display.update()
        clock.tick(100)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()