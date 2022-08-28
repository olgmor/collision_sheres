import wx
from findpointcollision import PointC0llision


class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(630, 350))

        self.win_interface()

    def win_interface(self):
        panel = wx.Panel(self)

        self.vbox = wx.BoxSizer(wx.VERTICAL)

        text = wx.StaticText(panel,
                             label="Программа преднозначена для вычисленния координат точки столкновения двух",
                             pos=(0, 0))
        text_2 = wx.StaticText(panel, label="сфер при их движении в пространстве.", pos=(0, 0))

        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font_1 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        text_2.SetFont(font)

        text_3 = wx.StaticText(panel, label="Введите начальные координаты,координаты через время t, радиус сферы1: ")
        text_3.SetFont(font)
        text_4 = wx.StaticText(panel, label="Введите начальные координаты,координаты через время t, радиус сферы2: ")
        text_4.SetFont(font)
        self.st1 = wx.TextCtrl(panel, value="")
        self.st2 = wx.TextCtrl(panel, value="1000 1000 1000 0 0 0 5")
        text_5 = wx.StaticText(panel, label="* координаты и радиус вводить через пробел(семь чисел на сферу)")

        self.vbox.Add(text, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.UP, border=10)
        self.vbox.Add(text_2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        self.vbox.Add(text_3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        self.vbox.Add(self.st1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        self.vbox.Add(text_4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        self.vbox.Add(self.st2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        self.vbox.Add(text_5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        but_run = wx.Button(panel, wx.ID_ANY, "Run")
        vbox_2 = wx.FlexGridSizer(3, 2, 5, 5)

        self.text_result_1 = wx.TextCtrl(panel, value="")
        self.text_result_2 = wx.TextCtrl(panel, value="")
        self.text_result_3 = wx.TextCtrl(panel, value="")

        self.text_6 = wx.StaticText(panel, label="координаты точки столкновения:")
        self.text_7 = wx.StaticText(panel, label="координаты сферы1 при столкновении:")
        self.text_8 = wx.StaticText(panel, label="координаты сферы2 при столкновении:")
        self.text_6.SetFont(font_1)
        self.text_7.SetFont(font_1)
        self.text_8.SetFont(font_1)
        vbox_2.Add(self.text_6, flag=wx.LEFT, border=5)
        vbox_2.Add(self.text_result_1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox_2.Add(self.text_7, flag=wx.LEFT, border=5)
        vbox_2.Add(self.text_result_2, flag=wx.ALL | wx.EXPAND, border=5)
        vbox_2.Add(self.text_8, flag=wx.LEFT, border=5)
        vbox_2.Add(self.text_result_3, flag=wx.ALL | wx.EXPAND, border=5)
        vbox_2.AddGrowableCol(1, 0)
        self.vbox.Add(vbox_2, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        box_3 = wx.BoxSizer()
        box_3.Add(but_run, flag=wx.LEFT, border=525)
        self.vbox.Add(box_3, proportion=1, flag=wx.DOWN | wx.EXPAND, border=10)
        but_run.Bind(wx.EVT_BUTTON, self.onStart)

        panel.SetSizer(self.vbox)

    def clear_text_ctrl(self):

        self.st1.SetValue("Семь чисел через пробел")
        self.st2.SetValue("Семь чисел через пробел")


    def onStart(self, event):
        validate_flag = True
        try:

            sphere1 = list(int(x) for x in self.st1.GetValue().split())
            sphere2 = list(int(x) for x in self.st2.GetValue().split())

            if len(sphere1) != 7 or len(sphere2) != 7:
                self.clear_text_ctrl()
                validate_flag = False
        except ValueError:
            self.clear_text_ctrl()
            validate_flag = False

        if validate_flag:
            v = PointC0llision()
            result = v.work(sphere1[:3], sphere1[3:6], sphere1[6], sphere2[:3], sphere2[3:6], sphere2[6])
            if result:
                result_cor_1 = str(result[0][:3])
                result_cor_2 = str(result[0][3:])
                result_cor_st = str(result[1:])

                self.text_result_1.SetValue(result_cor_st)
                self.text_result_2.SetValue(result_cor_1)
                self.text_result_3.SetValue(result_cor_2)

            else:
                self.text_result_1.SetValue("сферы не столкнутся")
                self.text_result_2.SetValue("сферы не столкнутся")
                self.text_result_3.SetValue("сферы не столкнутся")


app = wx.App()
frame = MyFrame(None, "Столкновение сфер")
frame.Center()
frame.Show()
app.MainLoop()
