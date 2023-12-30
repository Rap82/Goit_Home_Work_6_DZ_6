
from pathlib import Path
import re ,os,shutil,sys,pathlib

Name_dir =('archives', 'video','audio', 'documents', 'others' )
dict_sufixes = {
    '.ZIP': 'archives', '.GZ': 'archives', '.TAR': 'archives', 
    '.AVI': 'video', '.MP4': 'video', '.MOV': 'video', '.MKV': 'video', 
    '.MP3': 'audio', '.OGG': 'audio', '.WAV': 'audio', '.AMR': 'audio', 
    '.DOC': 'documents', '.DOCX': 'documents', '.TXT': 'documents', '.PDF': 'documents', '.XLSX': 'documents', '.PPTX': 'documents', 
    '.JPEG': 'images', '.PNG': 'images', '.JPG': 'images', '.SVG': 'images', 
    'others': 'others'
    }  # Словник в якому в нас записанні як ключі всі наші розширення які потрібно перевірити за умовами завдання а значення якій категорії ці розширення належать. 

def unpack_archive (new_path_file_arhive, extract_arhive_dir_name, format_unpack_arhive) :

    try : 
        shutil.unpack_archive (new_path_file_arhive, extract_arhive_dir_name , f'{format_unpack_arhive}' )
    except:
        print(f'Bad arhive was delete <{new_path_file_arhive}>')
        os.remove(new_path_file_arhive)


def replace_files ( root_path , path_file ) :

    name_file = path_file.stem    # Метод *шлях(path).stem .Повертає імя файлу .Те що до розширення. (з С:\User\documents\text.txt поверне *text)
    suf_file =  path_file.suffix  # Метод *шлях(path).suffix .Повертає розширення файлу .Те що після імені(повертає розширення). (з С:\User\documents\text.txt поверне *.txt)
    
    category = dict_sufixes.get ( suf_file.upper(), 'others' ) # Щоб визначити в яку папку переносити файл , замість циклу можна напряму звернутись в наш словник Методом *"імя_словник".get [ *"імя_ключа", *"не обовязковий параметер вказує яке значення повернути якщо ключа неайдеться" ] 
                                                    # *dict_sufixes в  якому є записані всі потрібні нам суфікси у вигляді ключів і значення у вигляді папок які відповідають цим ключам.
                                                      # *dict_sufixes - наш словник.
                                                      # *suf_file поточне розширення нашого файлу переданого в функцію . 'others' - другий параметр (не обовязковий) В нашому випадку потрібний щоб якщо за поточним  ключем *suf_file не найшлось ключа з словника *dict_sufixes і невиникла помилка .
                                                      # ми для всіх таких ключів повертаємо значення в *category другого параметру , в нашому випадку 'others'
                                                      # Тобто всім файлам з невідомим розширеням (ті що неописані в *dict_sufixes) ми *category присвоюємо значеня *otehers
                                                      # *category буде містити імя підпапки в яку потрібно перемістити наш поточний файл. Або в під папку значень з словника або в *others якщо не має співпадінь по розширеню з кючами словника  *dict_sufixes
    #print(f'category={category}')  # тесттовий принт.
    
    #  +++++++++++++++++++ Опрацювання шляху для ереносу нашого поточного файлу за допомогою циклу *for - зпоживає більше ресурсів ніж проходження по вже готовому словнику. . ++++++++++++++++++++++++++++  
    # for  sufixes , categ  in dict_sufixes.items() : # Цикл в якому походимось по словнику  ключ ,значення метод *'імя_словника'.items() повертає першій зміннії з циклу завжди ключ а дрігії значеня.
                                                      # В нашому випадку *sufixes буде мітисти поточний ключ ,а *categ - поточне значення для цього ключа з словника *dict_sufixes
        
    #     if suf_file == sufixes :                    # Перевіряємо чи наше розширеня з файлу  *suf_file - передане в функцію *replace_files (root_path, path_file ) дорівнює одному з ключів з словника . Якщо дорівнює значить даний файл потрібно перести в відповідну папку на яку вказує значення цього ключа з словника *dict_sufixes
                                                    
    #         category =  categ                       # Приклад якщо *suf_file == ".AVI" то ctegory == 'video'. як тільки находим співпадіння цикл зупиняєо операторм *break
    #         break                                   # Зипиняємо цикл.
    # else :                                          # Якщо в нашму словнику немає співпадінь з поточним суфіксом(розширенням) то спрацьовує *else . В такому випадку це не відоме розширення Переносомо файл з таким розширенням у папку *others
        
    #     category =  'others'                        # Для побудови шляху до файлу з  невідомомим нам розиренням  в *category =  'others'. за вказаним шляхом перенесемо наш файл в подальшому тілі програми.
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # new_path_dir: Path            # Анотація типу . Явно вказуємо тип даних які передамо в зміну. *імя_змної : *Тип даних. (вцьому випадку new_path_dir: Path  де *new_path_dir - імя зміної , двокрапка *: - знак анотації , *Path - тип даних Path(шлях) )
    new_path_dir = Path( f'{root_path}/{category}') # зміна *new_path_dir прийме шлях до відповідної деректорії(під папки). де root_path - корінева папка в якій виконуємо сортування по заданим в умові в завдані. */category - під папка в яку будемо переносити файли відповідні до категорії.
    
    

    if not new_path_dir.exists() :  # Перевіряємо чи вказаний шлях вказує на існуючу папку (шлях до папки і сама папка це різні речі).
                                    # Метод *шлях(path).exists()  -Повертає True якщо шлях вказує на існуючу папку чи файл і False якщо за вказаним шляхом такого файла чи папки не існує.
        new_path_dir.mkdir()        # Якщо спрацює *if not new_path_dir.exists() значить за вказаним шляхом немає потрібної папки . Створюємо її за допомогою методу *шлях(path).mkdir() .
                                    # *шлях(path).mkdir() створює фізично папку на диску  за вказаним шляхом з іменем на яке вказує шлях.
    path_file.replace ( new_path_dir/f"{name_file}{suf_file}" )

    if suf_file.upper() in ('.ZIP', '.GZ', '.TAR') :

        new_path_file_arhive = Path (f'{new_path_dir}/{name_file}{suf_file.lower()}')
        # exstract_dir_arhive = Path (f'{new_path_dir}/{name_file}')
        print(f'new_path_file_arhive === {new_path_file_arhive}')
        extract_arhive_dir_name = Path (f'{new_path_dir}/{name_file}')
        format_unpack_arhive = re.sub (r'\.', '', suf_file.lower() )
        print(extract_arhive_dir_name )

        print( f' format_unpack_arhive = { format_unpack_arhive }')
        unpack_archive (new_path_file_arhive, extract_arhive_dir_name, format_unpack_arhive)


def sort_dir ( root_path , path ) :

   
     for item in path.iterdir() : #Цикл в якому проходимомсь по всім папкам і файлам в поточній дерикторії. *item на кожнії ітерації циклу буде мітити шлях(свій path) на папку в поточній папці на яку ваказує *path переданий в функцію *sort_dir(path)
        # print(f"шлях {item}")
        if item.is_file(): #  Перевіряємо чи поточний шлях (*item) вказує на файл .Метод *шлях.is_file() повертає True якщо це імя файлу і False якщо це не так.
            
            replace_files (root_path, item)
            
            # print (f'i is file = {item}') # Принтемо відносний шлях до кожного файлу в поточній папці.Для нашого випадку *Rizne\Ajd_der.Ajd де Rizne - це поточна папка на яку вказує початковий *path , Ajd_der.Ajd - імя одного з файлів в цій папці.
            
        if item.is_dir() :   # перевіряємо чи шлях *item вказує на папку  . *шлях.is_dir() Повертає True якщо папка False якщо ні.
            if not item.stem in Name_dir :
                print(item)
                sort_dir ( root_path , item ) # якщо Папка то викликаємо ще раз *sort_dir ( path ) і знову перевіряємо вже поточну папку на вміст. Рекурсивний виклик. *item на даному кроці вказує вже на підпапку.
                               # і так скльки буде вкладених папок на таку глибину функція зайде і перевірить всі папки і файли. Якщо глибше папок не виявиться функція перестане себе викликкати .(Схлопниця.)   
           
            if len(os.listdir(item)) == 0 : #Перевіряємо чи папка пуста (її довжина буде рівна 0)
                print ( "era")
                item.rmdir() # Якщо пуста видаляємо цю папку.


root_path = Path ('Rizne/filmy/')
path = Path ('Rizne/filmy/in_filmy')

print (root_path , path )

sort_dir ( root_path , path )

