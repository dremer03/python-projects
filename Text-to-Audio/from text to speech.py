from gtts import gTTS
import os

# Записываем текст и выбираем язык
my_text = 'your text'
language = 'en'

my_obj = gTTS(text=my_text, lang=language, slow=False)

# Сохраняем файл
my_obj.save('text.mp3')

#Воспроизводим аудио (если операционная система Windows: os.system("start file")
os.system('open text.mp3')
