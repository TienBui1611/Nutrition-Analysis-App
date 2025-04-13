import matplotlib.pyplot as plt

def file_load(filepath):
    import pandas as pd  # Import here to avoid circular import
    try:
        df = pd.read_csv(filepath)
        df['row_number'] = df.index  # add primary key
        return df
    except Exception as e:
        raise Exception(f"Error loading file: {e}")

def update_grid(grid, data_frame):
    import wx.grid  # Import here to avoid circular import
    grid.ClearGrid()
    if grid.GetNumberRows() > 0:
        grid.DeleteRows(0, grid.GetNumberRows())
    if grid.GetNumberCols() > 0:
        grid.DeleteCols(0, grid.GetNumberCols())
    grid.AppendCols(len(data_frame.columns))
    for col, header in enumerate(data_frame.columns):
        grid.SetColLabelValue(col, header)
    grid.AppendRows(len(data_frame))
    for row in range(len(data_frame)):
        for col in range(len(data_frame.columns)):
            grid.SetCellValue(row, col, str(data_frame.iat[row, col]))
def top10_nutrition_density(data_frame):
    return data_frame.sort_values(by='Nutrition Density', ascending=False).head(10)
def get_nutrition_data(data_frame, cols):
    return data_frame[cols]
def pieBreakdown(sizes, foods, colors):

    fig, ax = plt.subplots(figsize =(8, 5))
    wedges, texts, autotexts = ax.pie(sizes, labels=None, colors=colors, autopct='%1.1f%%', startangle=90)

    # Create a legend with the labels
    ax.legend(wedges, labels=foods, title="Nutrition Breakdown", loc="lower left", bbox_to_anchor=(0.85, 0), fontsize=10)

    # Optional: Set aspect ratio to be equal, ensuring the pie is drawn as a circle.
    ax.axis('equal')

    fig.subplots_adjust(right=0.75)  # Adjust the right side of the subplot area

    return fig
def barBreakdown(sizes, foods, colors):

    fig, ax = plt.subplots(figsize =(7, 4))
    ax.bar(foods, sizes, color=colors)
    for i in range(len(sizes)):
        ax.text(i, sizes[i], sizes[i], ha='center')
    ax.set_ylabel("mg", fontsize=10)
    plt.xticks(rotation=90)
    fig.tight_layout()
    return fig
