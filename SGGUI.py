import wx
from wx import LIST_AUTOSIZE, LIST_FORMAT_CENTER

import OpenAISetup


class SGGUI(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                         title="Ngholomennod's Study Guide Generator")
        self.panel = SGGUI_Panel(self)
        self.SetSize(770, 360)
        self.Show()


class SGGUI_Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        course_label = wx.StaticText(self, label="Course")
        topic_label = wx.StaticText(self, label="Topic(s)")
        self.text_ctrl = wx.TextCtrl(self)
        self.text_ctrl2 = wx.TextCtrl(self)
        instructions = wx.StaticText(self, label="Please enter a course name followed by a topic like so -> (ex. "
                                                 "Computer Science, big-o notation) then click [Add Study-Guide]."
                                                 "\nAfter you add your guides, "
                                                 "clicking on the [Generate Study-Guide(s)] button will produce a "
                                                 "text file for each guide.\n")
        submit_btn = wx.Button(self, label='Generate Study-Guide(s)')
        submit_btn.Bind(wx.EVT_BUTTON, self.on_submit)
        add_btn = wx.Button(self, label='Add Study-Guide')
        add_btn.Bind(wx.EVT_BUTTON, self.on_add)

        self.list_ctrl = wx.ListCtrl(self,
                                     style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.row_obj_dict = {}
        self.list_ctrl.InsertColumn(0, 'Course', width=270)
        self.list_ctrl.InsertColumn(1, 'Topic(s)', width=470)

        my_sizer.Add(instructions, 0, wx.ALL | wx.LEFT, 5)

        my_sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        my_sizer2.AddSpacer(5)
        my_sizer2.Add(course_label, wx.ALL | wx.ALIGN_LEFT, 5)
        my_sizer2.Add(self.text_ctrl, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        my_sizer2.AddSpacer(110)
        my_sizer2.Add(topic_label, wx.ALL | wx.ALIGN_LEFT, 5)
        my_sizer2.Add(self.text_ctrl2, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        my_sizer.Add(my_sizer2, 1)

        my_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        my_sizer.Add(add_btn, 0, wx.ALL | wx.LEFT, 5)
        my_sizer.Add(submit_btn, 0, wx.ALL | wx.LEFT, 5)
        self.SetSizer(my_sizer)

    def on_add(self, event):
        course = self.text_ctrl.GetValue()
        topic = self.text_ctrl2.GetValue()
        if not course:
            print("You didn't enter anything!")
        else:
            print("Adding...")
            self.list_ctrl.InsertItem(0, course)
            self.list_ctrl.InsertItem(1, topic)


    def on_submit(self, event):
        index = 0
        while index < self.list_ctrl.GetItemCount():
            print("Communicating with OpenAI...")
            OpenAISetup.submit(self.list_ctrl.GetItemText(index, 0) + ', ' + self.list_ctrl.GetItemText(index, 1))
            index += 1
