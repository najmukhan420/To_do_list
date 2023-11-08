from tkinter import *
# Imports all modules from tkinter GUI


def main():
    
    # This is the file which the program reads/writes into, other one is where deleted lines go
    to_do_file = "ToDo.txt"
    deleted_text_file = "del_" + to_do_file


    def read():
        """ Each time this code is run, the output_one text box will be updated with the most recent text inside the 
        to_do_file.txt file"""
        
        output_one.delete(1.0, END)
        outstring = ""
        line_count = 0
        with open(to_do_file) as file_read:
            for i in file_read.readlines():
                line_count += 1
                outstring += format(line_count, "2d") + ". " + i
            output_one.insert(END, outstring)
        
    def run_append():
        """ Takes text from input_one text box and appends it into the to_do_file.txt """
        with open(to_do_file, "a") as file_append:
            input_string = input_one.get() + "\n"
            file_append.write(input_string)
        reset()

    def run_remove():
        """
        Removes selected line in the output_two text box and inserts it into the deleted_text_file
        """
        delete_line = eval(input_two.get()) - 1
        outstring = ""

        with open(to_do_file, "r") as file_delete:
            text_lines = file_delete.readlines()
            add_deleted_line = text_lines.pop(delete_line)

        with open(deleted_text_file, "a") as deleted:
            deleted.write(add_deleted_line + "\n")

        with open(to_do_file, "w") as file_append:
            for i in text_lines:
                outstring += i
            file_append.write(outstring)

        reset()

    def reset():
        """ Deletes all text in text boxes and re-reads the target text file"""
        output_one.delete(1.0, END)
        input_one.delete(0, END)
        input_two.delete(0, END)
        read()

    # Initialize tkinter interface
    root = Tk()
    root.title("~~ To Do List ~~")
    top_gui = Frame(root)
    top_gui.grid(row=1)
    bottom_gui = Frame(root)
    bottom_gui.grid(row=2)

    # Top GUI
    Label(top_gui, text="Enter text to be added:", width=34).grid(row=1, column=1)
    runner = Button(top_gui, text="Add", width=34, command=lambda: run_append())
    runner.grid(row=1, column=2)

    input_one = Entry(top_gui, width=80)
    input_one.grid(row=2, column=1, columnspan=2)

    Label(top_gui, text="Enter line to be removed:", width=34).grid(row=3, column=1)
    Button(top_gui, text="Remove", command=lambda: run_remove(), width=34).grid(row=3, column=2)

    input_two = Entry(top_gui, width=38)
    input_two.grid(row=4, column=1)

    Button(top_gui, text="Reset", command=lambda: reset(), width=34).grid(row=4, column=2)

    # Bottom GUI
    output_one = Text(bottom_gui, width=60, background="light gray")
    output_one.grid(row=2, column=1)
    Button(bottom_gui, width=68, text="QUIT", command=root.destroy, fg="red").grid(row=3, column=1)

    # Reads file after loading widgets to display your text
    read()

    root.mainloop()


if __name__ == '__main__':
    main()