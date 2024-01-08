import tkinter as tk
from tkinter import ttk
import threading
from netmiko import ConnectHandler
import schedule
import time

class TimePicker(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()

        # Label for Start Time
        self.label = tk.Label(self, text="Start time", font=("Helvetica", 12))
        self.label.pack(side=tk.LEFT, padx=5, pady=5)

        # Create Combobox for hours
        self.hour_combo = ttk.Combobox(self, values=[str(i).zfill(2) for i in range(24)], textvariable=self.hour_var)
        self.hour_combo.set("00")
        self.hour_combo.pack(side=tk.LEFT, padx=5, pady=5)

        # Create Combobox for minutes
        self.minute_combo = ttk.Combobox(self, values=[str(i).zfill(2) for i in range(60)], textvariable=self.minute_var)
        self.minute_combo.set("00")
        self.minute_combo.pack(side=tk.LEFT, padx=5, pady=5)

    def get_time(self):
        return f"{self.hour_var.get()}:{self.minute_var.get()}"

class Page2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Setting automation on router", font=("Helvetica", 18))
        label.pack(padx=10, pady=10)

        # ----------------------------------------------------------------

        # Create a frame to hold TimePicker
        time_frame = tk.Frame(self)
        time_frame.pack(padx=10, pady=5, anchor=tk.W)

        # Replace Entry widgets with TimePicker
        self.time_picker = TimePicker(time_frame)
        self.time_picker.pack(side=tk.LEFT)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # ----------------------------------------------------------------
                # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=10, anchor=tk.W)

        #-----------------------------------------------------------------

        label_inputipdevicerouter = tk.Label(new_line_frame, text="Input IP Device", font=("Helvetica", 10))
        label_inputipdevicerouter.pack(side=tk.LEFT, padx=15, pady=0)

        input_host_ipaddr = tk.Text(new_line_frame, width=20, height=1)
        input_host_ipaddr.pack(side=tk.LEFT, padx=10, pady=0)

        #-----------------------------------------------------------------

        # Radio buttons for command selection
        self.command_var = tk.StringVar()
        self.command_var.set("show_running")  # Default selection
        show_running_radio = tk.Radiobutton(new_line_frame, text="Show Running", variable=self.command_var, value="show_running")
        show_running_radio.pack(side=tk.LEFT, padx=10)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # ----------------------------------------------------------------

        ping_radio = tk.Radiobutton(new_line_frame, text="Ping", variable=self.command_var, value="ping")
        ping_radio.pack(side=tk.LEFT, padx=10)

        # Entry widget for IP address (for ping command)
        self.ip_entry = tk.Entry(new_line_frame)
        self.ip_entry.pack(side=tk.LEFT, padx=10)
        self.ip_entry.insert(0, "192.168.1.1")  # Default IP address

        # ----------------------------------------------------------------

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # Create a access list function by ip address
        acl_button = tk.Radiobutton(new_line_frame, text="Access Control List - By IP Address", variable=self.command_var,value="acl")
        acl_button.pack(side=tk.LEFT, padx=10, pady=5)

        # ----------------------------------------------------------------

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # Create a new label 
        lb_inputInt = tk.Label(new_line_frame, text="Input Interface you will need", font=("Helvetica", 10))
        lb_inputInt.pack(side=tk.LEFT, padx=25, pady=0)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # Create a label
        label_acl = tk.Label(new_line_frame, text="IP Address to allow:", font=("Helvetica", 10))
        label_acl.pack(side=tk.LEFT, padx=25, pady=0)

        # Input IP Address to allow
        ipp_ipadd = tk.Text(new_line_frame, width=20, height=1)
        ipp_ipadd.pack(side=tk.LEFT, padx=10, pady=0)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # IP Address to deny
        deny_ip = tk.Label(new_line_frame, text="IP Address to deny:", font=("Helvetica", 10))
        deny_ip.pack(side=tk.LEFT, padx=25, pady=0)

        # Input IP Address to deny
        ipp_ipadd = tk.Text(new_line_frame, width=20, height=1)
        ipp_ipadd.pack(side=tk.LEFT, padx=10, pady=0)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        #deny all labels
        deny_all_label_ip = tk.Checkbutton(new_line_frame, text="Deny all")
        deny_all_label_ip.pack(side=tk.LEFT, padx=20, pady=5)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # ----------------------------------------------------------------

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # Create a access list function by Interface
        acl_button = tk.Radiobutton(new_line_frame, text="Access Control List - By Interface", variable=self.command_var,value="aclint")
        acl_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # Create a new label 
        lb_inputInt = tk.Label(new_line_frame, text="Input Interface you will need", font=("Helvetica", 10))
        lb_inputInt.pack(side=tk.LEFT, padx=25, pady=0)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # Create a label
        label_acl = tk.Label(new_line_frame, text="Interface to allow:", font=("Helvetica", 10))
        label_acl.pack(side=tk.LEFT, padx=25, pady=0)

        # Input IP Address to allow
        ipp_ipadd = tk.Text(new_line_frame, width=20, height=1)
        ipp_ipadd.pack(side=tk.LEFT, padx=10, pady=0)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # IP Address to deny
        deny_ip = tk.Label(new_line_frame, text="Interface to deny:", font=("Helvetica", 10))
        deny_ip.pack(side=tk.LEFT, padx=25, pady=0)

        # Input IP Address to deny
        ipp_ipadd = tk.Text(new_line_frame, width=20, height=1)
        ipp_ipadd.pack(side=tk.LEFT, padx=10, pady=0)

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        #deny all labels
        deny_all_label = tk.Checkbutton(new_line_frame, text="Deny all")
        deny_all_label.pack(side=tk.LEFT, padx=20, pady=5)

        # ----------------------------------------------------------------

        # Create a new line
        new_line_frame = tk.Frame(self)
        new_line_frame.pack(pady=5, anchor=tk.W)

        # Create a Submit button
        submit_button = tk.Button(new_line_frame, text="Submit", command=self.submit)
        submit_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Create a Text widget for the output with adjusted width and height
        self.result_text = tk.Text(self, width=120, height=15)
        self.result_text.pack(side=tk.LEFT,padx=10, pady=0)

        # Create command to ssh router
        self.CSR = {
            'device_type': 'cisco_ios',
            'ip': label_inputipdevicerouter,
            'username': 'admin',
            'password': 'dgt'
        }

    def ping_command(self, ip):
        # Establish the SSH connection
        net_connect = ConnectHandler(**self.CSR)

        # Form the ping command with the provided IP address
        ping_cmd = f'ping {ip}'

        output = net_connect.send_command(ping_cmd)
        self.result_text.insert(tk.END, output + "\n\n")  # Insert the output into the Text widget

        # Close the connection
        net_connect.disconnect()

    def show_running_command(self):
        # Establish the SSH connection
        net_connect = ConnectHandler(**self.CSR)

        output = net_connect.send_command('show running')
        self.result_text.insert(tk.END, output + "\n\n")  # Insert the output into the Text widget

        # Close the connection
        net_connect.disconnect()

    def submit(self):
        # Get the selected time from TimePicker
        time_input = self.time_picker.get_time()

        # Schedule the appropriate command to run at the specified time
        if self.command_var.get() == "ping":
            ip_address = self.ip_entry.get()
            schedule.every().day.at(time_input).do(lambda: self.ping_command(ip_address))
        elif self.command_var.get() == "show_running":
            schedule.every().day.at(time_input).do(self.show_running_command)
        

        # Start the scheduler in a separate thread
        thread = threading.Thread(target=self.run_schedule)
        thread.start()

    def run_schedule(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    root.title("Switch Automation")
    Page2(root)
    root.mainloop()
