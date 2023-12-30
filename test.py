
# ++++++++++++++++++++++++++++++++ Чисті коди для автоперевірки без широких коментарів. +++++++++++++++++++++

# from pathlib import Path    # Підключаємо функцію *Path для пошуку шляху до  файлу для читання з бібліотеки *pathlib

# def write_employees_to_file( employee_list, path) :

#     print (path)
   
#     try: 
#         fh = open (path , 'w')
        
#         for employee_idex in employee_list :
#             for employee in employee_idex:
            
#                 new_employee = employee + '\n'
#                 print(new_employee)
#                 fh.write (new_employee )
       
      

    
        


#     finally:        # який би збій не був в середені коду закриває відкритий файл в кінці.

#         fh.close()  # Вудована функція закритя файлу який був відкритий вище. *fh.close(), Де fh - зміна в яку передали вікритий файл , *.close() метод закриття файлу.



# path = Path ( "employee_list_Zavdania_2.txt" )

# employee_list = [ ["Robert Stivenson,28", "Alex Denver,30", "Drake Mikelsson,19"] ,["Ro Stiv,48", "Alx Dver,50", "Dke Mison,49"]]


# write_employees_to_file(employee_list, path) 


# ***************************************************************************************************************************


# from pathlib import Path   

# import re  
# def read_employees_from_file (path) :

#     try:   

#         fh = open (path , "r")  
#         lines = fh.readlines() 
       
#         patern = "\n"   
#         replace = "" 

#         list_employees_from_file = []

#         for line in lines : 
#             employee_from_file = re.sub (patern, replace , line ) 

#             list_employees_from_file.append(employee_from_file)
    
#         return  list_employees_from_file 

#     finally:        
#         fh.close() 

# path = Path ( "employee_list_Zavdania_2.txt" )

# print(read_employees_from_file (path))






# from pathlib import Path
# import re

# def get_cats_info(path):
 
 
#  cats_info_list_all = []
#  Key_for_dict = ["id", "name", "age"]
#  cat_info_dict_up = {}

#  with open (path , "r") as fh :
        
#       #print (path)
#       cats_info = fh.readlines()
#       #print (cats_info)
#       patern = "\n"   
#       replace = ""
#       for cat_inf in cats_info :
#          cat_info =  re.sub (patern, replace , cat_inf ) 
#          #print(cat_info)
#          cat_info_list = re.split (",", cat_info)
#          #print(cat_info_list)
#          cat_info_dict_up = dict(zip(Key_for_dict,cat_info_list))      
         
            
#          print (cat_info_dict_up)
         
#          cats_info_list_all.append(cat_info_dict_up)
#       #print(f"cats_info_list_all = {cats_info_list_all}\n")
#  return cats_info_list_all


# byte_string = b'Hello world!'
# byte_string = 'some text'.encode()
# print (byte_string[1])

# s = "Привіт!"

# utf8 = s.encode()
# print(utf8)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'

# utf16 = s.encode('utf-16')
# print(utf16)  # b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00'

# s_from_utf16 = utf16.decode('utf-16')
# print(s_from_utf16 == s)  # True


# import shutil

# archive_name = shutil.make_archive('backup', 'zip', path.iterdir())
# shutil.unpack_archive(archive_name, 'new_folder_for_data')


#============================ Робота з файлами на зчитування. ====================
    
# file = open ("text.txt" , "r") 

# while True :  # Цикл для щитування файла по 5 байт (в кодіровці utf-8 че по символьно , оскльки символ в цій кодіровці кодується 8 біт ,тобто 1 байт, в utf-16 - 16 біт відповідно тобто 2 байти на 1 символ і так далі. Якщо кодування невказано значить це utf-8 (позамовчуванню) Примітка ( utf-8 є символи які займають 2 байта .)
#         txt = file.read (5) # записувати в зміну 5 біт з файлу.Пісяля зчитування курсор переміщається на ці 5 символів далі. і зчитує наступних 5 . Читаються всі символи навіть ті що візулально невидно , пробіли табуляції ,переноси на новий рядок і так далі.
#         print (txt)         # Принтимо по 5 біт на кожному кроці циклу. 
        
#         if not txt :        # Умова виходу з циклу. Поки незявиться пуста стріча . Оскльки метод *.read() повертає тільки тип даних стріча . коли дані закінчаться він буде поаертати пусти стрічку до безкінечності. 
#             break           # break -перериваємо поточний цикл коли умва виконалась. Тобто пішли пості стічки що означає файл закінчився. 

# file.close()                # Закриваємо файл.

# #Порядкове з читування  метод .readline (). Зчитує один рядок.і повертає рядок.

# file = open ("text.txt" , "r") 

# while True :  # Цикл для щитування файла по рядку.
#         txt = file.readline () # записувати в зміну один рядок (до символу переносу рядка *\n) з файлу і повертає цей рядок у зміну.
#         print (txt)         # Принтимо по 5 біт на кожному кроці циклу. 
        
#         if not txt :        # Умова виходу з циклу. Поки незявиться пуста стріча . Оскльки метод *.read() повертає тільки тип даних стріча . коли дані закінчаться він буде поаертати пусти стрічку до безкінечності. 
#             break           # break -перериваємо поточний цикл коли умва виконалась. Тобто пішли пості стічки що означає файл закінчився. 

# file.close()                # Закриваємо файл.

# #Порядкове з читування  метод .readlineі (). Зчитує всі рядки по одному .і повертає список рядків.Для зчитування файлу цим способом цикл непотрібний. Потрібно слідкувати щоб вистачило оперативної паямті копютера на зчитування всього файлу одночас.

# file = open ("text.txt" , "r") 

# txt = file.readlines () # записувати в зміну всі  рядоки (до символу переносу рядка *\n) з файлу і повертає цей рядок у зміну.
# print (txt)         # Принтимо по 5 біт на кожному кроці циклу. 
        
        

# file.close()                # Закриваємо файл.


#============================ Робота з файлами на запис. ====================

# with open ("text.txt" , 'w') as fn : # відкрити файл на запис. Все що було перед тим в файлі витруться коли файл закриється.режим "w".відкрито для запису через менеджер контексту with ... as : 

# with open ("text.txt" , 'a') as fn : # відкрити файл на запис. Все що було перед тим в файлі p,tht;tnmcz  файл закриється.режим "a" режим дозапису файла. Дані по замовчуванню записуються в кінці файла..відкрито для запису через менеджер контексту with ... as : 

# with open ("text.txt" , 'x') as fn : # Відкрити файл в режимі "x" - Створює файл з відповдною назвою якщо такий файл не існує , і видає помилку якщо існує . Опрацювавши помилку ми можемо гарантовано перевірити що файла з такою назвою вже існує і потрібно змінти назву нашого файлу інакше перезапише існуючий.  . Потрібно щоб часом неперезаписати існуючий вже файл з такм же імя. 
# with open ("text.txt" , 'r+') as fn : # відкрити файл на читання і запис . записує в місце де вказує курсор. Позамовчуванню в кінці файла але задопомого методу .seek(). Все що було перед тим в файлі p,tht;tnmcz  файл закриється.режим "a" режим дозапису файла. Дані по замовчуванню записуються в кінці файла..відкрито для запису через менеджер контексту with ... as : 

#============================ Робота з файлами архіви .біліотека  shutil ====================

# import shutil,re
# from pathlib import Path

# shutil.make_archive("bacup" , "zip", "Work_6_DZ_6/") # shutil.make_archive("*імя_архів" , "*імя_архівтора" , "імя_папки_яку_хочемо_заархівувати/")Створюємо архів папки  в поточній папці де знаходться файл який виконує Python(в нашому випадку test.py знаходиться в папці "Goit_Home_Work_6_DZ_6" , "Work_6_DZ_6/"- папка яку будемо архівувати ,де / в кінці вказує що потрібно відкрити вміст цієї папки. )
#                                                                # "bacup"- назва архів який створиться , "zip" - архіватор *zip буде використаний , "Goit_Home_Work_6_DZ_6/" -  папка  яку будемо архівувати.

# path_file = Path ("bacup.zip")
# extract_dir = Path ("bacup")

# format = "zip"
# print (path_file)
# #print(extract_dir)
# print(format)

# shutil.unpack_archive(path_file , extract_dir, format )

# # suf_file ='.zIp'
# # format_unpack_arhive = re.sub(r'\.', '', suf_file.lower() )
# # print(format_unpack_arhive)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




from pathlib import Path
import re , os, shutil, sys, pathlib

TRANS = {
        1072: 'a', 1040: 'A', 1073: 'b', 1041: 'B', 1074: 'v', 1042: 'V', 1075: 'g', 1043: 'G', 1076: 'd', 1044: 'D',
        1077: 'e', 1045: 'E', 1105: 'e', 1025: 'E', 1078: 'j', 1046: 'J', 1079: 'z', 1047: 'Z', 1080: 'i', 1048: 'I',
        1081: 'j', 1049: 'J', 1082: 'k', 1050: 'K', 1083: 'l', 1051: 'L', 1084: 'm', 1052: 'M', 1085: 'n', 1053: 'N', 
        1086: 'o', 1054: 'O', 1087: 'p', 1055: 'P', 1088: 'r', 1056: 'R', 1089: 's', 1057: 'S', 1090: 't', 1058: 'T', 
        1091: 'u', 1059: 'U', 1092: 'f', 1060: 'F', 1093: 'h', 1061: 'H', 1094: 'ts', 1062: 'TS', 
        1095: 'ch', 1063: 'CH', 1096: 'sh', 1064: 'SH', 1097: 'sch', 1065: 'SCH', 1098: '', 1066: '', 1099: 'y', 1067: 'Y', 
        1100: '', 1068: '', 1101: 'e', 1069: 'E', 1102: 'yu', 1070: 'YU', 1103: 'ya', 1071: 'YA', 1108: 'je', 1028: 'JE', 
        1110: 'i', 1030: 'I', 1111: 'ji', 1031: 'JI', 1169: 'g', 1168: 'G'
        }

dict_sufixes = {
    '.ZIP': 'archives', '.GZ': 'archives', '.TAR': 'archives', 
    '.AVI': 'video', '.MP4': 'video', '.MOV': 'video', '.MKV': 'video', 
    '.MP3': 'audio', '.OGG': 'audio', '.WAV': 'audio', '.AMR': 'audio', 
    '.DOC': 'documents', '.DOCX': 'documents', '.TXT': 'documents', '.PDF': 'documents', '.XLSX': 'documents', '.PPTX': 'documents', 
    '.JPEG': 'images', '.PNG': 'images', '.JPG': 'images', '.SVG': 'images', 
    'others': 'others'
    }  # Словник в якому в нас записанні як ключі всі наші розширення які потрібно перевірити за умовами завдання а значення якій категорії ці розширення належать. 

Name_dir = ( 'archives', 'video','audio', 'documents','images', 'others' )
list_name_all_file = []

# def form_lists_file_all (file_name_curent) :

#     list_all = []
#     list_all.append (file_name_curent)

#     return list_all

def normalize ( file_name ) :

    patern = r"\W"
    replace = "_"

    normalize_file_name = re.sub ( patern, replace , file_name )
        
    new_file_name = normalize_file_name.translate(TRANS)

    return  new_file_name

# def form_lists_file_all (file_name) :
#     pass


def unpack_archive ( new_path_file_arhive, extract_arhive_dir_name, format_unpack_arhive ) :

    try : 

        shutil.unpack_archive ( new_path_file_arhive, extract_arhive_dir_name , f'{format_unpack_arhive}' )

    except:
        print(f'Bad arhive was delete <{ new_path_file_arhive }>')

        os.remove( new_path_file_arhive )


def replace_files ( root_path , path_file ) :

    name_file = normalize ( path_file.stem )

    suf_file =  path_file.suffix  

    category = dict_sufixes.get ( suf_file.upper(), 'others' ) 

    new_path_dir = Path ( f'{root_path}/{category}' ) 
    
    

    if not new_path_dir.exists() : 

        new_path_dir.mkdir()    
    

    file_name_curent = f'{name_file}{suf_file}'
    
    list_name_all_file.append( file_name_curent )
                                    
    path_file.replace ( new_path_dir/f"{name_file}{suf_file}" ) #Перенесення файлів в папки з відповідними категоріями.

    if suf_file.upper() in ('.ZIP', '.GZ', '.TAR') :

        new_path_file_arhive = Path ( f'{ new_path_dir }/{ name_file }{ suf_file.lower() }' )
        
        extract_arhive_dir_name = Path (f'{ new_path_dir }/{ name_file }')

        format_unpack_arhive = re.sub (r'\.', '', suf_file.lower() )

        unpack_archive ( new_path_file_arhive, extract_arhive_dir_name, format_unpack_arhive )
    
    return list_name_all_file


def sort_dir ( root_path , path ) :

    try :
     
     for item in path.iterdir() : 

        if item.is_file(): 
            
            replace_files ( root_path, item )
            
            
        if item.is_dir() : 

            if not item.stem in Name_dir :
                
                sort_dir ( root_path , item ) 
           
            if len ( os.listdir ( item ) ) == 0 :
                
                item.rmdir() 
    
    except:
       
       pass 
    lists_file_sort ( list_name_all_file , root_path)     

def  lists_file_sort ( list_name_all_file , root_path) :

    list_all_known_sufix = []
    list_all_unknown_sufix = []
    list_file_archives = []
    list_file_video = []
    list_file_audio = []
    list_file_documents = []
    list_file_images = []
    list_file_others = []

    suff_images = ('JPEG', 'PNG', 'JPG', 'SVG')
    suff_video =  ('AVI', 'MP4', 'MOV', 'MKV')
    suff_documents = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    suff_audio = ('MP3', 'OGG', 'WAV', 'AMR')
    suff_arhives = ('ZIP', 'GZ', 'TAR')
    # with open ( fr"{root_path}/file_info_in_dir.txt" ,'x') as fh :

                #    pass
    
    

    for name in list_name_all_file :

            suff = name.split('.')
            #print (f'suff[1] = {suff[1]}')

            if suff[1].upper() in suff_audio :
            
                list_file_audio.append ( name )
                list_all_known_sufix.append ( suff[1] )

            elif suff[1].upper() in suff_video :
            
                list_file_video.append ( name )
                list_all_known_sufix.append ( suff[1] )
            
            elif suff[1].upper() in suff_documents :
            
                list_file_documents.append ( name )
                list_all_known_sufix.append ( suff[1] )
            
            elif suff[1].upper() in suff_images :
            
                list_file_images.append ( name )
                list_all_known_sufix.append ( suff[1] )
            
            elif suff[1].upper() in suff_arhives :
            
                list_file_archives.append( name )
                list_all_known_sufix.append( suff[1] )
            else :
            
                list_file_others.append ( name )
                list_all_unknown_sufix.append ( suff[1] )
            
    list_all_known_sufix = list ( set ( list_all_known_sufix) )
    list_all_unknown_sufix = list ( set ( list_all_unknown_sufix ) )
    path_info_file = Path(f"{root_path}/file_info_in_dir.txt")
    # print (path_info_file)
    if not path_info_file.is_file() :
        with open (path_info_file , "a") as fh :
            ...

    tab ="\t"*5
    with open ( path_info_file, 'w') as fh :
            fh.writelines( f'\n{tab}Список відомих скрипту розширень, що були в папці :\n\n     {list_all_known_sufix}\n\n')
            fh.writelines( f'{tab}Список невідомих скрипту розширень, що були в папці :\n\n   {list_all_unknown_sufix}\n\n')
            fh.writelines( f'{tab}Список всіх Музичних файлів, що були в папці :\n\n    {list_file_audio}\n\n')
            fh.writelines( f'{tab}Список всіх Відео файлів, що були в папці :\n\n       {list_file_video}\n\n')
            fh.writelines( f'{tab}Список всіх Документ файлів, що були в папці :\n\n    {list_file_documents}\n\n')
            fh.writelines( f'{tab}Список всіх Фото файлів, що були в папці :\n\n        {list_file_images}\n\n')
            fh.writelines( f'{tab}Список всіх Аріхів файлів, що були в папці :\n\n      {list_file_archives}\n\n')
            fh.writelines( f'{tab}Список всіх Невідомих файлів, що були в папці :\n\n   {list_file_others}\n\n')
           
  

    

root_path = Path ( 'Rizne/filmy/in_filmy' )

path = Path ( 'Rizne/filmy/in_filmy' )

# print ( root_path , path )


sort_dir ( root_path , path )

#print (list_name_all_file)

