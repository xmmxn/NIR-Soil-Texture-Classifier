from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font
import os


class canvas_classifier:
    def __init__(self, root):
        self.root = root

        # Folder path for images
        image_folder = "C:\\Users\\pacom\\Desktop\\NIR_Soil_Texture_Classifier\\assets\\images"

        # Load images for canvas background
        background_image_path = os.path.join(image_folder, "rec_canvas.png")
        background_image = Image.open(background_image_path)
        self.background_image = ImageTk.PhotoImage(background_image)

        # Create a canvas with the loaded image as the background
        self.canvas = tk.Canvas(
            root, width=300, height=450, highlightthickness=0)
        self.canvas.create_image(
            0, 0, anchor=tk.NW, image=self.background_image)
        self.canvas.pack(side=tk.RIGHT, padx=20, pady=20)

        # Block of code for SAND PERCENTAGE
        # Add text layers with padding along the x-axis
        squad_font = font.Font(family="Squada One", size=20, )

        sand_label = tk.Label(root, text="Sand %",
                              bg='#EEF5E8', font=squad_font)
        self.sand_label_window = self.canvas.create_window(
            20, 40, window=sand_label, anchor='w')

        self.sand_value = tk.Label(
            root, text="0", font=squad_font, bg='#EEF5E8')
        self.sand_value_window = self.canvas.create_window(
            120, 40, window=self.sand_value, anchor='w')

        # Block of code for SILT PERCENTAGE
        silt_label = tk.Label(root, text="Silt %",
                              bg='#EEF5E8', font=squad_font)
        self.silt_label_window = self.canvas.create_window(
            20, 80, window=silt_label, anchor='w')

        self.silt_value = tk.Label(
            root, text="0", font=squad_font, bg='#EEF5E8')
        self.silt_value_window = self.canvas.create_window(
            120, 80, window=self.silt_value, anchor='w')

        # Block of code for CLAY PERCENTAGE
        clay_label = tk.Label(root, text="Clay %",
                              bg='#EEF5E8', font=squad_font)
        self.clay_label_window = self.canvas.create_window(
            20, 120, window=clay_label, anchor='w')

        # Create and place the text area
        self.clay_value = tk.Label(
            root, text="0", font=squad_font, bg='#EEF5E8')
        self.clay_value_window = self.canvas.create_window(
            120, 120, window=self.clay_value, anchor='w')

        # Add text layers with padding along the x-axis
        squada_font = font.Font(family="Squada One", size=30, )

        # Add Text "Texture Class" inside the canvas
        texture_label = tk.Label(
            root, text="TEXTURE CLASS", bg='#EEF5E8', font=squad_font)
        self.texture_label_window = self.canvas.create_window(
            150, 200, window=texture_label, anchor='center')

        # Create and place the text area
        self.texture_text = tk.Label(
            root, text=None, fg='#32620E', bg='#EEF5E8', font=squada_font)
        self.texture_text_window = self.canvas.create_window(
            150, 280, window=self.texture_text, anchor='center')
        # self.center_text(self.texture_text)

    def center_text(self, text_widget):
        # Configure a tag to center the text
        text_widget.tag_configure("center", justify='center', font=(
            'Squada One', 15, 'bold'), foreground="#32620E")

        # Apply the centering tag to the entire content
        text_widget.insert("1.0", "SAMPLE", "center")


if __name__ == "__main__":
    try:
        root = tk.Tk()
        canvas_window = canvas_classifier(root)
        root.mainloop()
    except RuntimeError as e:
        print(e)
