import tkinter as tk
import vlc  # Using python-vlc to play radio streams

class RadioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Radio App")

        # Create a label
        self.label = tk.Label(root, text="Select a Radio Station")
        self.label.pack()

        # Create a listbox to display radio stations
        self.station_list = tk.Listbox(root, selectmode=tk.SINGLE)
        self.station_list.pack()

        # Add radio stations to the list (you can add more)
        self.radio_stations = {
            "Station 1": "http://url.to.your.radio.station1",
            "Station 2": "http://url.to.your.radio.station2",
            # Add more stations as needed
        }

        for station in self.radio_stations:
            self.station_list.insert(tk.END, station)

        # Create a play button
        self.play_button = tk.Button(root, text="Play", command=self.play_radio)
        self.play_button.pack()

        # Initialize VLC instance for media playback
        self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        self.player = self.instance.media_player_new()

    def play_radio(self):
        # Get the selected radio station
        selected_index = self.station_list.curselection()
        if selected_index:
            station_name = self.station_list.get(selected_index)
            station_url = self.radio_stations.get(station_name)
            
            # Stop the player if it's already playing
            if self.player.is_playing():
                self.player.stop()

            # Load and play the selected station
            media = self.instance.media_new(station_url)
            self.player.set_media(media)
            self.player.play()


def main():
    root = tk.Tk()
    app = RadioApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
