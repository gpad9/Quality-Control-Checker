#Quality Control GUI
import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import filedialog
import os


class Quality_Control_GUI: #Tkinter GUI
    def __init__(self, root): 
        self.root = root
        self.root.title("Quality Control GUI")
        self.root.geometry("300x250")
        
        self.label = tk.Label(root, text="Excel Sheet")
        self.label.pack()

        self.button = tk.Button(root, text="Get Excel Data", command=self.read_excel)
        self.button.pack()

        self.label1 = tk.Label(root, text="Directory Files")
        self.label1.pack()

        self.button1 = tk.Button(root, text="Get Directory Data", command=self.get_file_names)
        self.button1.pack()

        self.label2 = tk.Label(root, text="Cross-Reference")
        self.label2.pack()

        self.button2 = tk.Button(root, text="Compare", command=self.compare)
        self.button2.pack()

        self.label3 = tk.Label(root, text="")
        self.label3.pack()

        self.excel_df = None
        self.directory_df = None
    
    def read_excel(self): # Reads the excel file and retrieves data
        excel_file = filedialog.askopenfilename()
        sheet_name = "Sheet1"
        data = pd.read_excel(excel_file, sheet_name)
        df = pd.DataFrame(data, columns=['Data'])
        self.excel_df = df
        self.label.config(text="Got Excel df") 
        self.button.destroy()
    
    def get_file_names(self): #Uses os to get the names of the files and puts them into a dataframe
        directory_path = filedialog.askdirectory()
        files = os.listdir(directory_path)
        df_files = pd.DataFrame(files, columns=['File_Names'])
        self.directory_df = df_files
        self.label1.config(text="Got Directory df")
        self.button1.destroy()
    
    def compare(self): #Compares what is in the directory with the data from excel file
        excel_data = [self.excel_df.iloc[i, 0] for i in range(len(self.excel_df))] #Creates a table of values
        directory_data = [self.directory_df.iloc[i, 0][:-4] for i in range(len(self.directory_df))]
        for i in directory_data:
            if i in excel_data:
                excel_data.remove(i) #if the file is found in directory, it removes the element from the data extracted from the excel
            else:
                pass
        s = "Missing:\n"
        for i in excel_data: #concatenates the elements that are missing from the directory into a string
            s = s + i + "\n"
        self.label2.config(text="Cross-Referenced")
        self.button2.destroy()
        self.label3.config(text=s)

def main():
    root = tk.Tk()
    Quality_Control_GUI(root)
    root.mainloop()

if __name__ == "__main__": #Makes sure this is the main script
    main()
    
