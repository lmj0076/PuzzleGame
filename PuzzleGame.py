from bangtal import *
import random

scene1 = Scene("main", "images/배경1.png")
scene2 = Scene("GameStart", "images/배경1.png")

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)


############################################3
#scene1

photo = Object("images/원본1.png")
photo.locate(scene1, 200, 10)
photo.show()


#start 버튼
s_btn = Object("images/start.png")
s_btn.locate(scene1, 600, 300)
s_btn.setScale(1.8)
s_btn.show()


############################################3
#scene2

#타이머
time = Timer(20.0)
showTimer(time)

def time_onTimeout():
    showMessage("실패~ㅠㅠ")
time.onTimeout = time_onTimeout


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


p = []
check = p
pp = []
a = 7   #빈칸


#정답 퍼즐 배열
for i in range(9):
    p.append(Object("images/{}.png".format(str(i+1))))
    p[i].locate(scene2, 100 + (340 * (i % 3)), 470 - (230 * (i // 3)))
    p[i].hide()

    







#start 버튼 눌러서 퍼즐 섞기
rl = []
def s_btn_onMouseAction(x, y, action):
    ran_num = random.randint(0, 8)

    for j in range(9):
        while ran_num in rl:
            ran_num = random.randint(0, 8)
        rl.append(ran_num)


    #퍼즐 섞기
    for k in rl:
        pp.append(p[k])

    for m in range(9):
        pp[m].locate(scene2, 100 + (340 * (m % 3)), 470 - (230 * (m // 3)))
        pp[m].show()

    scene2.enter()
    time.start()

    pp[a].hide()
s_btn.onMouseAction = s_btn_onMouseAction



#reset 버튼
def rs_btn_onMouseAction(x, y, action):
    rl.clear()
    scene1.enter()
    time.stop()
    time.set(10.0)
rs_btn.onMouseAction = rs_btn_onMouseAction












############################################3
startGame(scene1)