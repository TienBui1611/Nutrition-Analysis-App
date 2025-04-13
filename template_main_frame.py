# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Nutrition App"), pos = wx.DefaultPosition, size = wx.Size( 696,420 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer_main_frame = wx.BoxSizer( wx.VERTICAL )

        self.m_main_frame_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_tab_panel_main_frame_top10 = wx.Panel( self.m_main_frame_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_top10 = wx.BoxSizer( wx.VERTICAL )

        self.m_grid_top10_display = wx.grid.Grid( self.m_tab_panel_main_frame_top10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid_top10_display.CreateGrid( 5, 5 )
        self.m_grid_top10_display.EnableEditing( True )
        self.m_grid_top10_display.EnableGridLines( True )
        self.m_grid_top10_display.EnableDragGridSize( False )
        self.m_grid_top10_display.SetMargins( 0, 0 )

        # Columns
        self.m_grid_top10_display.EnableDragColMove( False )
        self.m_grid_top10_display.EnableDragColSize( True )
        self.m_grid_top10_display.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid_top10_display.EnableDragRowSize( True )
        self.m_grid_top10_display.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid_top10_display.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer_top10.Add( self.m_grid_top10_display, 0, wx.ALL, 5 )

        self.m_button_top10_breakdown = wx.Button( self.m_tab_panel_main_frame_top10, wx.ID_ANY, _(u"Breakdown"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_top10.Add( self.m_button_top10_breakdown, 0, wx.ALL, 5 )


        self.m_tab_panel_main_frame_top10.SetSizer( bSizer_top10 )
        self.m_tab_panel_main_frame_top10.Layout()
        bSizer_top10.Fit( self.m_tab_panel_main_frame_top10 )
        self.m_main_frame_notebook.AddPage( self.m_tab_panel_main_frame_top10, _(u"Top 10"), False )
        self.m_tab_panel_main_frame_search = wx.Panel( self.m_main_frame_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL, u"Search" )
        bSizer_search = wx.BoxSizer( wx.VERTICAL )

        self.m_panel_search = wx.Panel( self.m_tab_panel_main_frame_search, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer1 = wx.GridSizer( 6, 2, 0, 0 )

        self.m_static_search_name = wx.StaticText( self.m_panel_search, wx.ID_ANY, _(u"Name:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_static_search_name.Wrap( -1 )

        gSizer1.Add( self.m_static_search_name, 0, wx.ALL, 5 )

        self.m_textCtrl_search_name = wx.TextCtrl( self.m_panel_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_textCtrl_search_name, 0, wx.ALL, 5 )

        self.m_static_search_nutrition = wx.StaticText( self.m_panel_search, wx.ID_ANY, _(u"Nutrition:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_static_search_nutrition.Wrap( -1 )

        gSizer1.Add( self.m_static_search_nutrition, 0, wx.ALL, 5 )

        m_comboBox_search_nutritionChoices = [ _(u"Caloric Value"), _(u"Fat"), _(u"Saturated Fats"), _(u"Monounsaturated Fats"), _(u"Polyunsaturated Fats"), _(u"Carbohydrates"), _(u"Sugars"), _(u"Protein"), _(u"Dietary Fiber"), _(u"Cholesterol"), _(u"Sodium"), _(u"Water"), _(u"Vitamin A"), _(u"Vitamin B1"), _(u"Vitamin B11"), _(u"Vitamin B12"), _(u"Vitamin B2"), _(u"Vitamin B3"), _(u"Vitamin B5"), _(u"Vitamin B6"), _(u"Vitamin C"), _(u"Vitamin D"), _(u"Vitamin E"), _(u"Vitamin K"), _(u"Calcium"), _(u"Copper"), _(u"Iron"), _(u"Magnesium"), _(u"Manganese"), _(u"Phosphorus"), _(u"Potassium"), _(u"Selenium"), _(u"Zinc"), _(u"Nutrition Density") ]
        self.m_comboBox_search_nutrition = wx.ComboBox( self.m_panel_search, wx.ID_ANY, _(u"Caloric Value"), wx.DefaultPosition, wx.DefaultSize, m_comboBox_search_nutritionChoices, 0 )
        self.m_comboBox_search_nutrition.SetSelection( 0 )
        gSizer1.Add( self.m_comboBox_search_nutrition, 0, wx.ALL, 5 )

        self.m_static_search_min = wx.StaticText( self.m_panel_search, wx.ID_ANY, _(u"Min:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_static_search_min.Wrap( -1 )

        gSizer1.Add( self.m_static_search_min, 0, wx.ALL, 5 )

        self.m_textCtrl_search_min = wx.TextCtrl( self.m_panel_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_textCtrl_search_min, 0, wx.ALL, 5 )

        self.m_static_search_max = wx.StaticText( self.m_panel_search, wx.ID_ANY, _(u"Max:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_static_search_max.Wrap( -1 )

        gSizer1.Add( self.m_static_search_max, 0, wx.ALL, 5 )

        self.m_textCtrl_search_max = wx.TextCtrl( self.m_panel_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_textCtrl_search_max, 0, wx.ALL, 5 )

        self.m_static_search_level = wx.StaticText( self.m_panel_search, wx.ID_ANY, _(u"Level:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_static_search_level.Wrap( -1 )

        gSizer1.Add( self.m_static_search_level, 0, wx.ALL, 5 )

        m_comboBox_search_levelChoices = [ _(u"All"), _(u"Low"), _(u"Mid"), _(u"High") ]
        self.m_comboBox_search_level = wx.ComboBox( self.m_panel_search, wx.ID_ANY, _(u"All"), wx.DefaultPosition, wx.DefaultSize, m_comboBox_search_levelChoices, 0 )
        self.m_comboBox_search_level.SetSelection( 0 )
        gSizer1.Add( self.m_comboBox_search_level, 0, wx.ALL, 5 )

        self.m_button_search = wx.Button( self.m_panel_search, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button_search, 0, wx.ALL, 5 )


        self.m_panel_search.SetSizer( gSizer1 )
        self.m_panel_search.Layout()
        gSizer1.Fit( self.m_panel_search )
        bSizer_search.Add( self.m_panel_search, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel_display = wx.Panel( self.m_tab_panel_main_frame_search, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_search.Add( self.m_panel_display, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText_num_rows = wx.StaticText( self.m_tab_panel_main_frame_search, wx.ID_ANY, _(u"The number of rows:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_num_rows.Wrap( -1 )

        bSizer_search.Add( self.m_staticText_num_rows, 0, wx.ALL, 5 )

        self.m_grid_search_display = wx.grid.Grid( self.m_tab_panel_main_frame_search, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid_search_display.CreateGrid( 5, 5 )
        self.m_grid_search_display.EnableEditing( True )
        self.m_grid_search_display.EnableGridLines( True )
        self.m_grid_search_display.EnableDragGridSize( False )
        self.m_grid_search_display.SetMargins( 0, 0 )

        # Columns
        self.m_grid_search_display.EnableDragColMove( False )
        self.m_grid_search_display.EnableDragColSize( True )
        self.m_grid_search_display.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid_search_display.EnableDragRowSize( True )
        self.m_grid_search_display.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid_search_display.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer_search.Add( self.m_grid_search_display, 0, wx.ALL, 5 )

        self.m_button_search_breakdown = wx.Button( self.m_tab_panel_main_frame_search, wx.ID_ANY, _(u"Breakdown"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_search.Add( self.m_button_search_breakdown, 0, wx.ALL, 5 )


        self.m_tab_panel_main_frame_search.SetSizer( bSizer_search )
        self.m_tab_panel_main_frame_search.Layout()
        bSizer_search.Fit( self.m_tab_panel_main_frame_search )
        self.m_main_frame_notebook.AddPage( self.m_tab_panel_main_frame_search, _(u"Search"), True )

        bSizer_main_frame.Add( self.m_main_frame_notebook, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer_main_frame )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnClose )
        self.m_grid_top10_display.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.OnGridSelectTop10 )
        self.m_button_top10_breakdown.Bind( wx.EVT_BUTTON, self.Breakdown )
        self.m_button_search.Bind( wx.EVT_BUTTON, self.Search )
        self.m_grid_search_display.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.OnGridSelectSearch )
        self.m_button_search_breakdown.Bind( wx.EVT_BUTTON, self.Breakdown )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnClose( self, event ):
        event.Skip()

    def OnGridSelectTop10( self, event ):
        event.Skip()

    def Breakdown( self, event ):
        event.Skip()

    def Search( self, event ):
        event.Skip()

    def OnGridSelectSearch( self, event ):
        event.Skip()



