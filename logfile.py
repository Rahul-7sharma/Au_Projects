import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

# --- Original Logic Class (Unchanged) ---
class Linecounter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.line = []

    def read(self):
        with open(self.file_name, "r") as f:
            self.line = f.readlines()

    def fetch_ip_add(self):
        self.ip_add = list(map(lambda x: x.split(" ")[0], self.line))
        return self.ip_add

    def ip_add_20(self):
        return list(filter(lambda x: int(x.split(".")[0]) < 20, self.ip_add))

    def ratio(self):
        return len(self.ip_add_20()) / len(self.fetch_ip_add())


# --- GUI with Enhanced UI ---
class LinecounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("🌐 Log IP Analyzer")
        self.master.configure(bg="#e9f5ff")

        self.lc = None
        self.filename = tk.StringVar(value="No file selected")

        # Fonts
        header_font = ("Helvetica", 16, "bold")
        button_font = ("Segoe UI", 10, "bold")
        text_font = ("Consolas", 10)

        # --- Header ---
        tk.Label(master, text="Log File IP Analyzer", font=header_font, bg="#e9f5ff", fg="#003366").pack(pady=(10, 0))
        tk.Label(master, textvariable=self.filename, bg="#e9f5ff", fg="#444444", font=("Segoe UI", 9)).pack(pady=(0, 10))

        # --- Buttons Frame ---
        button_frame = tk.Frame(master, bg="#e9f5ff")
        button_frame.pack(pady=10)

        def styled_btn(text, cmd, color):
            return tk.Button(button_frame, text=text, font=button_font, bg=color, fg="white",
                             activebackground="#333", activeforeground="white", width=20, command=cmd)

        styled_btn("📂 Select Log File", self.load_file, "#4CAF50").grid(row=0, column=0, padx=5, pady=5)
        styled_btn("📄 Show All IPs", self.show_all_ips, "#2196F3").grid(row=0, column=1, padx=5, pady=5)
        styled_btn("🧪 Show IPs < 20", self.show_ips_20, "#FF9800").grid(row=0, column=2, padx=5, pady=5)
        styled_btn("📊 Show Ratio", self.show_ratio, "#9C27B0").grid(row=0, column=3, padx=5, pady=5)

        # --- Output Area ---
        self.output = ScrolledText(master, width=100, height=25, bg="#ffffff", fg="#333333",
                                   font=text_font, borderwidth=2, relief="flat", padx=10, pady=10)
        self.output.pack(padx=15, pady=15)

    # --- Actions ---
    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                self.lc = Linecounter(file_path)
                self.lc.read()
                self.lc.fetch_ip_add()
                self.filename.set(f"✅ Loaded: {file_path}")
                self.output.delete('1.0', tk.END)
                self.output.insert(tk.END, "✅ File loaded successfully.\n")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def show_all_ips(self):
        if self.lc:
            self.output.delete('1.0', tk.END)
            self.output.insert(tk.END, "📋 All IPs:\n\n" + "\n".join(self.lc.ip_add))
        else:
            messagebox.showwarning("Warning", "Please load a log file first.")

    def show_ips_20(self):
        if self.lc:
            ips = self.lc.ip_add_20()
            self.output.delete('1.0', tk.END)
            self.output.insert(tk.END, "🧪 IPs with first octet < 20:\n\n" + "\n".join(ips))
        else:
            messagebox.showwarning("Warning", "Please load a log file first.")

    def show_ratio(self):
        if self.lc:
            ratio = self.lc.ratio()
            self.output.delete('1.0', tk.END)
            self.output.insert(tk.END, f"📊 Ratio of IPs with first octet < 20: {ratio:.2f}")
        else:
            messagebox.showwarning("Warning", "Please load a log file first.")


# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x650")
    app = LinecounterApp(root)
    root.mainloop()