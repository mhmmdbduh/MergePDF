import os
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog, messagebox
import emoji

def clear_widget(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Function to open the file dialog and get the selected file paths
def open_files():

    # Create the tkinter root object
    root = tk.Tk()

    # Hide the root window
    root.withdraw()

    # Try to get the selected file paths
    try:

        # Use the filedialog method to get the selected files
        file_path = list(filedialog.askopenfilenames(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]))
                
    except Exception as e:

        # If an error occurred, print the error message
        print("Error",f"An error occurred: {e}")
        return None

    # Return the selected file paths
    return file_path

# Function to merge the selected pdf files
def merge_pdf():

    # Get the selected pdf file paths
    pdf_files = open_files()    
    root = tk.Tk()
    root.withdraw()

    # Create a new PdfMerger object
    merger = PdfMerger()
    
    # Check if no files selected
    if not pdf_files:
        messagebox.showerror("Error", "No files selected!")
        return None
    

    else :
        # Ask for output file
        output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    
    try:
        for pdf in pdf_files:
            # Append each pdf files to the merger object
            merger.append(pdf)

    # Write the merged pdf to a file
        merger.write(output + ".pdf")
    # close the merger object
        merger.close()
    
        messagebox.showinfo("info", "PDFs Merged successfuly!")
        
    except Exception as e:
        # If an error occurred, print the error message
         messagebox.showinfo("Error",f"An error occurred: {e}")
         return None
    


def merge_button_clicked():
    # Call the merge_pdf() function to start the merge process
    merge_pdf()
def on_closing():
    root.destroy()
palet = ["#96CBEE","#BADBDE","#FFAD0A","#032425"]
font = "Times New Roman"
root = tk.Tk()
#root.state('zoomed')
root.title("Merge PDFs")
root.resizable(False,False)
root.eval("tk::PlaceWindow . center")
def load_frame1():
    clear_widget(frame2)
    frame1.tkraise()
    
    #frame1.pack_propagate(False)
    # Create a label with instructions on how to use the application
    greeting = tk.Label(frame1,    
                            text="""Welcome! This app where you can choose any pdf files you wish to merge.""", 
                            font=(font, 12),
                            bg=palet[2], width=60,
                            padx=20, pady=20,
                            foreground=palet[3])
    greeting.pack(padx=20, pady=20)
    merge_button = tk.Button(frame1, 
                            text="Select PDFs",
                            bg=palet[3],
                            height=1, 
                            width=60,
                            font=(font, 12),
                            foreground=palet[2],
                            relief="solid",
                            padx=5, pady=10,
                            bd=0,
                            command=merge_button_clicked)
    merge_button.pack(padx=0, pady=10) 
    instruction_button = tk.Button(frame1, 
                            text="How to Use?",
                            bg=palet[3],
                            height=1, 
                            width=60,
                            font=(font, 12), foreground=palet[2],
                            relief="solid",bd=0,
                            padx=5, pady=10,
                            command=load_frame2).pack(padx=0,pady=10)
    signature = tk.Label(frame1, 
                            text=emoji.emojize('Made with :black_heart: by Abduh', variant="emoji_type"), 
                            font=(font, 12),
                            padx=150, pady=10,
                            bg=palet[0], 
                            foreground=palet[3])
    signature.pack(padx=0, pady=20)

def load_frame2():
    frame2.pack_propagate(False)
    clear_widget(frame1)
    frame2.tkraise()
    label = tk.Label(frame2,    
                            text="""To use the application:

1. Click the 'Select PDFs' button.
2. Choose the files that you want to merge.
3. Select the destination folder where you want to save the merged files.
4. Wait until the message "Files merged successfully!" is displayed.""", 
                            font=(font, 12),
                            bg=palet[2],width=60, 
                            padx=20, pady=20,
                            foreground=palet[3])
    label.pack(padx=20, pady=20)

    back_button = tk.Button(frame2, 
                            text="Back",
                            bg=palet[3],
                            height=1, 
                            width=100,
                            font=(font, 12), 
                            foreground=palet[2],
                            relief="solid",
                            bd=0,
                            padx=5, pady=10,
                            command=load_frame1)
    back_button.pack(padx=20, pady=0, )
    signature = tk.Label(frame2, 
                            text=emoji.emojize('Made with :black_heart: by Abduh', variant="emoji_type"), 
                            font=(font, 12),
                            padx=150, pady=12,
                            bg=palet[0], 
                            foreground=palet[3])
    signature.pack(padx=0, pady=20, )


 # Create frame widget   
frame1 = tk.Frame(root,width=600,height=250,  bg=palet[0])#.pack(fill="both", expand = True)
frame2 = tk.Frame(root,  bg=palet[0])#.pack(fill="both", expand = True)

for frame in (frame1, frame2):
    
    frame.grid(row=0, column=0, sticky="nesw" )
    #frame.pack(pady=10,fill="both",expand = True)
load_frame1()
#run app
root.mainloop()
