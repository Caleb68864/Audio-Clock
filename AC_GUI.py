# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Audio Clock", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Reload", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem5 )

		self.m_menu11 = wx.Menu()
		self.miAddTime = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Add Time", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.miAddTime )

		self.m_menuItem2 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Remove Time", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem2 )

		self.miAddAudio = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Add Audio", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.miAddAudio )

		self.m_menuItem4 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Remove Audio", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem4 )

		self.m_menu1.AppendSubMenu( self.m_menu11, u"Configure" )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnStart = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnStart, 1, wx.ALL, 5 )

		self.btnPlay = wx.Button( self, wx.ID_ANY, u"Play Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnPlay, 1, wx.ALL, 5 )

		self.btnRandom = wx.Button( self, wx.ID_ANY, u"Play Random", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnRandom, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		lbScheduleChoices = []
		self.lbSchedule = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbScheduleChoices, wx.LB_NEEDED_SB )
		bSizer2.Add( self.lbSchedule, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		lbFilesChoices = []
		self.lbFiles = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbFilesChoices, wx.LB_NEEDED_SB|wx.LB_SORT )
		bSizer3.Add( self.lbFiles, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer3, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.selReload, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.selAddTime, id = self.miAddTime.GetId() )
		self.Bind( wx.EVT_MENU, self.selRemoveTime, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.selAddFile, id = self.miAddAudio.GetId() )
		self.Bind( wx.EVT_MENU, self.selRemoveFile, id = self.m_menuItem4.GetId() )
		self.btnStart.Bind( wx.EVT_BUTTON, self.ClickStart )
		self.btnPlay.Bind( wx.EVT_BUTTON, self.ClickPlay )
		self.btnRandom.Bind( wx.EVT_BUTTON, self.ClickRandom )
		self.lbFiles.Bind( wx.EVT_LISTBOX_DCLICK, self.DClickFile )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def selReload( self, event ):
		event.Skip()

	def selAddTime( self, event ):
		event.Skip()

	def selRemoveTime( self, event ):
		event.Skip()

	def selAddFile( self, event ):
		event.Skip()

	def selRemoveFile( self, event ):
		event.Skip()

	def ClickStart( self, event ):
		event.Skip()

	def ClickPlay( self, event ):
		event.Skip()

	def ClickRandom( self, event ):
		event.Skip()

	def DClickFile( self, event ):
		event.Skip()


###########################################################################
## Class scheduleDialog
###########################################################################

class scheduleDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Dialog", pos = wx.DefaultPosition, size = wx.Size( 315,167 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.mdBtnAdd = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.mdBtnAdd, 0, wx.ALL, 5 )

		self.mdBtnCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.mdBtnCancel, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.mdBtnAdd.Bind( wx.EVT_BUTTON, self.mdBtnAdd_Click )
		self.mdBtnCancel.Bind( wx.EVT_BUTTON, self.mdBtnCancel_Click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def mdBtnAdd_Click( self, event ):
		event.Skip()

	def mdBtnCancel_Click( self, event ):
		event.Skip()


