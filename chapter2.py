from PIL import Image
from PIL import ImageFilter
from pydub import AudioSegment



# Memuat gambar
image = Image.open('Zee.jpeg')

# Menyimpan gambar
image.save('result.jpeg')


#crop
cropped_image = image.crop((50, 50, 200, 200))
cropped_image.save('cropped_result.jpg')


#resize
resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')
#filter

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpeg')




#audio
# Memuat file audio
audio = AudioSegment.from_file('rannu.mp3')

# Menyimpan file audio
audio.export('result.mp3', format='mp3')

#crop audio
clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')

#menggabungAudio
combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')

#mengubah format audio
audio.export('result.wav', format='wav')

#menambah volume
louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')