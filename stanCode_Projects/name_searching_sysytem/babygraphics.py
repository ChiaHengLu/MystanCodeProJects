"""
File: babygraphics.py
Name: Chia-heng Lu
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    gap = (width - 2 * GRAPH_MARGIN_SIZE)/(len(YEARS))
    x_coordinate = GRAPH_MARGIN_SIZE + gap * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    for year_index in range(len(YEARS)):
        year_index_x = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(year_index_x, 0, year_index_x, CANVAS_HEIGHT)
        canvas.create_text(year_index_x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[year_index], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    y_long = CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE
    y_long_gap = y_long / 1000
    color_index = -1
    for lookup_name in lookup_names:
        if lookup_name in name_data:
            color_index += 1
            if color_index > len(COLORS)-1:
                color_index %= len(COLORS)
            for i in range(len(YEARS)-1):
                name_year_x_1 = get_x_coordinate(CANVAS_WIDTH, i)
                if str(YEARS[i]) in name_data[lookup_name]:
                    year_1 = str(YEARS[i])
                    name_year_y_1 = int(name_data[lookup_name][year_1]) * y_long_gap
                    name_year = lookup_name + ' ' + name_data[lookup_name][year_1]
                else:
                    year_1 = '*'
                    name_year_y_1 = CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE
                    name_year = lookup_name + ' ' + year_1
                name_year_x_2 = get_x_coordinate(CANVAS_WIDTH, i+1)
                if str(YEARS[i+1]) in name_data[lookup_name]:
                    year_2 = str(YEARS[i+1])
                    name_year_y_2 = int(name_data[lookup_name][year_2]) * y_long_gap
                else:
                    name_year_y_2 = CANVAS_HEIGHT -  2* GRAPH_MARGIN_SIZE
                canvas.create_line(name_year_x_1, name_year_y_1 + GRAPH_MARGIN_SIZE, name_year_x_2, name_year_y_2 + GRAPH_MARGIN_SIZE, width=LINE_WIDTH,
                                   fill=COLORS[color_index])
                canvas.create_text(name_year_x_1 + TEXT_DX, name_year_y_1 + GRAPH_MARGIN_SIZE, text=name_year,
                                   anchor=tkinter.SW, fill=COLORS[color_index])
            name_year_x_end = get_x_coordinate(CANVAS_WIDTH, len(YEARS)-1)
            if str(YEARS[len(YEARS)-1]) in name_data[lookup_name]:
                year_end = str(YEARS[len(YEARS)-1])
                name_year_y_end = int(name_data[lookup_name][year_end]) * y_long_gap
                name_year_end = lookup_name + ' ' + name_data[lookup_name][year_end]
            else:
                year_end = '*'
                name_year_y_end = CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE
                name_year_end = lookup_name + ' ' + year_end
            canvas.create_text(name_year_x_end + TEXT_DX, name_year_y_end + GRAPH_MARGIN_SIZE, text=name_year_end,anchor=tkinter.SW,
                               fill=COLORS[color_index])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
