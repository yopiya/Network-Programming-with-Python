import tkinter as tk
from tkinter import ttk
from page1 import Page1
from page2 import Page2

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Automation Manager")

        # สร้าง NoteBook (แท็บ)
        self.notebook = ttk.Notebook(root)

        # สร้างหน้า 1
        self.page1 = ttk.Frame(self.notebook)
        self.notebook.add(self.page1, text="Switch")
        self.create_page_content(self.page1, Page1)

        # สร้างหน้า 2
        self.page2 = ttk.Frame(self.notebook)
        self.notebook.add(self.page2, text="Router")
        self.create_page_content(self.page2, Page2)

        # แสดง NoteBook ที่สร้าง
        self.notebook.pack(expand=True, fill="both")

    def create_page_content(self, page, PageClass):
        # สร้างหน้าจอตามคลาสที่กำหนด
        page_content = PageClass(page)
        page_content.pack(expand=True, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x900")
    app = MyApp(root)
    root.mainloop()
