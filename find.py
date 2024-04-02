from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import requests
import datetime
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import tkinter as tk
from tkinter import filedialog

data=[]
class result:
    def __init__(self,reg) -> None:
        self.regno=reg[0]
        self.comb=reg[1]
        print(self.comb)
            
    def find_res(self):
        marks_table=[]
        try:
            driver = webdriver.Chrome()
            driver.get("https://karresults.nic.in/slpufirst.asp")
            driver.maximize_window()
            
            #regno=946632
            driver.find_element(By.ID, 'reg').send_keys(self.regno)
            select = Select(driver.find_element(By.ID, 'ddlsub'))
            if self.comb=="science":
                select.select_by_index(1)
            else :
                select.select_by_index(3)
            driver.find_element(By.XPATH,"//button[@type='submit']").click()
            #newname=f"screenshot_{self.regno}_.png"
            
            name=driver.find_element(By.XPATH, "//span[normalize-space()]")
            reg=driver.find_element(By.XPATH, "//span[normalize-space()]")
            elements = driver.find_elements(By.CLASS_NAME, "textright")
            res1 = driver.find_elements(By.XPATH, "//td[normalize-space()]")
            
            newname=f"screenshot_{self.regno}_{name.text}.png"
            #print(driver.save_screenshot(newname))
            marks_table.append(self.regno)
            marks_table.append(self.comb)
            marks_table.append(name.text)
            
            #marks_table.append(reg.text)
            #for ele in elements:
            #    marks_table.append(ele.text)
            for i in res1:
                marks_table.append(i.text)
        except Exception as e:
            marks_table.append(self.regno)
            marks_table.append(f"An exception happend {e}")    
        #print(marks_table)
        #mk=[]
        #mk.append(self.regno)
        #mk.append(marks_table[0])
        #mk.append(marks_table[6])
        #mk.append(marks_table[9])
        #mk.append(marks_table[15])
        #mk.append(marks_table[18])
        #mk.append(marks_table[21])
        #mk.append(marks_table[24])
        data.append(marks_table)
        df = pd.DataFrame(data)
        rows = dataframe_to_rows(df)
        wb = Workbook()
        ws = wb.active
        for row in rows:
            ws.append(row)
        wb.save('data1.xlsx')
        
        #print(mk)
    
class Feeder:
    def open_file_picker(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()
        df = pd.read_excel(file_path)

      
        data_list = df.values.tolist()
        data = [(x[0], x[1]) for x in data_list]

        root.destroy()

        return data

    def nums(self, data):
        """Return the numbers in the given data as a list of tuples."""
        # Create a list of tuples, each containing the first and second elements of the input tuple
        # and the first element as an integer
        nums = [(x[0], x[1]) for x in data]

        return nums

ob = Feeder()
d = ob.open_file_picker()

d = ob.nums(d)   
#d=[946624, 946632, 946633, 946645, 946649, 946696, 946721, 946751, 946752, 946766, 946768, 946769]
count=0
for i in d:
    obj = result(list(i))
    obj.find_res()
    count+=1
    print(count)

#print(data)