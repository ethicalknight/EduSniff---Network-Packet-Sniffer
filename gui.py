import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from sniffer import capture_packets
from utils import parse_packet
import threading

class PacketSnifferGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("EduSniff - Packet Sniffer")
        self.root.geometry("800x500")

        self.output = ScrolledText(self.root, font=("Consolas", 10))
        self.output.pack(fill=tk.BOTH, expand=True)

        self.start_button = tk.Button(self.root, text="Start Sniffing", command=self.start_sniffing)
        self.start_button.pack(pady=10)

    def display_packet(self, packet):
        parsed = parse_packet(packet)
        self.output.insert(tk.END, parsed + "\n")
        self.output.see(tk.END)

    def start_sniffing(self):
        self.output.insert(tk.END, "Starting packet capture...\n")
        thread = threading.Thread(target=capture_packets, args=(self.display_packet,))
        thread.daemon = True
        thread.start()

    def run(self):
        self.root.mainloop()
