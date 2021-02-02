# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Audio Clock", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnStart = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnStart, 0, wx.ALL, 5 )
		
		self.btnPlay = wx.Button( self, wx.ID_ANY, u"Play Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnPlay, 0, wx.ALL, 5 )
		
		self.btnRandom = wx.Button( self, wx.ID_ANY, u"Play Random", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnRandom, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		lbScheduleChoices = []
		self.lbSchedule = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbScheduleChoices, 0 )
		bSizer2.Add( self.lbSchedule, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		lbFilesChoices = []
		self.lbFiles = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbFilesChoices, 0 )
		bSizer3.Add( self.lbFiles, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnStart.Bind( wx.EVT_BUTTON, self.ClickStart )
		self.btnPlay.Bind( wx.EVT_BUTTON, self.ClickPlay )
		self.btnRandom.Bind( wx.EVT_BUTTON, self.ClickRandom )
		self.lbFiles.Bind( wx.EVT_LISTBOX_DCLICK, self.DClickFile )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ClickStart( self, event ):
		event.Skip()
	
	def ClickPlay( self, event ):
		event.Skip()
	
	def ClickRandom( self, event ):
		event.Skip()
	
	def DClickFile( self, event ):
		event.Skip()
	

