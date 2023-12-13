
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






from pathlib import Path
import re

def get_cats_info(path):
 
 
 cats_info_list_all = []
 Key_for_dict = ["id", "name", "age"]
 cat_info_dict_up = {}

 with open (path , "r") as fh :
        
      #print (path)
      cats_info = fh.readlines()
      #print (cats_info)
      patern = "\n"   
      replace = ""
      for cat_inf in cats_info :
         cat_info =  re.sub (patern, replace , cat_inf ) 
         #print(cat_info)
         cat_info_list = re.split (",", cat_info)
         #print(cat_info_list)
         cat_info_dict_up = dict(zip(Key_for_dict,cat_info_list))      
         
            
         print (cat_info_dict_up)
         
         cats_info_list_all.append(cat_info_dict_up)
      #print(f"cats_info_list_all = {cats_info_list_all}\n")
 return cats_info_list_all