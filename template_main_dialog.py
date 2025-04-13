# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainDialog
###########################################################################

class MainDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Nutrition Breakdown"), pos = wx.DefaultPosition, size = wx.Size( 1043,721 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer_main_dialog = wx.BoxSizer( wx.VERTICAL )

        self.m_panel_dialog_graph_info = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel_dialog_graph_info.SetMaxSize( wx.Size( -1,80 ) )

        bSizer_graph_info = wx.BoxSizer( wx.VERTICAL )

        self.m_Text_graph_info_name = wx.StaticText( self.m_panel_dialog_graph_info, wx.ID_ANY, _(u"avo"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Text_graph_info_name.Wrap( -1 )

        self.m_Text_graph_info_name.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer_graph_info.Add( self.m_Text_graph_info_name, 0, wx.ALL, 5 )

        gSizer9 = wx.GridSizer( 1, 5, 0, 0 )

        self.m_staticText_graph_info_cal = wx.StaticText( self.m_panel_dialog_graph_info, wx.ID_ANY, _(u"Caloric Value (kcal):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_graph_info_cal.Wrap( -1 )

        gSizer9.Add( self.m_staticText_graph_info_cal, 0, wx.ALL, 5 )

        self.m_Text_graph_info_cal = wx.StaticText( self.m_panel_dialog_graph_info, wx.ID_ANY, _(u"50kcal"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Text_graph_info_cal.Wrap( -1 )

        gSizer9.Add( self.m_Text_graph_info_cal, 0, wx.ALL, 5 )

        self.m_staticText_graph_info_density = wx.StaticText( self.m_panel_dialog_graph_info, wx.ID_ANY, _(u"Nutrition Density:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_graph_info_density.Wrap( -1 )

        gSizer9.Add( self.m_staticText_graph_info_density, 0, wx.ALL, 5 )

        self.m_Text_graph_info_density = wx.StaticText( self.m_panel_dialog_graph_info, wx.ID_ANY, _(u"200g"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Text_graph_info_density.Wrap( -1 )

        gSizer9.Add( self.m_Text_graph_info_density, 0, wx.ALL, 5 )


        bSizer_graph_info.Add( gSizer9, 1, wx.EXPAND, 5 )


        self.m_panel_dialog_graph_info.SetSizer( bSizer_graph_info )
        self.m_panel_dialog_graph_info.Layout()
        bSizer_graph_info.Fit( self.m_panel_dialog_graph_info )
        bSizer_main_dialog.Add( self.m_panel_dialog_graph_info, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_dialog_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel_dialog_pie_tab = wx.Panel( self.m_dialog_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_graph_pie = wx.BoxSizer( wx.VERTICAL )


        self.m_panel_dialog_pie_tab.SetSizer( bSizer_graph_pie )
        self.m_panel_dialog_pie_tab.Layout()
        bSizer_graph_pie.Fit( self.m_panel_dialog_pie_tab )
        self.m_dialog_notebook.AddPage( self.m_panel_dialog_pie_tab, _(u"Nutrition Chart"), True )
        self.m_panel_dialog_bar_tab = wx.Panel( self.m_dialog_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_graph_bar = wx.BoxSizer( wx.VERTICAL )


        self.m_panel_dialog_bar_tab.SetSizer( bSizer_graph_bar )
        self.m_panel_dialog_bar_tab.Layout()
        bSizer_graph_bar.Fit( self.m_panel_dialog_bar_tab )
        self.m_dialog_notebook.AddPage( self.m_panel_dialog_bar_tab, _(u"Vitamins and Minerals"), False )

        bSizer_main_dialog.Add( self.m_dialog_notebook, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer_main_dialog )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SIZE, self.OnResize )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnResize( self, event ):
        event.Skip()


