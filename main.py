## this is the maind document for my pythong script
import GUI

if __name__ == "__main__":
    app = GUI.App()
    # creation of an instance
    GUI.Window(app)
    GUI.MainFrame(app)
    app.mainloop()