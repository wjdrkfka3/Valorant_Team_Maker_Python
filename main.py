# PyQT 5.0 버전과, 아나콘다 Python 3.6 버전을 사용했습니다.
# PyCharm을 사용하는 경우 File->Settings->Project Interpreter 를 아나콘다 Python 3.6으로 설정해줘야 코드가 올바르게 동작합니다.
import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        # ----- 위젯 생성 시작 -----
        self.player_list = []

        global listWidget
        listWidget = QListWidget()  # 리스트박스
        listWidget.setFixedSize(150, 250)  # 사이즈 조절

        global nickNameBox
        nickNameBox = QLineEdit()  # 닉네임박스
        nickNameBox.setFixedSize(130, 20)  # 사이즈 조절
        nickNameBox.returnPressed.connect(self.moveToListWidget)  # 엔터 칠때 함수 moveToListWidget에 연결

        global btn_add
        btn_add = QPushButton('추 가')  # 추가 버튼
        # btn_add.setFixedSize(70, 30) # 사이즈 조절
        btn_add.clicked.connect(self.moveToListWidget)  # 버튼 누를 때 함수 btn_add_Function에 연결

        global btn_delete
        btn_delete = QPushButton('삭 제')  # 삭제 버튼
        btn_delete.clicked.connect(self.btn_delete_Function)  # 버튼 누를 때 함수 btn_delete_Function에 연결

        global txt_setNum
        txt_setNum = QLabel('참여 인원 :')  # 참여 인원 선택 텍스트

        global txt_memberCount
        txt_memberCount = QLabel(str(listWidget.count())+' 명')

        global btn_makeTeam
        btn_makeTeam = QPushButton('팀 생성하기')  # 팀 생성하기 버튼


        btn_makeTeam.clicked.connect(self.makeTeamOK)
        # btn_makeTeam.clicked.connect(self.suffleTeam)
        # btn_makeTeam.clicked.connect(self.insertTeam)
        # btn_makeTeam.clicked.connect(self.suffleMap)

        btn_makeTeam.setFixedSize(120, 50)  # 사이즈 조절
        btn_makeTeam.setCheckable(True)  # 선택 가능하게 하기
        btn_makeTeam.setChecked(True)  # 선택 되어있게 하기

        global btn_exit
        btn_exit = QPushButton('종료')  # 종료 버튼
        btn_exit.clicked.connect(QCoreApplication.instance().quit)

        global items
        items = []

        global m_items
        m_items = [0, 1, 2, 3]

        global lbl_maps
        lbl_maps = [QLabel('1경기 : 스플릿'), QLabel('2경기 : 바인드'), QLabel('3경기 : 헤이븐'), QLabel('4경기 : 어센트')]

        global num
        num = []
        for i in range(40):
            num.append(QLabel())

        self.player_list = list(range(1, 41))

        global lbl_imgmaps
        lbl_imgmaps = [QLabel(), QLabel(), QLabel(), QLabel()]

        global img_split
        img_split = QPixmap('split.jpg')

        global img_haven
        img_haven = QPixmap('haven.jpg')

        global img_ascent
        img_ascent = QPixmap('ascent.jpg')

        global img_bind
        img_bind = QPixmap('bind.jpg')

        lbl_imgmaps[0].setPixmap(QPixmap(img_split.scaledToWidth(150)))
        lbl_imgmaps[1].setPixmap(QPixmap(img_haven.scaledToWidth(150)))
        lbl_imgmaps[2].setPixmap(QPixmap(img_bind.scaledToWidth(150)))
        lbl_imgmaps[3].setPixmap(QPixmap(img_ascent.scaledToWidth(150)))

        pixmap = QPixmap('logo_civil_war.png')  # 상단 로고 설정
        lbl_logo = QLabel()  # 레이블 활용하여 로고 설정

        lbl_logo.setPixmap(QPixmap(pixmap.scaledToWidth(600)))  # 사이즈 조절 (비율에 맞춰서)

        # ----- 위젯 생성 끝 -----

        # ----- 레이아웃 세부 설정 -----

        layout_top_right_high = QHBoxLayout()
        layout_top_right_high.addWidget(self.mapBox1())
        layout_top_right_high.addWidget(self.mapBox2())

        layout_top_right_low = QHBoxLayout()
        layout_top_right_low.addWidget(self.mapBox3())
        layout_top_right_low.addWidget(self.mapBox4())

        layout_top_right = QVBoxLayout()
        layout_top_right.addLayout(layout_top_right_high)
        layout_top_right.addLayout(layout_top_right_low)

        layout_top_left = QVBoxLayout()
        layout_top_left.addWidget(self.executeBox())
        layout_top_left.addWidget(self.modifyBox())
        # mid_right1.addWidget(self.mapBox())

        # layout_top
        layout_top = QHBoxLayout()
        layout_top.addWidget(listWidget)  # 리스트박스 추가
        layout_top.addLayout(layout_top_left)
        layout_top.addLayout(layout_top_right)
        # hbox.addWidget(self.modifyBox())  # 수정 그룹박스 추가
        # hbox.addWidget(self.executeBox())  # 팀 생성 그룹박스 추가
        # hbox.addWidget(self.mapBox())  # 맵 선택 그룹박스 추가

        # layout_mid
        layout_mid = QHBoxLayout()
        layout_mid.addStretch(1)
        for i in range(4):
            layout_mid.addWidget(self.team_groupbox(i+1))
            if (i+1) % 2 == 0:
                layout_mid.addStretch(1)

        # layout_bottom
        layout_bottom = QHBoxLayout()
        layout_bottom.addStretch(1)
        for i in range(4):
            layout_bottom.addWidget(self.team_groupbox(i+5))
            if (i+5) % 2 == 0:
                layout_bottom.addStretch(1)

        # layout_main
        layout_main = QVBoxLayout()
        layout_main.addWidget(lbl_logo)  # 세로 첫줄 로고 추가
        layout_main.addLayout(layout_top)
        layout_main.addStretch(1)
        layout_main.addLayout(layout_mid)
        layout_main.addLayout(layout_bottom)
        layout_main.addStretch(1)

        # ----- 레이아웃 세부 설정 끝 -----

        # 기본 설정들
        self.setLayout(layout_main)  # 레이아웃 설정
        self.setWindowTitle('sVeT clan 발로란트 내전 팀 생성기')  # 프로그램 제목 설정
        self.setWindowIcon(QIcon('icon_svet.ico'))  # sVeT 클랜 아이콘 설정
        self.setFixedSize(600, 900)  # 창 사이즈 조절
        self.center()  # 창 가운데 함수 실행
        self.show()

    def center(self):  # 창 가운데 함수
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def btn_delete_Function(self):  # 삭제 버튼 함수
        removeItemText = listWidget.currentRow()
        listWidget.takeItem(removeItemText)
        txt_memberCount.setText(str(listWidget.count()) + ' 명')

    def moveToListWidget(self):  # 엔터 버튼 함수
        if not nickNameBox.text():
            reply = QMessageBox.warning(self, '경고', '닉네임을 네모칸에 입력 후<br>추가버튼을 눌러 추가해주세요.')
        elif (listWidget.count()>39):
            reply = QMessageBox.warning(self, '경고', '최대 인원인 40명을 초과할 수 없습니다.')
        else:
            addItemText = nickNameBox.text()
            listWidget.addItem(addItemText)
            nickNameBox.clear()
        txt_memberCount.setText(str(listWidget.count()) + ' 명')

    def makeTeamOK(self):
        if (listWidget.count()==0):
            reply = QMessageBox.warning(self, '경고', '추가된 인원이 없어 팀을 생성할 수 없습니다.')
        else:
            reply = QMessageBox.warning(self, '팀 생성 완료', '팀 생성이 완료되었습니다.')
            self.suffleTeam()
            self.insertTeam()
            self.suffleMap()


    def suffleTeam(self):
        items.clear()
        for index in range(listWidget.count()):
            items.append(listWidget.item(index).text())
        random.shuffle(items)

    def suffleMap(self):
        random.shuffle(m_items)
        for i in range(0, 4):
            if (m_items[i] == 0):
                # 스플릿
                lbl_maps[i].setText(str(i + 1) + '경기 : 스플릿')
                lbl_imgmaps[i].setPixmap(QPixmap(img_split.scaledToWidth(150)))
            elif (m_items[i] == 1):
                # 바인드
                lbl_maps[i].setText(str(i + 1) + '경기 : 바인드')
                lbl_imgmaps[i].setPixmap(QPixmap(img_bind.scaledToWidth(150)))
            elif (m_items[i] == 2):
                # 헤이븐
                lbl_maps[i].setText(str(i + 1) + '경기 : 헤이븐')
                lbl_imgmaps[i].setPixmap(QPixmap(img_haven.scaledToWidth(150)))
            elif (m_items[i] == 3):
                # 어센트
                lbl_maps[i].setText(str(i + 1) + '경기 : 어센트')
                lbl_imgmaps[i].setPixmap(QPixmap(img_ascent.scaledToWidth(150)))


    def insertTeam(self):
        for i in range(len(items)):
            self.player_list[i] = items[i]
            num[i].setText(self.player_list[i])
        for i in range(len(items), 40):
            num[i].clear()

    def team_groupbox(self, team_num):
        end_idx = team_num * 5
        start_idx = end_idx - 5
        groupbox = QGroupBox('Team #'+str(team_num))
        vbox = QVBoxLayout()
        for i in range (start_idx, end_idx):
            vbox.addWidget(num[i])
        groupbox.setLayout(vbox)
        groupbox.setFixedSize(130, 180)
        return groupbox

    def modifyBox(self):
        groupbox = QGroupBox()
        grid = QGridLayout()
        grid.addWidget(txt_setNum, 0, 0)  # 현재 참여 인원 텍스트 추가
        grid.addWidget(txt_memberCount, 0, 1)  # 현재 참여 인원 카운트 추가
        grid.addWidget(nickNameBox, 1, 0)  # 닉네임박스 추가
        grid.addWidget(btn_add, 2, 0)  # 추가 버튼 추가
        grid.addWidget(btn_delete, 2, 1)  # 삭제 버튼 추가
        # groupbox.setFlat(True)
        groupbox.setLayout(grid)
        groupbox.setFixedSize(150, 120)  # 사이즈 조절
        return groupbox

    def executeBox(self):
        groupbox = QGroupBox()
        grid = QGridLayout()

        version = QLabel('Ver 2.0')

        grid.addWidget(btn_makeTeam, 0, 0)
        grid.addWidget(version, 1, 0)
        grid.addWidget(btn_exit, 1, 3)
        groupbox.setLayout(grid)
        groupbox.setFixedSize(150, 120)  # 사이즈 조절
        return groupbox

    # def mapBox(self):
    #     groupbox = QGroupBox('맵 선택')
    #     grid = QGridLayout()
    #     text1 = QLabel('1경기 :')
    #     text2 = QLabel('2경기 :')
    #     text3 = QLabel('3경기 :')
    #     text4 = QLabel('4경기 :')
    #
    #     map1 = QLabel('스플릿')
    #     map2 = QLabel('헤이븐')
    #     map3 = QLabel('바인드')
    #     map4 = QLabel('어센트')
    #
    #     grid.addWidget(text1, 0, 0)
    #     grid.addWidget(text2, 1, 0)
    #     grid.addWidget(text3, 2, 0)
    #     grid.addWidget(text4, 3, 0)
    #
    #     grid.addWidget(map1, 0, 1)
    #     grid.addWidget(map2, 1, 1)
    #     grid.addWidget(map3, 2, 1)
    #     grid.addWidget(map4, 3, 1)
    #
    #     groupbox.setLayout(grid)
    #     groupbox.setFixedSize(120, 120)  # 그룹박스 크기
    #     return groupbox

    def mapBox1(self):
        groupbox = QGroupBox()
        grid = QGridLayout()
        grid.addWidget(lbl_imgmaps[0], 0, 0)
        grid.addWidget(lbl_maps[0], 1, 0)
        groupbox.setLayout(grid)
        groupbox.setFixedSize(120, 120)
        return groupbox

    def mapBox2(self):
        groupbox = QGroupBox()
        grid = QGridLayout()
        grid.addWidget(lbl_imgmaps[1], 0, 0)
        grid.addWidget(lbl_maps[1], 1, 0)
        groupbox.setLayout(grid)
        groupbox.setFixedSize(120, 120)
        return groupbox

    def mapBox3(self):
        groupbox = QGroupBox()
        grid = QGridLayout()
        grid.addWidget(lbl_imgmaps[2], 0, 0)
        grid.addWidget(lbl_maps[2], 1, 0)
        groupbox.setLayout(grid)
        groupbox.setFixedSize(120, 120)
        return groupbox

    def mapBox4(self):
        groupbox = QGroupBox()
        grid = QGridLayout()
        grid.addWidget(lbl_imgmaps[3], 0, 0)
        grid.addWidget(lbl_maps[3], 1, 0)
        groupbox.setLayout(grid)
        groupbox.setFixedSize(120, 120)
        return groupbox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
