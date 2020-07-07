import os

def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    else:
        print(folder,' folder already exists')

os.chdir('C:\\Users\\user\\testing')

files = os.listdir()

createIfNotExists('Images')
createIfNotExists('Docs')
createIfNotExists('Medias')
createIfNotExists('Others')

imageExt = ['.jpg','.png','.jpeg','.gif']
images = [file for file in files if os.path.splitext(file)[1].lower() in imageExt ] # ('kartik','.png')
print(images)

docExt = ['.docx','.txt','.pdf','.doc','.xlsx']
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExt ] # ('kartik','.png')
print(docs)

mediaExt = ['.mp4','.mp3']
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt ] # ('kartik','.png')
print(medias)

others = []

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if ext not in imageExt and ext not in docExt and ext not in mediaExt and os.path.isfile(file):
        others.append(file)

print(others)

def move(folder,files):
    for file in files:
        os.replace(file,f'{folder}\\{file}')

move('Images',images)
move('Docs',docs)
move('Medias',medias)
move('Others',others)