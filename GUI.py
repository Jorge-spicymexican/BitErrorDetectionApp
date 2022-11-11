"""
# Licensed to MSOE
# This file is owned and copyrighted by Jorge Jurado-Garcia
#  Author: Jorge Jesus Jurado-Garcia
#  Title: Electrical Engineering Student
#
#  Date of Creation: 10/18/2022
#  Rev: 1.0
"""

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk, Menu
from tkinter.messagebox import showerror, showinfo
from imports import text_imports


def CalBurst(Value, Compare, burst_index):
    fileinfo = ["=====================================================\n"]

    print("=====================================================")
    Value_array = Value.encode()
    Compare_array = Compare.encode()
    Value_bin_int = bin(int.from_bytes(Value_array, "big"))
    Compare_bin_int = bin(int.from_bytes(Compare_array, "big"))

    print("Burst Threshold: ", burst_index)
    fileinfo.append("Burst Threshold: " + burst_index + "\n")

    print("User ASCII Value: ", Value, "\nBinary Format:\t", Value_bin_int)
    fileinfo.append("User ASCII Value: " + Value + "\nBinary Format:\t" + Value_bin_int + "\n")

    print("Comparing ASCII Value: ", Compare, "\nBinary Format:\t", Compare_bin_int)
    print("\n")
    fileinfo.append("Comparing ASCII Value: " + Compare +
                    "\nBinary Format:\t" + Compare_bin_int + "\n")
    fileinfo.append("\n\n")
    indexCounter = int(burst_index)
    STTOP = False
    FirstErrorFound = False
    FirstErrorFoundConstant = False
    IndexOfFirstError = 0
    IndexofEndBurst = 0

    for i in range(len(Value_bin_int)):
        # print("Counter", indexCounter)
        # print("Index", i)

        # loop around the user binary value and check
        # if it matches to the comparing value
        if Value_bin_int[i] != Compare_bin_int[i]:
            print("Values are different at Index:", i)
            fileinfo.append("Values are different at Index:" + str(i) + "\n")
            FirstErrorFound = True

            if FirstErrorFound and FirstErrorFoundConstant == False:
                FirstErrorFoundConstant = True
                IndexOfFirstError = i

        if FirstErrorFoundConstant and STTOP == False:
            # if the value are equal to each other decrease the counter if they are the same put the counter back
            # at its max value
            if Value_bin_int[i] != Compare_bin_int[i]:
                indexCounter = int(burst_index)
            else:
                indexCounter = indexCounter - 1

            # if the counter reaches 0 this means the first has ben finished
            if indexCounter == 0:
                IndexofEndBurst = i
                STTOP = True

    # print("Index of End Burst", IndexofEndBurst)
    FinalCountdown = 0
    print("\n")
    fileinfo.append("\n")

    if indexCounter > 0:
        IndexofEndBurst = 16
        FinalCountdown = IndexofEndBurst
    else:
        FinalCountdown = IndexofEndBurst - int(burst_index)

    print("Start of Burst:", IndexOfFirstError, "End of Burst:", FinalCountdown)
    print("Final Burst Length", FinalCountdown - IndexOfFirstError + 1)
    print("=====================================================")
    print("\n\n")

    fileinfo.append("Start of Burst:" + str(IndexOfFirstError) + "\nEnd of Burst:" + str(FinalCountdown) + "\n")
    fileinfo.append("Final Burst Length:" + str(FinalCountdown - IndexOfFirstError + 1) + "\n")
    fileinfo.append("=====================================================\n\n")

    return fileinfo


def writeTextFile( data, path):
    file1 = open(path + "\CE4951 Problem-1 DataLog.txt", "w")
    file1.writelines(data)
    file1.close()
    print(path)


class MainFrame(ttk.Frame):

    # Initialization
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        """object main public variables"""
        self.UserSelected_entry = tk.StringVar()
        self.selected_ASCII = tk.StringVar()
        self.selected_BurstAmount = tk.StringVar()
        self.datalog_location_path = str()

        # UserSelected label
        self.UserSelected_label = ttk.Label(self, text="2 Char ASCII :")
        self.UserSelected_label.grid(column=0, row=0, sticky=tk.W, **options)

        # Name entry
        self.UserSelected_entry = ttk.Entry(self, textvariable=self.UserSelected_entry)
        self.UserSelected_entry.grid(column=1, row=0, sticky=tk.EW, **options)
        self.UserSelected_entry.focus()

        # burst label and combo box
        self.BurstLength = ttk.Label(self, text="Burst Length:")
        self.BurstLength.grid(column=0, row=1, sticky=tk.W, **options)

        self.Burst_cb = ttk.Combobox(self, textvariable=self.selected_BurstAmount)
        self.Burst_cb['values'] = ('1', '2', '3', '4', '5')
        self.Burst_cb['state'] = 'readonly'
        self.Burst_cb.grid(column=1, row=1, sticky=tk.NE, **options)
        self.Burst_cb.set('None selected')

        # Compared ASCII label and combo box
        self.CASCII_label = ttk.Label(self, text="Compared ASCII:")
        self.CASCII_label.grid(column=0, row=2, sticky=tk.W, **options)
        self.ASCII_cb = ttk.Combobox(self, textvariable=self.selected_ASCII)
        self.ASCII_cb['values'] = ('AB', 'BC', 'DE', 'ZA', 'HI')
        self.ASCII_cb['state'] = 'readonly'
        self.ASCII_cb.grid(column=1, row=2, sticky=tk.NE, **options)
        self.ASCII_cb.set('None selected')

        # Dump txt file here
        self.button = ttk.Button(self, text="Datalog Location", command=self.new_log_location)
        self.button.grid(row=3, column=0, columnspan=2, sticky=tk.EW, **options)

        # start button
        self.start_button = ttk.Button(self, text='Start', command=self.start)
        self.start_button.grid(column=0, row=4, columnspan=2, sticky=tk.EW, **options)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def new_log_location(self):
        self.datalog_location_path = self.folder_lookup()

    def start(self):
        self.check_entry

    def stop(self):
        self.stop_entry

    @staticmethod
    def folder_lookup():
        directory = fd.askdirectory(
        )
        if directory != "":
            showinfo(
                title='Selected Directory',
                message=directory
            )
        return directory

    @property
    def check_entry(self):
        check = True
        # print( self.UserSelected_entry.get(), self.selected_ASCII.get(), self.selected_BurstAmount.get() )

        value = self.UserSelected_entry.get()
        # print(len(value))
        # check if the user inputted all of the needed values
        if self.UserSelected_entry.get() == '' or (len(value) != 2):
            showerror(
                title='Error-ASCII',
                message='Type in two ASCIIs characters.'
            )
            check = False
            return

        if self.selected_ASCII.get() == 'None selected':
            showerror(
                title='Error-Selection',
                message='Select an ASCII to compare it to.'

            )
            check = False

        if self.selected_BurstAmount.get() == 'None selected':
            showerror(
                title='Error-Burst Amount',
                message='Select a Burst Amount.'
            )
            check = False

        if self.datalog_location_path == "":
            showerror(
                title='Error-Logging Path',
                message='Looks like you forgot to insert a Data-logging Directory.'
            )
            check = False
        """
        Here we are going to write a function that calculates the other brust error 
        """
        if (check == True):
            # print(value, self.selected_ASCII.get(), self.selected_BurstAmount.get())
            data = CalBurst(value, self.selected_ASCII.get(), self.selected_BurstAmount.get())
            writeTextFile(data, self.datalog_location_path )
            showinfo(
                title='Burst Error Outcome',
                message=self.datalog_location_path + "/CE4951 Problem-1 DataLog.txt"
            )

"""
Here, we are creating our class, Window, and inheriting from the Frame
class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
"""


class Window(tk.Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master):
        super().__init__(master)
        # field options

        # reference to the master widget, which is the tk window
        self.save = tk.BooleanVar()
        self.save.set(False)
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Read Me", command=self.read_me_exit)
        file.add_command(label="Exit", command=self.user_exit)

        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object
        about = Menu(menu)

        # added "about the author" to our menu
        about.add_command(label="About Author", command=self.author_about)
        about.add_command(label="About Burst and Single-bit errors ", command=self.problem_about)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        menu.add_cascade(label="About", menu=about)

        # create the file object
        github = Menu(menu)

        # added "about the author" to our menu
        github.add_command(label="GitHub Repository", command=self.Github_link)
        github.add_command(label="Email - Address", command=self.email_link)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        menu.add_cascade(label="GitHub", menu=github)

        # scope = Menu(menu)
        # scope.add_checkbutton(label="Save Waveform", onvalue=1, offvalue=0, variable=self.save)
        # menu.add_cascade(label="Scope", menu=scope)

    @staticmethod
    def read_me_exit():
        text_imports.text_window("Read Me", text_imports.read_info)

    @staticmethod
    def author_about():
        # print("HI")
        text_imports.text_window("About Author", text_imports.author_info)

    @staticmethod
    def problem_about():
        # print("lol")
        text_imports.text_window("About Single and Burst Errors", text_imports.filter_info)

    @staticmethod
    def user_exit():
        exit()

    @staticmethod
    def Github_link():
        showinfo(
            title='GitHub Repository',
            message='https://github.com/Jorge-spicymexican/BitErrorDetectionApp'
        )

    @staticmethod
    def email_link():
        showinfo(
            title='Email',
            message='jorgejuradogarcia2@gmail.com'
        )


"""
This is the main window widget of the GUI, the title and icon is configured here 
title is done to be at CE4951 Lab Week 7 
the Tkinker has been setup as a grid style and the width and height has also been configured.
"""


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('CE4951 Lab Week 7 ')
        self.resizable(False, False)
        # ensure that a window is always at the top of the stacking order
        self.attributes('-topmost', 1)

        """ CONFIGURE THE GRID OF THE GUI"""
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        window_width = 300
        window_height = 200

        # get screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # create the screen on window console
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # changing the Tinker Logo into the MSOE logo instead for our development
        self.iconbitmap('./imports/msoe.ico')
        frm = ttk.Frame(self, padding=1)
        frm.grid()


"""
Main function and runs code settings information 
"""
if __name__ == "__main__":
    print("GUI.PY SHOULD NOT BE RUN, WARNING!!!.\n")
