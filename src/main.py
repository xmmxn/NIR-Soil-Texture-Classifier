import tkinter as tk


class SoilTextureClassifier:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("Tkinter OOP GUI Example")

        # Add widgets or perform other actions as needed
        self.label = tk.Label(root, text="Hello, Tkinter!",
                              font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="Click Me!",
                                command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Button Clicked!")


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    # Create an instance of the MyGUI class
    my_gui = SoilTextureClassifier(root)

    # Start the Tkinter event loop
    root.mainloop()
