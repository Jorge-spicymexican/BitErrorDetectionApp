import tkinter as tk


read_info = """Welcome to my App for CE4951 Lab 7 analyzer.
Coded in python!\nThis page is for instructions on the application!
    Supplies needed:
        * Computer,
        * Zip File with App exe 
    Procedure:
            (1) Turn on your computer and download the 
            latest python code on computer.\n
            (2) Locate the Zip file on your computer,
            or download the App code on github. \n
            (3) Download the exe. and under the ribbon 
            cable,read more about Single and Burst 
            Error detection rates.\n
            (4) Type in your desired 2 ASCII value and 
            decide what to compare it to.\n
            (5) Select a location for dumping the 
            Data-logging feature of the app,
            This will allow to debug the exe and give 
            you a text file result page.\n
            (6) Run the app and enjoy!\n
        """

author_info = """
Jorge Jurado-Garcia is a student in Milwaukee School 
of Engineering (MSOE).\n
Where he is pursing a degree in Electrical Engineering.
Jorge grew up in Beloit Wisconsin with 10 Siblings, 8 
Brothers and 2 Sisters with a pet dog.As the oldest, 
Jorge hopes to lead by example that high education is 
important by continuing his education after College. 
He hopes to get a Masters from Marquette or UW-Madison 
in signal processing. During his Free time Jorge likes 
to learn statistical analysis and writing code in C and C#.

"""

filter_info = """
A Error Burst is defined as a group of bits in which two 
successive erroneous bits are always separated by less than
a given number x of correct bits. The last erroneous bit in 
the burst and the first erroneous bit in the following burst
are accordingly speared by a correct bits or more. 

Example is shown below:

Let X = 3, and suppose that receiver receives 
0101 0100 1010 0010
But the expect value was ASCII letters AB:
0100 0001 0100 0010

The first bit error in index 4 can be a single-bit error 
or the start of a burst. If an error occurs before 3 
correct bits the burst continues. In this case, an
error is located at:
Index: 4,6,8,9,10,11
Due to this the length of our Burst will be 8 BITs long. 
Or End_of_Burst - Inital_Burst + 1

In this application an inital burst error will be found. 
A test reporting of the length of the burst error 
will also be given as long as its indices.

"""

def text_window(str,info):
    win = tk.Toplevel()

    window_width = 500
    window_height = 350

    # get screen dimension
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # create the screen on window console
    win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    win.title(str)
    win.resizable(False, False)
    win.iconbitmap('./Imports/msoe.ico')
    win.attributes('-topmost', 1)

    # create a text widget and specifiy size
    T = tk.Text(win, height=18, width=70)

    # create a label
    l = tk.Label(win, text=str)
    l.config(font=("Courier", 16))

    # create an exit button
    b_exit = tk.Button(win, text="Exit", command=win.destroy)

    # create a Scrollbar and associate it with txt
    scrollb = tk.Scrollbar(win, command=T.yview)
    l.pack(side=tk.TOP)
    scrollb.pack(side=tk.RIGHT)
    T.pack()
    T.insert(tk.END, info)
    b_exit.pack()