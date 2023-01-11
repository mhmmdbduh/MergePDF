import os
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog, messagebox


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
palet = ["#BBDEF0","#235789","#F58F29"]
root = tk.Tk()
#root.geometry("600x250")
root.title("Merge PDFs")
root.eval("tk::PlaceWindow . center")
frame1 = tk.Frame(root, width=600, height=250, bg=palet[0])
frame1.grid(row=0, column=0)

# Create a label with instructions on how to use the application
label = tk.Label(frame1, 
                 text="""Welcome! This app where you can choose any pdf files you wish to merge.

To use the application:
1. Click the 'Select PDFs' button.
2. Choose the files that you want to merge.
3. Select the destination folder where you want to save the merged files.
4. Wait until the message "Files merged successfully!" is displayed.""", 
                 font=('Fira Code', 10),
                 bg=palet[1], 
                 padx=20, pady=20,
                 foreground='white')
label.pack(padx=20, pady=20)
merge_button = tk.Button(frame1, 
                         text="Select PDFs",
                         bg=palet[2],
                         height=1, 
                         width=60,
                         font=('montserrat', 12), 
                         relief="solid",
                         padx=5, pady=10,
                         command=merge_button_clicked)
merge_button.pack(padx=20, pady=10)
label = tk.Label(frame1, 
                    text="""made by <3 by Abduh """, 
                    font=('Fira Code', 12),
                    padx=150, pady=10,
                    bg=palet[0], 
                    foreground=palet[1])
label.pack(padx=0, pady=20)
root.mainloop()
