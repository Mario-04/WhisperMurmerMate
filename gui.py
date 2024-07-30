# gui.py
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import ttk  # Import ttk for the progress bar
from transcriber import Transcriber
import threading  # To handle transcription in a separate thread

class TranscriptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transcription App")
        self.transcriber = Transcriber()

        self.label = tk.Label(root, text="Select an audio file to transcribe")
        self.label.pack()

        self.transcription_box = Text(root, height=20, width=80)
        self.transcription_box.pack()

        self.load_button = tk.Button(root, text="Load Audio", command=self.load_audio)
        self.load_button.pack()

        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack()

    def load_audio(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.transcription_box.delete(1.0, tk.END)
            # Run the transcription in a separate thread to keep the GUI responsive
            threading.Thread(target=self.transcribe_audio, args=(file_path,)).start()

    def transcribe_audio(self, file_path):
        self.progress.start()
        language, transcription = self.transcriber.transcribe(file_path, self.update_progress)
        self.progress.stop()
        self.transcription_box.insert(tk.END, f"Detected language: {language}\n")
        self.transcription_box.insert(tk.END, transcription)

    def update_progress(self, progress):
        self.progress['value'] = progress
        self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = TranscriptionApp(root)
    root.mainloop()
