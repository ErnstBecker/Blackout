# Necessary imports.
import tkinter
from tkinter import Canvas, Button, Entry, Label, PhotoImage
import os


# Creating The "Program" Class.
class Program:
    # Main Function.
    def __init__(self, root):
        # Validate function.
        def testVal(inStr, acttyp):
            if acttyp == '1':  # insert
                if not inStr.isdigit():
                    return False
            return True

        # Function for buttons animations.
        # Function for make him red. (Shutdown)
        def shutdown_anim_on(event):
            self.btn_shutdown.config(image=self.img_shutdown_selec)

        # Function to return to default. (Shutdown)
        def shutdown_anim_off(event):
            self.btn_shutdown.config(image=self.img_shutdown)

        # Function for make him green. (Confirm)
        def confirm_anim_on(event):
            self.btn_confirm.config(image=self.img_confirm_selec)

        # Function to return to default. (Confirm)
        def confirm_anim_off(event):
            self.btn_confirm.config(image=self.img_confirm)

        # Function for make him blue. (Cancel)
        def cancel_anim_on(event):
            self.btn_cancel.config(image=self.img_cancel_selec)

        # Function to return to default. (Cancel)
        def cancel_anim_off(event):
            self.btn_cancel.config(image=self.img_cancel)

        # Function for make him orange. (Reset)
        def reset_anim_on(event):
            self.btn_reset.config(image=self.img_reset_selec)

        # Function to return to default. (Reset)
        def reset_anim_off(event):
            self.btn_reset.config(image=self.img_reset)

        # Program title.
        self.text_title = Label(root,
                                text='Blackout',
                                bg='#191919',
                                fg="#FFFFFF")
        self.text_title.config(font=('Bahnschrift', 20))
        self.text_title.place(x=247, y=33)

        # Text to talk about the timer.
        self.text_tutorial = Label(root,
                                   text='Time for shutdown the computer',
                                   bg='#191919',
                                   fg="#FFFFFF")
        self.text_tutorial.config(font=('Bahnschrift', 20))
        self.text_tutorial.place(x=35, y=200)

        # Text for show the minutes.
        self.text_minutes = Label(root,
                                  text='Minutes',
                                  bg='#191919',
                                  fg="#FFFFFF")
        self.text_minutes.config(font=('Bahnschrift', 20))
        self.text_minutes.place(x=386, y=132)

        # Text box for place the time for shutdown the computer.
        self.box_time = Entry(root,
                              width=7,
                              font=('Bahnschrift', 20, 'bold'),
                              bg='#e2e2e2',
                              fg='#000000',
                              relief='flat',
                              validate='key')
        self.box_time['validatecommand'] = (
            self.box_time.register(testVal), '%P', '%d')
        self.box_time.place(x=248, y=133)

        # Path of the images.
        self.dirname_img = os.path.dirname(os.path.abspath(__file__))

        # Images.
        # Image of shutdown button.
        self.img_shutdown = PhotoImage(
            file=f'{self.dirname_img}/images/shutdown-button.png')

        # Image of shutdown button selected.
        self.img_shutdown_selec = PhotoImage(
            file=f'{self.dirname_img}/images/shutdown-button-selec.png')

        # Image of confirm button.
        self.img_confirm = PhotoImage(
            file=f'{self.dirname_img}/images/confirm-button.png')

        # Image of confirm button selected.
        self.img_confirm_selec = PhotoImage(
            file=f'{self.dirname_img}/images/confirm-button-selec.png')

        # Image of cancel button.
        self.img_cancel = PhotoImage(
            file=f'{self.dirname_img}/images/cancel-button.png')

        # Image of cancel button selected.
        self.img_cancel_selec = PhotoImage(
            file=f'{self.dirname_img}/images/cancel-button-selec.png')

        # Image of reset button.
        self.img_reset = PhotoImage(
            file=f'{self.dirname_img}/images/reset-button.png')

        # Image of reset button selected.
        self.img_reset_selec = PhotoImage(
            file=f'{self.dirname_img}/images/reset-button-selec.png')

        # Showing confirm button again.
        def start():
            # Confirm button animated.
            self.btn_confirm = Button(root,
                                      highlightcolor='#FF0000',
                                      borderwidth=0,
                                      bg='#191919',
                                      activebackground='#191919',
                                      image=self.img_confirm,
                                      relief='flat',
                                      command=lambda: [time_calc(), self.btn_confirm.place_forget()])
            self.btn_confirm.place(x=90.5, y=126)
            self.btn_confirm.bind('<Enter>', confirm_anim_on)
            self.btn_confirm.bind('<Leave>', confirm_anim_off)

        # Cancel button animated.
        self.btn_cancel = Button(root,
                                 highlightcolor='#FF0000',
                                 borderwidth=0,
                                 bg='#191919',
                                 activebackground='#191919',
                                 relief='flat',
                                 image=self.img_cancel,
                                 command=lambda: os.system("shutdown -a"))
        self.btn_cancel.place(x=390.5, y=276)
        self.btn_cancel.bind('<Enter>', cancel_anim_on)
        self.btn_cancel.bind('<Leave>', cancel_anim_off)

        # Starting the function that shows the confirm button.
        start()

        # Function for calculate the time for execute the shutdown function.
        def time_calc():
            # Function that shutdown the computer in the right time.
            def windows_shutdown(time):
                os.system(f"shutdown -s -t {time}")

            self.time_minutes = self.box_time.get()
            self.time_seconds = int(self.time_minutes) * 60

            # Shutdown button animated.
            self.btn_shutdown = Button(root,
                                       highlightcolor='#FF0000',
                                       borderwidth=0,
                                       bg='#191919',
                                       activebackground='#191919',
                                       relief='flat',
                                       image=self.img_shutdown,
                                       command=lambda: windows_shutdown(self.time_seconds))
            self.btn_shutdown.place(x=90.5, y=276)
            self.btn_shutdown.bind('<Enter>', shutdown_anim_on)
            self.btn_shutdown.bind('<Leave>', shutdown_anim_off)

            # Reset button animated.
            self.btn_reset = Button(root,
                                    highlightcolor='#FF0000',
                                    borderwidth=0,
                                    bg='#191919',
                                    activebackground='#191919',
                                    relief='flat',
                                    image=self.img_reset,
                                    command=lambda: [self.box_time.delete(0, 'ins'), start(),
                                                     self.btn_reset.place_forget(),
                                                     self.btn_shutdown.place_forget()])
            self.btn_reset.place(x=90.5, y=126)
            self.btn_reset.bind('<Enter>', reset_anim_on)
            self.btn_reset.bind('<Leave>', reset_anim_off)


# Main function with some settings.
def main():
    # For start Tkinter.
    root = tkinter.Tk()

    # Path of the program icon.
    dirname_ico = os.path.dirname(os.path.abspath(__file__))

    # Program icon.
    root.iconbitmap(f'{dirname_ico}/images/Blackout.ico')

    # Title of the window.
    root.title('Blackout')

    # Make it impossible to change the screen size.
    root.resizable(width=False, height=False)

    # Program window.
    canvas = Canvas(root, width=600,
                    height=400,
                    bg='#191919',
                    relief='flat')
    canvas.pack()

    # For the "Program" class to get the root of tkinter.
    Program(root)

    # Program start.
    root.mainloop()


# Function to run only the main program.
if __name__ == '__main__':
    main()
