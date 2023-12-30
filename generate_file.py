import shutil

from pathlib import Path

def creat_file (file_name, sufix, path) :
    print (path)
    
    for el in file_name :

        for el_suf in sufix :
            with open (fr'{path}\\{el_suf}_{el}.{el_suf}', 'x') as fh : 
                pass

           
        

        


# path = Path ("C:\\Users\\User\\Desktop\\Rizne\\filmy\\in_filmy")

# path = Path ("C:\\Users\\User\\Desktop\\Rizne\\Musik")
# path = Path ("C:\\Users\\User\\Desktop\\Rizne\\документи")

# path = Path ("C:\\Users\\User\\Desktop\\Rizne\\зображення")
# path = Path ("C:\\Users\\User\\Desktop\\Rizne\\музика")
# path = Path ("C:\\Users\\User\\Desktop\\Rizne\\")



#  file_name = ["Втеча з Шоушенка", "Хрещений батько", "SeVen&", "Кома", "Бійцівський клуб", "Володар перснів Дві вежі","Сім самураїв"]
# sufix = ['AVI', 'MP4', 'MOV', 'MKV']

# file_name = ["Doc1", "Док23", "12_док", "Ком", "Зарплата", "Володар ","Видатки"]

# sufix = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']

# sufix = ['MP3', 'OGG', 'WAV', 'AMR']

# file_name = ["KARTA SVITU", "Кажанна", "Klavdia Petrivna", "SKOFKA", "Jerry Heil", "ENLEO ","YARAYA"]

# sufix =['ZIP', 'GZ', 'TAR']

# sufix = ['ua', 'fasr', 'der','qwe','Ajd', 'limp']
# file_name = ['ua', 'fasr', 'der','qwe','Ajd', 'limp']


# creat_file (file_name, sufix, path)

# def create_backup(path, file_name):
    
#         archive_name = shutil.make_archive(fr"{path}\\{file_name}", "zip", path)

#         return archive_name

# path = Path ("C:\\Users\\User\\Desktop\\Rizne")
# file_name = "Musik"
# create_backup(path, file_name)

lists_names = 'archives,video,audio,documents,images,others'.split(",")
lists_sufixes = [ ['.ZIP', '.GZ', '.TAR'] , ['.AVI', '.MP4', '.MOV', '.MKV'] , ['.MP3', '.OGG', '.WAV', '.AMR'] , ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'] ,  ['.JPEG', '.PNG', '.JPG', '.SVG'], ['others'] ]
#print(lists_names)            

dict_sufixes = {}
     

dict_dir = {
        'archives': ['.ZIP', '.GZ', '.TAR'], 
        'video': ['.AVI', '.MP4', '.MOV', '.MKV'], 
        'audio': ['.MP3', '.OGG', '.WAV', '.AMR'], 
        'documents': ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'], 
        'images': ['.JPEG', '.PNG', '.JPG', '.SVG'], 
        'others': ['others']
        }

dict_sufixes = {
    '.ZIP': 'archives', '.GZ': 'archives', '.TAR': 'archives', 
    '.AVI': 'video', '.MP4': 'video', '.MOV': 'video', '.MKV': 'video', 
    '.MP3': 'audio', '.OGG': 'audio', '.WAV': 'audio', '.AMR': 'audio', 
    '.DOC': 'documents', '.DOCX': 'documents', '.TXT': 'documents', '.PDF': 'documents', '.XLSX': 'documents', '.PPTX': 'documents', 
    '.JPEG': 'images', '.PNG': 'images', '.JPG': 'images', '.SVG': 'images', 
    'others': 'others'
    }

count = 0 
    
for name in lists_names :
    #print (name )
         
    dict_dir[name] = lists_sufixes[count]
    #print(lists_sufixes[count])
    count += 1


for categ , sufix in dict_dir.items() :
   dict_sufixes.update( dict.fromkeys(sufix,categ))

#print (dict_dir)
print(dict_sufixes)








    
   
  




