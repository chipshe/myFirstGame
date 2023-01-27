import pygame,random

pygame.init()

GENISLIK,YUKSEKLIK = 500, 500

pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK))

lvlUp = pygame.mixer.Sound("levelUp.wav")
feed = pygame.mixer.Sound("pick.wav")

canavar = pygame.image.load("1.png")
canavarKoordinat = canavar.get_rect()
canavarKoordinat.topleft = (150,150)

yem = pygame.image.load("cent.png")
yemKoordinat = yem.get_rect()
yemKoordinat.topleft = (GENISLIK/2, YUKSEKLIK/2)

bonus = pygame.image.load("bonus.png")
bonusKoordinat = bonus.get_rect()
bonusKoordinat.topleft = (450,300)

font = pygame.font.SysFont("consolas",32)


HIZ = 9
saat = pygame.time.Clock()
FPS = 27

skor = 0
Y = 0

durum = True

while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False

    pencere.fill((0,0,0))
    pencere.blit(canavar,canavarKoordinat)
    pencere.blit(yem,yemKoordinat)
    pencere.blit(bonus,bonusKoordinat)

    yazi = font.render("Skor: "+str(skor),True,(255,0,0),(255,255,255))
    yaziKoordinat = yazi.get_rect()
    yaziKoordinat.topleft = (10,10)
    pencere.blit(yazi,yaziKoordinat)

    pygame.draw.line(pencere,(255,255,255),(0,60),(500,60),3)

    tus = pygame.key.get_pressed()
    if tus[pygame.K_LEFT] and canavarKoordinat.left > 0:
        canavarKoordinat.x-=HIZ
    elif tus[pygame.K_RIGHT] and canavarKoordinat.right < GENISLIK-10:
        canavarKoordinat.x+=HIZ
    elif tus[pygame.K_UP] and canavarKoordinat.top > 61:
        canavarKoordinat.y-=HIZ
    elif tus[pygame.K_DOWN] and canavarKoordinat.bottom < YUKSEKLIK-10:
        canavarKoordinat.y+=HIZ

    if canavarKoordinat.colliderect(yemKoordinat):
        feed.play()

        yemKoordinat.x = random.randint(0,GENISLIK-32)
        yemKoordinat.y = random.randint(61,YUKSEKLIK-32)

        skor+=1
    
    if canavarKoordinat.colliderect(bonusKoordinat):
        feed.play()

        bonusKoordinat.x = random.randint(0,GENISLIK-32)
        bonusKoordinat.y = random.randint(61,YUKSEKLIK-32)

        skor+=5
    
    if skor > 15:
        canavar = pygame.image.load("2.png")
        
        if Y == 0:
            lvlUp.play()

            canavarKoordinat = canavar.get_rect()
            canavarKoordinat.topleft = (100,100)

            tus = pygame.key.get_pressed()
            if tus[pygame.K_LEFT] and canavarKoordinat.left > 0:
                canavarKoordinat.x-=HIZ
            elif tus[pygame.K_RIGHT] and canavarKoordinat.right < GENISLIK:
                canavarKoordinat.x+=HIZ
            elif tus[pygame.K_UP] and canavarKoordinat.top > 61:
                canavarKoordinat.y-=HIZ
            elif tus[pygame.K_DOWN] and canavarKoordinat.bottom < YUKSEKLIK:
                canavarKoordinat.y+=HIZ

            if canavarKoordinat.colliderect(yemKoordinat):
                feed.play()

                yemKoordinat.x = random.randint(0,GENISLIK-32)
                yemKoordinat.y = random.randint(61,YUKSEKLIK-32)

                skor+=1

            Y +=1
    pygame.display.update()
    saat.tick(FPS)

pygame.quit()