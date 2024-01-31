import wx
import OpenAISetup


class SGGUI(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                         title="Ngholomennod's Study Guide Generator")
        self.panel = SGGUI_Panel(self)
        self.SetSize(770,300)
        self.Show()


class SGGUI_Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(self)
        instructions = wx.StaticText(self, label = "Please enter a course name followed by a topic like so -> (ex. "
                                                   "Computer Science, big-o notation) then click [Add Study-Guide]."
                                                   "\nAfter you add your guides, "
                                                   "clicking on the [Generate Study-Guide(s)] button will produce a "
                                                   "text file for each guide."
                                                   "\nEnter COURSE, TOPIC or COURSE, "
                "[TOPIC1, TOPIC2, TOPIC3]:")
        submit_btn = wx.Button(self, label='Generate Study-Guide(s)')
        submit_btn.Bind(wx.EVT_BUTTON, self.on_submit)
        add_btn = wx.Button(self, label='Add Study-Guide')
        add_btn.Bind(wx.EVT_BUTTON, self.on_add)

        self.list_ctrl = wx.ListCtrl(self, size=(-1, 100),
                                style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.row_obj_dict = {}
        self.list_ctrl.InsertColumn(0, '<Course, Topic(s)>', width=800)
        my_sizer.Add(instructions, 0, wx.ALL | wx.LEFT, 5)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        my_sizer.Add(add_btn, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(submit_btn, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(my_sizer)

    def on_add(self, event):
        message = self.text_ctrl.GetValue()
        if not message:
            print("You didn't enter anything!")
        else:
            print("Adding...")
            self.list_ctrl.InsertItem(0, message)


    def on_submit(self, event):
        index = 0
        while index < self.list_ctrl.GetItemCount():
            print("Communicating with OpenAI...")
            OpenAISetup.submit(self.list_ctrl.GetItemText(index))
            index+=1