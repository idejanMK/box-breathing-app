import tkinter as tk
import time
import threading
import winsound

class BoxBreathingApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Box Breath')
        self.master.geometry('220x310')  # Increased height from 280 to 310
        self.master.configure(bg='#f0f0f0')
        self.master.protocol('WM_DELETE_WINDOW', self.on_closing)
        
        # Remove window decorations
        self.master.overrideredirect(True)
        
        # Main frame
        self.main_frame = tk.Frame(master, bg='#f0f0f0')
        self.main_frame.pack(expand=True, fill='both', padx=10, pady=5)

        # Title bar
        self.title_bar = tk.Frame(self.main_frame, bg='#f0f0f0')
        self.title_bar.pack(fill='x')
        
        # Title
        tk.Label(self.title_bar, text='Box Breath', bg='#f0f0f0', 
                font=('Segoe UI', 10, 'bold'), fg='#333333').pack(side='left')
        
        # Close button
        close_button = tk.Button(self.title_bar, text='✕', bg='#f0f0f0',
                               font=('Segoe UI', 10), bd=0,
                               activebackground='#f0f0f0', fg='#666666',
                               command=self.on_closing)
        close_button.pack(side='right', padx=2)

        # Pin button
        self.stay_on_top = False
        self.pin_button = tk.Button(self.title_bar, text='📌', bg='#f0f0f0',
                                  font=('Segoe UI', 10), bd=0,
                                  activebackground='#f0f0f0', fg='#666666',
                                  command=self.toggle_stay_on_top)
        self.pin_button.pack(side='right', padx=2)

        # Custom duration inputs frame
        duration_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        duration_frame.pack(fill='x', pady=(5, 0))
        
        # Validation function for input fields (only allow integers)
        vcmd = (self.master.register(self.validate_input), '%P')
        
        # Inhale duration
        inhale_frame = tk.Frame(duration_frame, bg='#f0f0f0')
        inhale_frame.pack(side='left', expand=True)
        tk.Label(inhale_frame, text='Inhale', bg='#f0f0f0', font=('Segoe UI', 7), fg='#666666').pack(anchor='center')
        self.inhale_var = tk.StringVar(value='4')
        self.inhale_entry = tk.Entry(inhale_frame, textvariable=self.inhale_var, width=2, 
                                   font=('Segoe UI', 8), justify='center', validate='key', 
                                   validatecommand=vcmd)
        self.inhale_entry.pack(anchor='center')
        
        # First hold duration
        hold1_frame = tk.Frame(duration_frame, bg='#f0f0f0')
        hold1_frame.pack(side='left', expand=True)
        tk.Label(hold1_frame, text='Hold', bg='#f0f0f0', font=('Segoe UI', 7), fg='#666666').pack(anchor='center')
        self.hold1_var = tk.StringVar(value='4')
        self.hold1_entry = tk.Entry(hold1_frame, textvariable=self.hold1_var, width=2, 
                                  font=('Segoe UI', 8), justify='center', validate='key', 
                                  validatecommand=vcmd)
        self.hold1_entry.pack(anchor='center')
        
        # Exhale duration
        exhale_frame = tk.Frame(duration_frame, bg='#f0f0f0')
        exhale_frame.pack(side='left', expand=True)
        tk.Label(exhale_frame, text='Exhale', bg='#f0f0f0', font=('Segoe UI', 7), fg='#666666').pack(anchor='center')
        self.exhale_var = tk.StringVar(value='8')
        self.exhale_entry = tk.Entry(exhale_frame, textvariable=self.exhale_var, width=2, 
                                   font=('Segoe UI', 8), justify='center', validate='key', 
                                   validatecommand=vcmd)
        self.exhale_entry.pack(anchor='center')
        
        # Second hold duration
        hold2_frame = tk.Frame(duration_frame, bg='#f0f0f0')
        hold2_frame.pack(side='left', expand=True)
        tk.Label(hold2_frame, text='Hold', bg='#f0f0f0', font=('Segoe UI', 7), fg='#666666').pack(anchor='center')
        self.hold2_var = tk.StringVar(value='4')
        self.hold2_entry = tk.Entry(hold2_frame, textvariable=self.hold2_var, width=2, 
                                  font=('Segoe UI', 8), justify='center', validate='key', 
                                  validatecommand=vcmd)
        self.hold2_entry.pack(anchor='center')

        # Center frame for all elements
        center_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        center_frame.pack(expand=True, fill='both')
        
        # Add weight to the grid
        center_frame.grid_rowconfigure(0, weight=1)
        center_frame.grid_rowconfigure(5, weight=1)
        center_frame.grid_columnconfigure(0, weight=1)

        # Timer display
        self.timer_label = tk.Label(center_frame, text='10:00',
                                  font=('Segoe UI', 18, 'bold'),
                                  bg='#f0f0f0', fg='#333333')
        self.timer_label.grid(row=1, pady=(5, 0))  # 5px above, 0px below

        # Phase instruction
        self.phase_label = tk.Label(center_frame, text='Inhale',
                                  font=('Segoe UI', 18),
                                  bg='#f0f0f0', fg='#333333')
        self.phase_label.grid(row=2, pady=(0, 0))  # 0px padding to tighten spacing
        
        # Counter
        self.counter_label = tk.Label(center_frame, text='4',
                                    font=('Segoe UI', 60, 'bold'),
                                    bg='#f0f0f0', fg='#333333')
        self.counter_label.grid(row=3, pady=(0, 0))  # 0px padding to tighten spacing

        # Start/Stop button
        self.start_button = tk.Button(center_frame, text='START',
                                    font=('Segoe UI', 9, 'bold'),
                                    fg='white', bg='#007AFF',
                                    activeforeground='white',
                                    activebackground='#0051FF',
                                    command=self.start_breathing,
                                    width=8, height=1,
                                    relief='flat', bd=0)
        self.start_button.grid(row=4, pady=(5, 10))  # 5px above, 10px below

        # Make window draggable
        self.title_bar.bind('<Button-1>', self.start_move)
        self.title_bar.bind('<B1-Motion>', self.on_move)

        # Initialize variables
        self.is_breathing = False
        self.breathing_thread = None
        self.start_time = None
        
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry(f"+{x}+{y}")

    def toggle_stay_on_top(self):
        self.stay_on_top = not self.stay_on_top
        self.master.attributes('-topmost', self.stay_on_top)
        if self.stay_on_top:
            self.pin_button.configure(text='📍', fg='#007AFF')
        else:
            self.pin_button.configure(text='📌', fg='#666666')
            
    def validate_input(self, new_value):
        # Allow empty field or positive integers only
        if new_value == "":
            return True
        try:
            value = int(new_value)
            return value >= 0 and len(new_value) <= 2  # Limit to 2 digits (0-99)
        except ValueError:
            return False

    def start_breathing(self):
        if not self.is_breathing:
            self.is_breathing = True
            self.start_button.configure(text='STOP', bg='#FF3B30')
            self.start_time = time.time()
            self.breathing_thread = threading.Thread(target=self.breathing_cycle)
            self.breathing_thread.start()
        else:
            self.stop_breathing()

    def stop_breathing(self):
        self.is_breathing = False
        if self.breathing_thread:
            self.breathing_thread.join(0.1)
        self.start_button.configure(text='START', bg='#007AFF')
        self.phase_label.configure(text='Inhale')
        self.counter_label.configure(text='4')
        self.timer_label.configure(text='10:00')
        self.start_time = None

    def update_timer(self):
        if self.start_time is not None and self.is_breathing:
            elapsed = int(time.time() - self.start_time)
            remaining = max(600 - elapsed, 0)  # 10 minutes in seconds
            minutes = remaining // 60
            seconds = remaining % 60
            self.timer_label.configure(text=f'{minutes}:{seconds:02d}')
            if remaining == 0:
                self.stop_breathing()

    def breathing_cycle(self):
        # Get duration values from input fields, with fallback defaults
        try:
            inhale_duration = int(self.inhale_var.get() or '4')
            hold1_duration = int(self.hold1_var.get() or '4')
            exhale_duration = int(self.exhale_var.get() or '8')
            hold2_duration = int(self.hold2_var.get() or '4')
        except ValueError:
            # If any conversion fails, use defaults
            inhale_duration = 4
            hold1_duration = 4
            exhale_duration = 8
            hold2_duration = 4
        
        phases = [
            ("Inhale", inhale_duration),
            ("Hold", hold1_duration),
            ("Exhale", exhale_duration),
            ("Hold", hold2_duration)
        ]
        
        while self.is_breathing:
            for phase_name, duration in phases:
                if not self.is_breathing:
                    return
                    
                # Skip phase if duration is zero
                if duration == 0:
                    continue
                    
                self.phase_label.configure(text=phase_name)
                for i in range(duration, -1, -1):
                    if not self.is_breathing:
                        return
                    self.counter_label.configure(text=str(i))
                    self.update_timer()
                    
                    # Beep only when counter is at 1 for all phases
                    if i == 1:
                        # Schedule the beep with phase-specific timing
                        def delayed_beep(phase_type):
                            # Different timing based on phase type
                            if phase_type == "Hold":
                                time.sleep(0.85)  # Longer delay for Hold phases
                            else:
                                time.sleep(0.45)  # Shorter delay for Inhale/Exhale
                            winsound.Beep(1000, 500)
                        
                        beep_thread = threading.Thread(target=lambda: delayed_beep(phase_name), daemon=True)
                        beep_thread.start()
                        
                    # Use a more precise timing approach
                    start_time = time.time()
                    while time.time() - start_time < 1.0:
                        time.sleep(0.01)  # Short sleep to prevent CPU hogging

    def on_closing(self):
        self.stop_breathing()
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = BoxBreathingApp(root)
    root.mainloop()
