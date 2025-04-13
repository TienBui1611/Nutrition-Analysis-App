import wx
import matplotlib.pyplot as plt
from template_main_frame import MainFrame
from template_main_dialog import MainDialog
from all_functions import file_load, update_grid, top10_nutrition_density, get_nutrition_data, pieBreakdown, barBreakdown
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

class MyMainDialog(MainDialog):


    def __init__(self, *args, **kw):
        # Initialize the dialog
        super(MyMainDialog, self).__init__(*args, **kw)
        self.m_panel_dialog_pie_tab.Bind(wx.EVT_SIZE, self.OnResize)

        self.pie_figure = None
        self.pie_canvas = None
        self.bar_figure = None
        self.bar_canvas = None

    def OnResize(self, event):
        if self.pie_figure is not None:
            panel_width, panel_height = self.m_panel_dialog_pie_tab.GetSize()
            dpi = self.pie_figure.get_dpi()
            new_fig_width = panel_width / dpi
            new_fig_height = panel_height / dpi
            self.pie_figure.set_size_inches(new_fig_width, new_fig_height)
            self.pie_canvas.draw()

        if self.bar_figure is not None:
            panel_width, panel_height = self.m_panel_dialog_bar_tab.GetSize()
            dpi = self.bar_figure.get_dpi()
            new_fig_width = panel_width / dpi
            new_fig_height = panel_height / dpi
            self.bar_figure.set_size_inches(new_fig_width, new_fig_height)
            self.bar_canvas.draw()

        event.Skip()

class MyMainFrame(MainFrame):

    def __init__(self, parent, *args, **kw):
        super(MyMainFrame, self).__init__(parent, *args, **kw)

        self.df = file_load('Food_Nutrition_Dataset.csv')
        self.dialogs = []
        self.selected_row_index = None
        self.pie_wedge_names = ['Fat', 'Saturated Fats', 'Monounsaturated Fats', 'Polyunsaturated Fats', 'Carbohydrates', 'Sugars', 'Protein', 'Dietary Fiber', 'Cholesterol', 'Sodium', 'Water']
        self.pie_wedge_colors = ['blue', 'green', 'red', 'yellow', 'purple', 'orange', 'pink', 'gray', 'brown', 'cyan', 'magenta']
        self.bar_names = ['Vitamin A','Vitamin B1','Vitamin B11','Vitamin B12','Vitamin B2','Vitamin B3','Vitamin B5','Vitamin B6','Vitamin C','Vitamin D','Vitamin E','Vitamin K','Calcium','Copper','Iron','Magnesium','Manganese','Phosphorus','Potassium','Selenium','Zinc']
        self.bar_colors = ['blue', 'green', 'red', 'yellow', 'purple', 'orange', 'pink', 'gray', 'brown', 'cyan', 'magenta', 'blue', 'green', 'red', 'yellow', 'purple', 'orange', 'pink', 'gray', 'brown', 'cyan']
        self.search_df = self.df
        update_grid(self.m_grid_top10_display, top10_nutrition_density(self.df))
        update_grid(self.m_grid_search_display, self.search_df)
        # Select the first row by default and create a manual GridEvent
        if self.m_grid_top10_display.GetNumberRows() > 0:
            self.m_grid_top10_display.SelectRow(0)  # Select the first row
            self.OnGridSelectTop10(manual_override=0)  # Pass the first row index directly

    def Breakdown(self, event):
        idx = int(self.selected_row_index)
        selected_row = self.df[self.df['row_number'] == idx]

        pie_wedge_values = selected_row[self.pie_wedge_names].iloc[0].tolist()
        bar_values = selected_row[self.bar_names].iloc[0].tolist()

        # Create figures
        pie_fig = pieBreakdown(pie_wedge_values, self.pie_wedge_names, self.pie_wedge_colors)
        bar_fig = barBreakdown(bar_values, self.bar_names, self.bar_colors)

        # Open dialog with a pie chart
        current_dialog = MyMainDialog(None)
        self.dialogs.append(current_dialog)
        # set info panel
        current_dialog.m_Text_graph_info_name.SetLabel(str(selected_row['food'].iloc[0]))
        current_dialog.m_Text_graph_info_cal.SetLabel(str(selected_row['Caloric Value'].iloc[0]))
        current_dialog.m_Text_graph_info_density.SetLabel(str(selected_row['Nutrition Density'].iloc[0]))

        # Create canvas for the charts and add it to the dialog panel
        pie_canvas = FigureCanvas(current_dialog.m_panel_dialog_pie_tab, -1, pie_fig)
        bar_canvas = FigureCanvas(current_dialog.m_panel_dialog_bar_tab, -1, bar_fig)

        # Get or create the sizer for the panel
        pie_graph_sizer = current_dialog.m_panel_dialog_pie_tab.GetSizer()
        if pie_graph_sizer is None:
            pie_graph_sizer = wx.BoxSizer(wx.VERTICAL)
            current_dialog.m_panel_dialog_pie_tab.SetSizer(pie_graph_sizer)

        bar_graph_sizer = current_dialog.m_panel_dialog_bar_tab.GetSizer()
        if bar_graph_sizer is None:
            bar_graph_sizer = wx.BoxSizer(wx.VERTICAL)
            current_dialog.m_panel_dialog_bar_tab.SetSizer(bar_graph_sizer)

        # Clear previous contents from the sizer
        pie_graph_sizer.Clear(True)
        bar_graph_sizer.Clear(True)

        # Add the canvases to the sizer
        pie_graph_sizer.Add(pie_canvas, 1, wx.EXPAND)
        bar_graph_sizer.Add(bar_canvas, 1, wx.EXPAND)

        # Save the figure and canvas for future resizing
        current_dialog.pie_figure = pie_fig
        current_dialog.pie_canvas = pie_canvas
        current_dialog.bar_figure = bar_fig
        current_dialog.bar_canvas = bar_canvas

        # Update the panel layout to apply changes
        current_dialog.m_panel_dialog_pie_tab.Layout()
        current_dialog.m_panel_dialog_bar_tab.Layout()

        # Show the dialog as non-modal
        current_dialog.Show()  # Non-modal dialog

    def Search(self, event):
        search_name = self.m_textCtrl_search_name.GetValue().strip()
        search_nutrition = self.m_comboBox_search_nutrition.GetValue().strip()
        search_min = self.m_textCtrl_search_min.GetValue().strip()
        search_max = self.m_textCtrl_search_max.GetValue().strip()
        search_level = self.m_comboBox_search_level.GetValue().strip()

        print(f"search_name: {search_name}, search_min: {search_min}, search_max = {search_max}, search_nutrition = {search_nutrition}, search_level = {search_level}  ")

        filtered_df = self.search_df
        if search_name:
            filtered_df = filtered_df[filtered_df['food'].str.contains(search_name, case=False, na=False)]

        if search_nutrition:
            if search_min:
                try:
                    min_value = float(search_min)
                    filtered_df = filtered_df[filtered_df[search_nutrition] >= min_value]
                except ValueError:
                    wx.MessageBox("Invalid minimum value. Please enter a valid number.", "Error", wx.OK | wx.ICON_ERROR)
            if search_max:
                try:
                    max_value = float(search_max)
                    filtered_df = filtered_df[filtered_df[search_nutrition] <= max_value]
                except ValueError:
                    wx.MessageBox("Invalid maximum value. Please enter a valid number.", "Error", wx.OK | wx.ICON_ERROR)

            max_value = filtered_df[search_nutrition].max() if not filtered_df.empty else 0
            print(f"max_value: {max_value}")

            if search_level == 'Low':
                filtered_df = filtered_df[filtered_df[search_nutrition] < (0.33 * max_value)]
            elif search_level == 'Mid':
                filtered_df = filtered_df[(filtered_df[search_nutrition] >= (0.33 * max_value)) &
                                         (filtered_df[search_nutrition] <= (0.66 * max_value))]
            elif search_level == 'High':
                filtered_df = filtered_df[filtered_df[search_nutrition] > (0.66 * max_value)]

        update_grid(self.m_grid_search_display, filtered_df)

        self.m_staticText_num_rows.SetLabel('The number of rows:  ' + str(len(filtered_df)))

        event.Skip()
    def OnGridSelectTop10(self, event=None, manual_override=None):
        self.OnGridSelect(event, manual_override, self.m_grid_top10_display)

    def OnGridSelectSearch(self, event=None, manual_override=None):
        self.OnGridSelect(event, manual_override, self.m_grid_search_display)

    @staticmethod
    def highlight_row(row_idx, grid):
        """Highlight the selected row in wxGrid."""
        for col_idx in range(grid.GetNumberCols()):
            grid.SetCellBackgroundColour(row_idx, col_idx, wx.Colour(200, 200, 255))  # Highlight color
        grid.ForceRefresh()
    def OnGridSelect(self, event=None, manual_override=None, grid=None):
        """Handle grid cell selection and highlight the row."""
        if event is not None:
            selected_row = event.GetRow()
        elif manual_override is not None:
            selected_row = manual_override
        else:
            return  # No valid row selected, exit the method

        # Reset the background color for all rows to default
        for row_idx in range(grid.GetNumberRows()):
            for col_idx in range(grid.GetNumberCols()):
                grid.SetCellBackgroundColour(row_idx, col_idx, wx.WHITE)

        self.highlight_row(selected_row, grid)  # Highlight the selected row

        last_col_index = grid.GetNumberCols() - 1  # Get the last column index
        self.selected_row_index = grid.GetCellValue(selected_row, last_col_index).strip()  # Get the value of the last cell

        print(f"Selected row: {self.selected_row_index}")
        if event is not None:
            event.Skip()
    def OnClose(self, event):
        print(f"Closing")
        for dialog in self.dialogs:
            dialog.Destroy()
        self.Destroy()  # Close the frame and exit the application
        event.Skip()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyMainFrame(None)
    frame.Show(True)
    app.MainLoop()
