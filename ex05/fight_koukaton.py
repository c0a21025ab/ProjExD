import pygame as pg
import random
import sys
import time


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    global life, move, time_sta, time_end
    
    clock =pg.time.Clock()
    scr = Screen("いいからくたばれ！こうかとん", (1600,900), "fig/pg_bg.jpg")

    kkt = Bird("fig/6.png", 2.0, (900,400))
    time_sta = time.time()
    kkt.update(scr)

    #bkd = Bomb((255,0,0),10,(+1,+1),scr)
    #bkd.update(scr)

    bombs = []

    for i in range(8):
        color = "red"
        vx = random.choice([-3, -2, -1, +1, +2, +3])#爆弾横方向のスピードの調節
        vy = random.choice([-3, -2, -1, +1, +2, +3])#爆弾縦方向のスピードの調節
        vz = random.choice([10, 20])
        bombs.append(Bomb(color, vz, (vx,vy),scr))
    # 練習２
    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        Moji(80,(0,0,0), None,(10,10), f"{life}",scr)

        kkt.update(scr)
        #bkd.update(scr)
        for bomb in bombs:
            bomb.update(scr)
            if kkt.rct.colliderect(bomb.rct):
                time_end = time.time()
                if time_end-time_sta <= 1:#ゲーム開始後1秒以内の無敵時間
                    continue
                else:
                    move += 1
                    life -= 1
                    if life == 0:
                        Moji(160,(0,0,0), None,(450,380), "GAME OVER",scr)#GAMEOVERの表示
                        pg.display.update()
                        time.sleep(2)
                        return
                            
                    else:
                        Moji(160,(0,0,0), "ipaexg.ttf",(600,380), "痛っ",scr)#痛みを訴える表示
                        pg.display.update()
                        time.sleep(1)
                        main()
                        return
        
        pg.display.update()
        clock.tick(1000)

class Moji():
    def __init__(self, size, color, font, xy,txts,scr):
        fonto = pg.font.Font(font,size)
        txt = fonto.render(txts, True, color)
        scr.sfc.blit(txt, xy)


class Screen():
    def __init__(self, title, wh, img_path):
        # 練習１
        pg.display.set_caption(title)#にげろこうかとん
        self.sfc = pg.display.set_mode(wh)#１６００，９００
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)#fig/pg_bg.py
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird():
    key_delta = {
        pg.K_UP:    [0, -2],
        pg.K_DOWN:  [0, +2],
        pg.K_LEFT:  [-2, 0],
        pg.K_RIGHT: [+2, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)#"fig/6.png"
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)#2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy#900, 400

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self,scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb():
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)
        
if __name__ == "__main__":
    life = 5
    move = 0
    pg.init()
    main()
    pg.quit()
    sys.exit()