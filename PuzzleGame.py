from bangtal import *
import random

scene2 = Scene("GameStart", "images/배경1.png")

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)


############################################3
#scene1

#restart 버튼
rs_btn = Object("images/restart.png")
rs_btn.locate(scene2, 10, 300)
rs_btn.setScale(0.7)
rs_btn.show()


#end 버튼
e_btn = Object("images/end.png")
e_btn.locate(scene2, 10, 250)
e_btn.setScale(0.7)
e_btn.show()

def e_btn_onMouseAction(x, y, action):
    endGame()
e_btn.onMouseAction = e_btn_onMouseAction


def find_index(object):
    for index in range(9):
        if p[index] == object:
            return index


def movable(index):
    if index < 0: return False
    if index > 8: return False
    if index % 3 > 0 and index - 1 == a: return True
    if index % 3 < 2 and index + 1 == a: return True
    if index > 2 and index - 3 == a: return True
    if index < 6 and index + 3 == a: return True
    return False


def move(index):
    global a
    p[index].locate(scene2, 100 + (340 * (a % 3)), 470 - (230 * (a // 3)))
    p[a].locate(scene2, 100 + (340 * (index % 3)), 470 - (230 * (index // 3)))

    object = p[index]
    p[index] = p[a]
    p[a] = object
    a = index


def completed():
    for index in range(9):
        if p[index] != init_p[index]:
            return False
    return True


d = [-1, 1, -3, 3]
def random_move():
    while True:

        index = a + d[random.randrange(4)] 
        if movable(index):  break
    move(index)


def onMouseAction_p(object, x, y, action):
    index = find_index(object)
    if movable(index):
        move(index)
        if completed():
            showMessage("성공~")
Object.onMouseActionDefault = onMouseAction_p


p = []
init_p = []
#정답 퍼즐 배열
for i in range(9):
    piece = Object("images/{}.png".format(str(i+1)))
    piece.locate(scene2, 100 + (340 * (i % 3)), 470 - (230 * (i // 3)))
    piece.show()

    p.append(piece)
    init_p.append(piece)

a = 8   #빈칸
p[a].hide()


cnt = 5
timer = Timer(1)
def onTimeout():
    random_move()
    global cnt
    print(cnt)
    cnt = cnt - 1
    if cnt > 0:
        timer.set(0.1)
        timer.start()
timer.onTimeout = onTimeout







time = Timer(10.0)
showTimer(time)
def onTimeout2():
    showMessage("타임오버~ 실패!!")
time.onTimeout = onTimeout2

#reset 버튼
def rs_btn_onMouseAction(x, y, action):
    time.stop()
    time.set(10.0)
    time.start()
rs_btn.onMouseAction = rs_btn_onMouseAction








timer.start()
time.start()
############################################3
startGame(scene2)