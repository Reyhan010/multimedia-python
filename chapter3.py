# from moviepy.editor import VideoFileClip
# from moviepy.editor import concatenate_videoclips
# from moviepy.editor import vfx



# # Memuat file video
# video = VideoFileClip('onePiece.mp4')

# # Menyimpan file video
# video.write_videofile('result.mp4')

# short_video = video.subclip(0, 7)  # Mendapatkan 10 detik pertama
# short_video.write_videofile('short_result.mp4')



# combined_video = concatenate_videoclips([video, short_video])
# combined_video.write_videofile('combined_result.mp4')


# reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
# reversed_video.write_videofile('reversed_result.mp4')
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import pygame

# Inisialisasi pygame mixer
pygame.mixer.init()

# Fungsi untuk memutar musik
def play_music(file_path='combine.wav'):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error playing audio: {e}")

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Memuat gambar menggunakan Pillow
image = Image.open('cropped_result.jpeg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=lambda: play_music('result.wav'))
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()