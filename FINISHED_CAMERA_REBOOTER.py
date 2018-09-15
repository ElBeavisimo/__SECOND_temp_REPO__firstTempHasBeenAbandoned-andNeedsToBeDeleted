import socket, pyautogui, pygame, sys, os
from time import sleep
dgramSock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
pygame.init()
clock = pygame.time.Clock()
os.environ['SDL_VIDEO_WINDOW_POS'] = '222, 333'
screen = pygame.display.set_mode((888, 55), pygame.RESIZABLE)
fnt = pygame.font.SysFont("impact", 44)


print '1 - MID BAR'
print '2 - POOL TABLE'
print '3 - FOYER 360'
print '4 - JUKE BOK'
print '5 - STAGE CAM'
print '6 - ICE MACHINE'
print '7 - REC ROOM'
print
print 'HIT THE NUMBER KEY OF THE CAMERA TO REBOOT...'
print 'OR HIT ANY OTHER KEY TO TERMINATE PROCESS'



def scanKEYBOARD():
    global ready
    global poynt

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            dgramSock.close()
            pygame.quit()
            sys.exit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                dgramSock.close()
                pygame.quit()
                sys.exit()
                quit()
               
            elif event.key == pygame.K_1:
                poynt = 1
            elif event.key == pygame.K_2:
                poynt = 2
            elif event.key == pygame.K_3:
                poynt = 3
            elif event.key == pygame.K_4:
                poynt = 4
            elif event.key == pygame.K_5:
                poynt = 5
            elif event.key == pygame.K_6:
                poynt = 6
            elif event.key == pygame.K_7:
                poynt = 7

            else:
                poynt = 0

    pygame.display.update()
    clock.tick(12)
    return



def sendUDP(): 
    webPkg = ('bad' + chr(48 + poynt) + 'LAN')
    dgramSock.sendto(webPkg, ('191.168.0.47', 60138))
    dgramSock.sendto(webPkg, ('174.71.248.169', 60138))
    return




def displayMsg(info):
    text = fnt.render(info, True, (255, 255, 255))               
    screen.fill((0,0,0))
    screen.blit(text,(1,1))
    pygame.display.update()    
    return




poynt = -16
sendUDP()
msg, (addr, port) = dgramSock.recvfrom(15)

if msg == 'READY' and port == 60138:
    info = 'Who is giving you trouble?'
    displayMsg(info)

    while poynt < 0:
        scanKEYBOARD()

    sendUDP()
    info, (addr, port) = dgramSock.recvfrom(49)
    displayMsg(info)

    if poynt > 0 and poynt < 8:
        info = 'Please wait 30 seconds for confirmation.'
        displayMsg(info)            
        info, (addr, port) = dgramSock.recvfrom(49)
        displayMsg(info)
    else:
        info = 'PROCESS TERMINATED - RESTART APP TO TRY AGAIN'
        displayMsg(info)


else:
    info = 'HARDWARE NOT READY - Try again'
    displayMsg(info)

sleep(5)

dgramSock.close()
pygame.quit()
sys.exit()
quit()




