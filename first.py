# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:19:17 2022

@author: Monashree
"""
import wx
class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
    def InitUI(self):
        self.panel = wx.Panel(self)
        #self.panel.SetBackgroundColour("gray")
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&Categories')
        Kurti = fileMenu.Append(wx.ID_ANY, 'Kurti')
        
        
        
        Tees = fileMenu.Append(wx.ID_ANY, 'Tees')
        Skirts = fileMenu.Append(wx.ID_ANY, 'Skirts')
        Ethnic = fileMenu.Append(wx.ID_ANY, 'Ethnic wear')
        Saree = fileMenu.Append(wx.ID_ANY, 'Saree')
        Sweaters = fileMenu.Append(wx.ID_ANY, 'Sweaters')
        Shrugs = fileMenu.Append(wx.ID_ANY, 'Shrugs and Coats')
        self.Bind(wx.EVT_MENU, self.OnKurti, Kurti)
        
        
        
        self.Bind(wx.EVT_MENU, self.OnTees, Tees)
        self.Bind(wx.EVT_MENU, self.OnSkirts, Skirts)
        self.Bind(wx.EVT_MENU, self.OnEthnic, Ethnic)
        self.Bind(wx.EVT_MENU, self.OnSaree, Saree)
        self.Bind(wx.EVT_MENU, self.OnSweaters, Sweaters)
        self.Bind(wx.EVT_MENU, self.OnShrugs, Shrugs)
        self.SetMenuBar(menubar)
        self.LoadImages()
        self.bg.SetPosition((40,0))
        self.Maximize(True)
    
    def LoadImages(self):
        self.bg = wx.StaticBitmap(self.panel, wx.ID_ANY,wx.Bitmap("pic2.jpg", wx.BITMAP_TYPE_ANY))
    def OnKurti(self,e):
        Kurti = windowKurti(None, title='Women\'s Kurti')
        Kurti.Show()
    def OnTees(self,e):
        Tees = windowTees(None, title='Women\'s Tees')
        Tees.Show()
    def OnSkirts(self,e):
        Skirts = windowSkirts(None, title='Women\'s Skirts')
        Skirts.Show()
    def OnEthnic(self,e):
        Ethnic = windowEthnic(None, title='Women\'s Ethnic Wear')
        Ethnic.Show()
    def OnSaree(self,e):
        Saree = windowSaree(None, title='Women\'s Saree')
        Saree.Show()
    def OnSweaters(self,e):
        Sweaters = windowSweaters(None, title='Women\'s Sweaters')
        Sweaters.Show()
    def OnShrugs(self,e):
        Shrugs = windowShrugs(None, title='Women\'s Shrugs and Coats')
        Shrugs.Show()

class windowKurti(wx.Frame):
    def __init__(self, parent, title):
        super(windowKurti, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
        self.Maximize(True)
    def InitUI(self):
        #pixel 250 333
        self.panel = wx.ScrolledWindow(self,wx.ID_ANY)
        self.panel.SetScrollbars(1, 1, 1, 1)
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&Categories')
        Kurti = fileMenu.Append(wx.ID_ANY, 'Kurti')
        
        
        
        Tees = fileMenu.Append(wx.ID_ANY, 'Tees')
        Skirts = fileMenu.Append(wx.ID_ANY, 'Skirts')
        Ethnic = fileMenu.Append(wx.ID_ANY, 'Ethnic wear')
        Saree = fileMenu.Append(wx.ID_ANY, 'Saree')
        Sweaters = fileMenu.Append(wx.ID_ANY, 'Sweaters')
        Shrugs = fileMenu.Append(wx.ID_ANY, 'Shrugs and Coats')
        self.Bind(wx.EVT_MENU, self.OnKurti, Kurti)
        
        
        self.Bind(wx.EVT_MENU, self.OnTees, Tees)
        self.Bind(wx.EVT_MENU, self.OnSkirts, Skirts)
        self.Bind(wx.EVT_MENU, self.OnEthnic, Ethnic)
        self.Bind(wx.EVT_MENU, self.OnSaree, Saree)
        self.Bind(wx.EVT_MENU, self.OnSweaters, Sweaters)
        self.Bind(wx.EVT_MENU, self.OnShrugs, Shrugs)
        self.SetMenuBar(menubar)
        toolbar = self.CreateToolBar()
        toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('back.png'))
        toolbar.Realize()
        file1 = open('kurthi.txt', 'r')
        sizer = wx.GridSizer(3,4,40,0)
        filenames = []
        text = ''
        count = 0
        for i in range(1,7):
            filenames.append("k"+str(i)+".jpg")
        for fn in filenames:
            img = wx.Image(fn,wx.BITMAP_TYPE_ANY)
            sizer.Add(wx.StaticBitmap(self.panel,wx.ID_ANY,wx.BitmapFromImage(img)))
            for line in file1:
                count += 1
                text += line
                if count == 10:
                    count = 0
                    break
            sizer.Add(wx.StaticText(self.panel,label = text))
            text = ''
        self.panel.SetSizer(sizer)
        file1.close()
    def OnKurti(self,e):
        Kurti = windowKurti(None, title='Women\'s Kurti')
        Kurti.Show()
        self.Close()
    def OnTees(self,e):
        Tees = windowTees(None, title='Women\'s Tees')
        Tees.Show()
        self.Close()
    def OnSkirts(self,e):
        Skirts = windowSkirts(None, title='Women\'s Skirts')
        Skirts.Show()
        self.Close()
    def OnEthnic(self,e):
        Ethnic = windowEthnic(None, title='Women\'s Ethnic Wear')
        Ethnic.Show()
        self.Close()
    def OnSaree(self,e):
        Saree = windowSaree(None, title='Women\'s Saree')
        Saree.Show()
        self.Close()
    def OnSweaters(self,e):
        Sweaters = windowSweaters(None, title='Women\'s Sweaters')
        Sweaters.Show()
        self.Close()
    def OnShrugs(self,e):
        Shrugs = windowShrugs(None, title='Women\'s Shrugs and Coats')
        Shrugs.Show()
        self.Close()
class windowTees(wx.Frame):
    def __init__(self, parent, title):
        super(windowTees, self).__init__(parent, title=title)
        self.InitUI()
        self.Maximize(True)
        self.Centre()
    def InitUI(self):
        self.panel = wx.ScrolledWindow(self,wx.ID_ANY)
        self.panel.SetScrollbars(1, 1, 1, 1)
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&Categories')
        Kurti = fileMenu.Append(wx.ID_ANY, 'Kurti')
        
        
        
        Tees = fileMenu.Append(wx.ID_ANY, 'Tees')
        Skirts = fileMenu.Append(wx.ID_ANY, 'Skirts')
        Ethnic = fileMenu.Append(wx.ID_ANY, 'Ethnic wear')
        Saree = fileMenu.Append(wx.ID_ANY, 'Saree')
        Sweaters = fileMenu.Append(wx.ID_ANY, 'Sweaters')
        Shrugs = fileMenu.Append(wx.ID_ANY, 'Shrugs and Coats')
        self.Bind(wx.EVT_MENU, self.OnKurti, Kurti)
        
        
        
        self.Bind(wx.EVT_MENU, self.OnTees, Tees)
        self.Bind(wx.EVT_MENU, self.OnSkirts, Skirts)
        self.Bind(wx.EVT_MENU, self.OnEthnic, Ethnic)
        self.Bind(wx.EVT_MENU, self.OnSaree, Saree)
        self.Bind(wx.EVT_MENU, self.OnSweaters, Sweaters)
        self.Bind(wx.EVT_MENU, self.OnShrugs, Shrugs)
        self.SetMenuBar(menubar)
        toolbar = self.CreateToolBar()
        toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('back.png'))
        toolbar.Realize()
        file1 = open('tees.txt', 'r')
        sizer = wx.GridSizer(3,4,40,0)
        filenames = []
        text = ''
        count = 0
        for i in range(1,7):
            filenames.append("t"+str(i)+".jpg")
        for fn in filenames:
            img = wx.Image(fn,wx.BITMAP_TYPE_ANY)
            sizer.Add(wx.StaticBitmap(self.panel,wx.ID_ANY,wx.BitmapFromImage(img)))
            for line in file1:
                count += 1
                text += line
                if count == 10:
                    count = 0
                    break
            sizer.Add(wx.StaticText(self.panel,label = text))
            text = ''
        self.panel.SetSizer(sizer)
        file1.close()
    def OnKurti(self,e):
        Kurti = windowKurti(None, title='Women\'s Kurti')
        Kurti.Show()
        self.Close()
    def OnTees(self,e):
        Tees = windowTees(None, title='Women\'s Tees')
        Tees.Show()
        self.Close()
    def OnSkirts(self,e):
        Skirts = windowSkirts(None, title='Women\'s Skirts')
        Skirts.Show()
        self.Close()
    def OnEthnic(self,e):
        Ethnic = windowEthnic(None, title='Women\'s Ethnic Wear')
        Ethnic.Show()
        self.Close()
    def OnSaree(self,e):
        Saree = windowSaree(None, title='Women\'s Saree')
        Saree.Show()
        self.Close()
    def OnSweaters(self,e):
        Sweaters = windowSweaters(None, title='Women\'s Sweaters')
        Sweaters.Show()
        self.Close()
    def OnShrugs(self,e):
        Shrugs = windowShrugs(None, title='Women\'s Shrugs and Coats')
        Shrugs.Show()
        self.Close()
class windowSkirts(wx.Frame):
    def __init__(self, parent, title):
        super(windowSkirts, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
        self.Maximize(True)
    def InitUI(self):
        self.panel = wx.ScrolledWindow(self,wx.ID_ANY)
        self.panel.SetScrollbars(1, 1, 1, 1)
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&Categories')
        Kurti = fileMenu.Append(wx.ID_ANY, 'Kurti')
        
        
        
        Tees = fileMenu.Append(wx.ID_ANY, 'Tees')
        Skirts = fileMenu.Append(wx.ID_ANY, 'Skirts')
        Ethnic = fileMenu.Append(wx.ID_ANY, 'Ethnic wear')
        Saree = fileMenu.Append(wx.ID_ANY, 'Saree')
        Sweaters = fileMenu.Append(wx.ID_ANY, 'Sweaters')
        Shrugs = fileMenu.Append(wx.ID_ANY, 'Shrugs and Coats')
        self.Bind(wx.EVT_MENU, self.OnKurti, Kurti)
        
        
        
        self.Bind(wx.EVT_MENU, self.OnTees, Tees)
        self.Bind(wx.EVT_MENU, self.OnSkirts, Skirts)
        self.Bind(wx.EVT_MENU, self.OnEthnic, Ethnic)
        self.Bind(wx.EVT_MENU, self.OnSaree, Saree)
        self.Bind(wx.EVT_MENU, self.OnSweaters, Sweaters)
        self.Bind(wx.EVT_MENU, self.OnShrugs, Shrugs)
        self.SetMenuBar(menubar)
        toolbar = self.CreateToolBar()
        toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('back.png'))
        toolbar.Realize()
        file1 = open('sk.txt', 'r')
        sizer = wx.GridSizer(3,4,40,0)
        filenames = []
        text = ''
        count = 0
        for i in range(1,7):
            filenames.append("sk"+str(i)+".jpg")
        for fn in filenames:
            img = wx.Image(fn,wx.BITMAP_TYPE_ANY)
            sizer.Add(wx.StaticBitmap(self.panel,wx.ID_ANY,wx.BitmapFromImage(img)))
            for line in file1:
                count += 1
                text += line
                if count == 10:
                    count = 0
                    break
            sizer.Add(wx.StaticText(self.panel,label = text))
            text = ''
        self.panel.SetSizer(sizer)
        file1.close()
    def OnKurti(self,e):
        Kurti = windowKurti(None, title='Women\'s Kurti')
        Kurti.Show()
        self.Close()
    def OnTees(self,e):
        Tees = windowTees(None, title='Women\'s Tees')
        Tees.Show()
        self.Close()
    def OnSkirts(self,e):
        Skirts = windowSkirts(None, title='Women\'s Skirts')
        Skirts.Show()
        self.Close()
    def OnEthnic(self,e):
        Ethnic = windowEthnic(None, title='Women\'s Ethnic Wear')
        Ethnic.Show()
        self.Close()
    def OnSaree(self,e):
        Saree = windowSaree(None, title='Women\'s Saree')
        Saree.Show()
        self.Close()
    def OnSweaters(self,e):
        Sweaters = windowSweaters(None, title='Women\'s Sweaters')
        Sweaters.Show()
        self.Close()
    def OnShrugs(self,e):
        Shrugs = windowShrugs(None, title='Women\'s Shrugs and Coats')
        Shrugs.Show()
        self.Close()
class windowEthnic(wx.Frame):
    def __init__(self, parent, title):
        super(windowEthnic, self).__init__(parent, title=title)
        self.InitUI()
        self.Maximize(True)
        self.Centre()
    def InitUI(self):
        self.panel = wx.ScrolledWindow(self,wx.ID_ANY)
        self.panel.SetScrollbars(1, 1, 1, 1)
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&Categories')
        Kurti = fileMenu.Append(wx.ID_ANY, 'Kurti')
        
        
        
        Tees = fileMenu.Append(wx.ID_ANY, 'Tees')
        Skirts = fileMenu.Append(wx.ID_ANY, 'Skirts')
        Ethnic = fileMenu.Append(wx.ID_ANY, 'Ethnic wear')
        Saree = fileMenu.Append(wx.ID_ANY, 'Saree')
        Sweaters = fileMenu.Append(wx.ID_ANY, 'Sweaters')
        Shrugs = fileMenu.Append(wx.ID_ANY, 'Shrugs and Coats')
        self.Bind(wx.EVT_MENU, self.OnKurti, Kurti)
        
        
        
        self.Bind(wx.EVT_MENU, self.OnTees, Tees)
        self.Bind(wx.EVT_MENU, self.OnSkirts, Skirts)
        self.Bind(wx.EVT_MENU, self.OnEthnic, Ethnic)
        self.Bind(wx.EVT_MENU, self.OnSaree, Saree)
        self.Bind(wx.EVT_MENU, self.OnSweaters, Sweaters)
        self.Bind(wx.EVT_MENU, self.OnShrugs, Shrugs)
        self.SetMenuBar(menubar)
        toolbar = self.CreateToolBar()
        toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('back.png'))
        toolbar.Realize()
        file1 = open('ew.txt', 'r')
        sizer = wx.GridSizer(3,4,40,0)
        filenames = []
        text = ''
        count = 0
        for i in range(1,7):
            filenames.append("ew"+str(i)+".jpg")
        for fn in filenames:
            img = wx.Image(fn,wx.BITMAP_TYPE_ANY)
            sizer.Add(wx.StaticBitmap(self.panel,wx.ID_ANY,wx.BitmapFromImage(img)))
            for line in file1:
                count += 1
                text += line
                if count == 10:
                    count = 0
                    break
            sizer.Add(wx.StaticText(self.panel,label = text))
            text = ''
        self.panel.SetSizer(sizer)
        file1.close()
    def OnKurti(self,e):
        Kurti = windowKurti(None, title='Women\'s Kurti')
        Kurti.Show()
        self.Close()
    def OnTees(self,e):
        Tees = windowTees(None, title='Women\'s Tees')
        Tees.Show()
        self.Close()
    def OnSkirts(self,e):
        Skirts = windowSkirts(None, title='Women\'s Skirts')
        Skirts.Show()
        self.Close()
    def OnEthnic(self,e):
        Ethnic = windowEthnic(None, title='Women\'s Ethnic Wear')
        Ethnic.Show()
        self.Close()
    def OnSaree(self,e):
        Saree = windowSaree(None, title='Women\'s Saree')
        Saree.Show()
        self.Close()
    def OnSweaters(self,e):
        Sweaters = windowSweaters(None, title='Women\'s Sweaters')
        Sweaters.Show()
        self.Close()
    def OnShrugs(self,e):
        Shrugs = windowShrugs(None, title='Women\'s Shrugs and Coats')
        Shrugs.Show()
        self.Close()
class windowSaree(wx.Frame):
    def __init__(self, parent, title):
        super(windowSaree, self).__init__(parent, title=title)
        self.InitUI()
        self.Maximize(True)
        self.Centre()
    def InitUI(self):
        self.panel = wx.ScrolledWindow(self,wx.ID_ANY)
        self.panel.SetScrollbars(1, 1, 1, 1)
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&Categories')
        Kurti = fileMenu.Append(wx.ID_ANY, 'Kurti')
        
        
        
        Tees = fileMenu.Append(wx.ID_ANY, 'Tees')
        Skirts = fileMenu.Append(wx.ID_ANY, 'Skirts')
        Ethnic = fileMenu.Append(wx.ID_ANY, 'Ethnic wear')
        Saree = fileMenu.Append(wx.ID_ANY, 'Saree')
        Sweaters = fileMenu.Append(wx.ID_ANY, 'Sweaters')
        Shrugs = fileMenu.Append(wx.ID_ANY, 'Shrugs and Coats')
        self.Bind(wx.EVT_MENU, self.OnKurti, Kurti)
        
        
        
        self.Bind(wx.EVT_MENU, self.OnTees, Tees)
        self.Bind(wx.EVT_MENU, self.OnSkirts, Skirts)
        self.Bind(wx.EVT_MENU, self.OnEthnic, Ethnic)
        self.Bind(wx.EVT_MENU, self.OnSaree, Saree)
        self.Bind(wx.EVT_MENU, self.OnSweaters, Sweaters)
        self.Bind(wx.EVT_MENU, self.OnShrugs, Shrugs)
        self.SetMenuBar(menubar)
        toolbar = self.CreateToolBar()
        toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('back.png'))
        toolbar.Realize()
        file1 = open('saree.txt', 'r')
        sizer = wx.GridSizer(3,4,40,0)
        filenames = []
        text = ''
        count = 0
        for i in range(1,7):
            filenames.append("sa"+str(i)+".jpg")
        for fn in filenames:
            img = wx.Image(fn,wx.BITMAP_TYPE_ANY)
            sizer.Add(wx.StaticBitmap(self.panel,wx.ID_ANY,wx.BitmapFromImage(img)))
            for line in file1:
                count += 1
                text += line
                if count == 10:
                    count = 0
                    break
            sizer.Add(wx.StaticText(self.panel,label = text))
            text = ''
        self.panel.SetSizer(sizer)
        file1.close()
    def OnKurti(self,e):
        Kurti = windowKurti(None, title='Women\'s Kurti')
        Kurti.Show()
        self.Close()
    def OnTees(self,e):
        Tees = windowTees(None, title='Women\'s Tees')
        Tees.Show()
        self.Close()
    def OnSkirts(self,e):
        Skirts = windowSkirts(None, title='Women\'s Skirts')
        Skirts.Show()
        self.Close()
    def OnEthnic(self,e):
        Ethnic = windowEthnic(None, title='Women\'s Ethnic Wear')
        Ethnic.Show()
        self.Close()
    def OnSaree(self,e):
        Saree = windowSaree(None, title='Women\'s Saree')
        Saree.Show()
        self.Close()
    def OnSweaters(self,e):
        Sweaters = windowSweaters(None, title='Women\'s Sweaters')
        Sweaters.Show()
        self.Close()
    def OnShrugs(self,e):
        Shrugs = windowShrugs(None, title='Women\'s Shrugs and Coats')
        Shrugs.Show()
        self.Close()
class windowSweaters(wx.Frame):
    def __init__(self, parent, title):
        super(windowSweaters, self).__init__(parent, title=title)
        self.InitUI()
        self.Maximize(True)
        self.Centre()
    def InitUI(self):
        self.panel = wx.ScrolledWindow(self,wx.ID_ANY)
        self.panel.SetScrollbars(1, 1, 1, 1)
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&Categories')
        Kurti = fileMenu.Append(wx.ID_ANY, 'Kurti')
        
        
        
        Tees = fileMenu.Append(wx.ID_ANY, 'Tees')
        Skirts = fileMenu.Append(wx.ID_ANY, 'Skirts')
        Ethnic = fileMenu.Append(wx.ID_ANY, 'Ethnic wear')
        Saree = fileMenu.Append(wx.ID_ANY, 'Saree')
        Sweaters = fileMenu.Append(wx.ID_ANY, 'Sweaters')
        Shrugs = fileMenu.Append(wx.ID_ANY, 'Shrugs and Coats')
        self.Bind(wx.EVT_MENU, self.OnKurti, Kurti)
        
        
        
        self.Bind(wx.EVT_MENU, self.OnTees, Tees)
        self.Bind(wx.EVT_MENU, self.OnSkirts, Skirts)
        self.Bind(wx.EVT_MENU, self.OnEthnic, Ethnic)
        self.Bind(wx.EVT_MENU, self.OnSaree, Saree)
        self.Bind(wx.EVT_MENU, self.OnSweaters, Sweaters)
        self.Bind(wx.EVT_MENU, self.OnShrugs, Shrugs)
        self.SetMenuBar(menubar)
        toolbar = self.CreateToolBar()
        toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('back.png'))
        toolbar.Realize()
        file1 = open('sweaters.txt', 'r')
        sizer = wx.GridSizer(3,4,40,0)
        filenames = []
        text = ''
        count = 0
        for i in range(1,7):
            filenames.append("sw"+str(i)+".jpg")
        for fn in filenames:
            img = wx.Image(fn,wx.BITMAP_TYPE_ANY)
            sizer.Add(wx.StaticBitmap(self.panel,wx.ID_ANY,wx.BitmapFromImage(img)))
            for line in file1:
                count += 1
                text += line
                if count == 10:
                    count = 0
                    break
            sizer.Add(wx.StaticText(self.panel,label = text))
            text = ''
        self.panel.SetSizer(sizer)
        file1.close()
    def OnKurti(self,e):
        Kurti = windowKurti(None, title='Women\'s Kurti')
        Kurti.Show()
        self.Close()
    def OnTees(self,e):
        Tees = windowTees(None, title='Women\'s Tees')
        Tees.Show()
        self.Close()
    def OnSkirts(self,e):
        Skirts = windowSkirts(None, title='Women\'s Skirts')
        Skirts.Show()
        self.Close()
    def OnEthnic(self,e):
        Ethnic = windowEthnic(None, title='Women\'s Ethnic Wear')
        Ethnic.Show()
        self.Close()
    def OnSaree(self,e):
        Saree = windowSaree(None, title='Women\'s Saree')
        Saree.Show()
        self.Close()
    def OnSweaters(self,e):
        Sweaters = windowSweaters(None, title='Women\'s Sweaters')
        Sweaters.Show()
        self.Close()
    def OnShrugs(self,e):
        Shrugs = windowShrugs(None, title='Women\'s Shrugs and Coats')
        Shrugs.Show()
        self.Close()
class windowShrugs(wx.Frame):
    def __init__(self, parent, title):
        super(windowShrugs, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
        self.Maximize(True)
    def InitUI(self):
        self.panel = wx.ScrolledWindow(self,wx.ID_ANY)
        self.panel.SetScrollbars(1, 1, 1, 1)
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&Categories')
        Kurti = fileMenu.Append(wx.ID_ANY, 'Kurti')
        
        
        
        Tees = fileMenu.Append(wx.ID_ANY, 'Tees')
        Skirts = fileMenu.Append(wx.ID_ANY, 'Skirts')
        Ethnic = fileMenu.Append(wx.ID_ANY, 'Ethnic wear')
        Saree = fileMenu.Append(wx.ID_ANY, 'Saree')
        Sweaters = fileMenu.Append(wx.ID_ANY, 'Sweaters')
        Shrugs = fileMenu.Append(wx.ID_ANY, 'Shrugs and Coats')
        self.Bind(wx.EVT_MENU, self.OnKurti, Kurti)
        
        
        
        self.Bind(wx.EVT_MENU, self.OnTees, Tees)
        self.Bind(wx.EVT_MENU, self.OnSkirts, Skirts)
        self.Bind(wx.EVT_MENU, self.OnEthnic, Ethnic)
        self.Bind(wx.EVT_MENU, self.OnSaree, Saree)
        self.Bind(wx.EVT_MENU, self.OnSweaters, Sweaters)
        self.Bind(wx.EVT_MENU, self.OnShrugs, Shrugs)
        self.SetMenuBar(menubar)
        toolbar = self.CreateToolBar()
        toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('back.png'))
        toolbar.Realize()
        file1 = open('shrugs.txt', 'r')
        sizer = wx.GridSizer(3,4,40,0)
        filenames = []
        text = ''
        count = 0
        for i in range(1,7):
            filenames.append("s"+str(i)+".jpg")
        for fn in filenames:
            img = wx.Image(fn,wx.BITMAP_TYPE_ANY)
            sizer.Add(wx.StaticBitmap(self.panel,wx.ID_ANY,wx.BitmapFromImage(img)))
            for line in file1:
                count += 1
                text += line
                if count == 10:
                    count = 0
                    break
            sizer.Add(wx.StaticText(self.panel,label = text))
            text = ''
        self.panel.SetSizer(sizer)
        file1.close()
    def OnKurti(self,e):
        Kurti = windowKurti(None, title='Women\'s Kurti')
        Kurti.Show()
        self.Close()
    def OnTees(self,e):
        Tees = windowTees(None, title='Women\'s Tees')
        Tees.Show()
        self.Close()
    def OnSkirts(self,e):
        Skirts = windowSkirts(None, title='Women\'s Skirts')
        Skirts.Show()
        self.Close()
    def OnEthnic(self,e):
        Ethnic = windowEthnic(None, title='Women\'s Ethnic Wear')
        Ethnic.Show()
        self.Close()
    def OnSaree(self,e):
        Saree = windowSaree(None, title='Women\'s Saree')
        Saree.Show()
        self.Close()
    def OnSweaters(self,e):
        Sweaters = windowSweaters(None, title='Women\'s Sweaters')
        Sweaters.Show()
        self.Close()
    def OnShrugs(self,e):
        Shrugs = windowShrugs(None, title='Women\'s Shrugs and Coats')
        Shrugs.Show()
        self.Close()
def main():
    app = wx.App()
    ex = Example(None, title='Women Shopping Portal')
    ex.Show()
    app.MainLoop()
if __name__ == '__main__':
    main()
