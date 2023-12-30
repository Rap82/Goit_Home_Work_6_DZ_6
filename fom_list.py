from pathlib import Path

# def form_lists_file_all (root_path) :

#     list_all = []
#     list_all_sufix = []
#     list_file_archives = []
#     listlist_file_video = []
#     listlist_file_audio = []
#     listlist_file_documents = []
#     listlist_file_others = []

#     for item in root_path.iterdir() :
#         print(item) 
        
#         if item.is_dir() : 
            
#             for file in item.iterdir() : 

#                  if file.is_file(): 
#                     file:Path

#                     file_sufix = file.suffix

#                     #print (file_sufix)
#                     list_all_sufix.append(file_sufix)
                                    
#                     list_all.append(file.name)

    
#     return list_all , list_all_sufix


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def dir_walk ( path, prev_list_dir ) :
#     print(prev_list_dir)
#     print(os.getcwd())
#     os.chdir(path)
#     list_dir = list ( filter ( os.listdir, os.listdir() ))
#     print (list_dir)
#     for el in list_dir :
#         list_dir.remove(el)
        
#         print(dir_walk (fr"{path}\{el}", list_dir ))


            

    # return path

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Name_dir = ( 'archives', 'video','audio', 'documents','images', 'others' ) 

# suff_images = ('JPEG', 'PNG', 'JPG', 'SVG')
# suff_video =  ('AVI', 'MP4', 'MOV', 'MKV')
# suff_documents = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
# suff_audio = ('MP3', 'OGG', 'WAV', 'AMR')
# suff_arhives = ('ZIP', 'GZ', 'TAR')

# # root_path = Path ( 'Rizne/filmy/in_filmy' )

# # path = Path ( 'Rizne/filmy/in_filmy' )

# # print ( form_lists_file_all (root_path) )

# def  lists_file_sort ( list_name_all_file , root_path) :

#     list_all_known_sufix = []
#     list_all_unknown_sufix = []
#     list_file_archives = []
#     list_file_video = []
#     list_file_audio = []
#     list_file_documents = []
#     list_file_images = []
#     list_file_others = []

#     suff_images = ('JPEG', 'PNG', 'JPG', 'SVG')
#     suff_video =  ('AVI', 'MP4', 'MOV', 'MKV')
#     suff_documents = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
#     suff_audio = ('MP3', 'OGG', 'WAV', 'AMR')
#     suff_arhives = ('ZIP', 'GZ', 'TAR')
#     # with open ( fr"{root_path}/file_info_in_dir.txt" ,'x') as fh :

#                 #    pass
    
    

#     for name in list_name_all_file :

#             suff = name.split('.')
#             #print (f'suff[1] = {suff[1]}')

#             if suff[1].upper() in suff_audio :
            
#                 list_file_audio.append ( name )
#                 list_all_known_sufix.append ( suff[1] )

#             elif suff[1].upper() in suff_video :
            
#                 list_file_video.append ( name )
#                 list_all_known_sufix.append ( suff[1] )
            
#             elif suff[1].upper() in suff_documents :
            
#                 list_file_documents.append ( name )
#                 list_all_known_sufix.append ( suff[1] )
            
#             elif suff[1].upper() in suff_images :
            
#                 list_file_images.append ( name )
#                 list_all_known_sufix.append ( suff[1] )
            
#             elif suff[1].upper() in suff_arhives :
            
#                 list_file_archives.append( name )
#                 list_all_known_sufix.append( suff[1] )
#             else :
            
#                 list_file_others.append ( name )
#                 list_all_unknown_sufix.append ( suff[1] )
            
#     list_all_known_sufix = list ( set ( list_all_known_sufix) )
#     list_all_unknown_sufix = list ( set ( list_all_unknown_sufix ) )
    
#     path_info_file = Path(f"{root_path}/file_info_in_dir.txt")
#     # print (path_info_file)
#     tab ="\t"*5
#     print (tab)
#     if not path_info_file.is_file() :
#         with open (path_info_file , "a") as fh :
#             ...
#     with open ( path_info_file,'r+') as fh :
#             fh.writelines( f'\n{tab}Список відомих скрипту розширень, що були в папці :\n\n     {list_all_known_sufix}\n\n')
#             fh.writelines( f'{tab}Список невідомих скрипту розширень, що були в папці :\n\n   {list_all_unknown_sufix}\n\n')
#             fh.writelines( f'{tab}Список всіх Музичних файлів, що були в папці :\n\n    {list_file_audio}\n\n')
#             fh.writelines( f'{tab}Список всіх Відео файлів, що були в папці :\n\n       {list_file_video}\n\n')
#             fh.writelines( f'{tab}Список всіх Документ файлів, що були в папці :\n\n    {list_file_documents}\n\n')
#             fh.writelines( f'{tab}Список всіх Фото файлів, що були в папці :\n\n        {list_file_images}\n\n')
#             fh.writelines( f'{tab}Список всіх Аріхів файлів, що були в папці :\n\n      {list_file_archives}\n\n')
#             fh.writelines( f'{tab}Список всіх Невідомих файлів, що були в папці :\n\n   {list_file_others}\n\n')
           
            
           
           


    


   



# list_name_all_file = ['3d-render-of-two-hands-covering.jpeg', '3d-trident_602782-136.jpeg', '3d_render_of_two_hands_covering.jpeg', '3d_trident_602782_136.jpeg', 'Ajd_Ajd.Ajd', 'Ajd_der.Ajd', 'AMR_ENLEO_.AMR', 'AMR_Jerry_Heil.AMR', 'AMR_Kajanna.AMR', 'AMR_KARTA_SVITU.AMR', 'AMR_Klavdia_Petrivna.AMR', 'AMR_SKOFKA.AMR', 'AMR_YARAYA.AMR', 'der_Ajd.der', 'dokumenti.zip', 'fasr_Ajd.fasr', 'filmy.zip', 'film_txt_txt.txt', 'flat-design-ukraine-national-emblems-collection_23-2149337773.SVG', 'flat-design-ukraine-national-emblems-collection_23-2149339330.jpg', 'flat_design_ukraine_national_emblems_collection_23_2149337773.SVG', 'flat_design_ukraine_national_emblems_collection_23_2149339330.jpg', 'image0.png', 'limp_Ajd.limp', 'MOVКома.MOV', 'MOVСім самураїв.MOV', 'MOVХрещений батько.MOV', 'MP3_ENLEO_.MP3', 'MP3_Jerry_Heil.MP3', 'MP3_Kajanna.MP3', 'MP3_KARTA_SVITU.MP3', 'MP3_Klavdia_Petrivna.MP3', 'MP3_SKOFKA.MP3', 'MP3_YARAYA.MP3', 'MP4SeVen&.MP4', 'Musik.zip', 'OGG_ENLEO_.OGG', 'OGG_Jerry_Heil.OGG', 'OGG_Kajanna.OGG', 'OGG_KARTA_SVITU.OGG', 'OGG_Klavdia_Petrivna.OGG', 'OGG_SKOFKA.OGG', 'OGG_YARAYA.OGG', 'PDF12_dok.PDF', 'PDFVidatki.PDF', 'PDFVolodar_.PDF', 'PDFZarplata.PDF', 'PDF_12_dok.PDF', 'PDF_Vidatki.PDF', 'PDF_Zarplata.PDF', 'PPTXDoc1.PPTX', 
# 'PPTXKom.PPTX', 'PPTXVidatki.PPTX', 'PPTXVolodar_.PPTX', 'PPTXZarplata.PPTX', 'PPTX_12_dok.PPTX', 'PPTX_Doc1.PPTX', 'PPTX_Dok23.PPTX', 'PPTX_Kom.PPTX', 'PPTX_Vidatki.PPTX', 'qwe_Ajd.qwe', 'qwe_der.qwe', 'TXTDok23.TXT', 'TXTVidatki.TXT', 'TXT_Doc1.TXT', 'ua_Ajd.ua', 'ua_der.ua', 'WAV_ENLEO_.WAV', 'WAV_Jerry_Heil.WAV', 'WAV_Kajanna.WAV', 'WAV_KARTA_SVITU.WAV', 'WAV_Klavdia_Petrivna.WAV', 'WAV_SKOFKA.WAV', 'WAV_YARAYA.WAV']

# root_path = Path ( 'Rizne/filmy/in_filmy' )



# lists_file_sort ( list_name_all_file, root_path ) 

print (ord("И") )
print (chr(1099))