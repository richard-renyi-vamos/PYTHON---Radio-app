import tkinter as tk
from tkinter import messagebox
import vlc

# Create the radio app class
class RadioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Radio App")
        self.root.geometry("400x200")

        # VLC instance to play the radio streams
        self.player = vlc.MediaPlayer()

        # Adding labels and buttons
        self.label = tk.Label(root, text="Select a Radio Station", font=("Arial", 16))
        self.label.pack(pady=20)

        # Add buttons for different radio stations
        self.station1_button = tk.Button(root, text="Station 1", command=self.play_station1)
        self.station1_button.pack(pady=10)

        self.station2_button = tk.Button(root, text="Station 2", command=self.play_station2)
        self.station2_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_radio, bg="red", fg="white")
        self.stop_button.pack(pady=10)

    # Define the radio stations
    def play_station1(self):
        station_url = "http://stream-url-for-station1"  # Replace with an actual URL
        self.play_radio(station_url)

    def play_station2(self):
        station_url = "http://stream-url-for-station2"  # Replace with an actual URL
        self.play_radio(station_url)

    # Function to play radio
    def play_radio(self, url):
        self.player.set_media(vlc.Media(url))
        self.player.play()

    # Function to stop the radio
    def stop_radio(self):
        self.player.stop()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RadioApp(root)
    root.mainloop()
