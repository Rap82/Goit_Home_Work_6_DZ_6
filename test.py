from pathlib import Path    # Підключаємо функцію *Path для пошуку шляху до  файлу для читання з бібліотеки *pathlib

def write_employees_to_file( employee_list, path) :

    print (path)
   
    try: 
        fh = open (path , 'w')
        
        for employee_idex in employee_list :
            for employee in employee_idex:
            
                new_employee = employee + '\n'
                print(new_employee)
                fh.write (new_employee )
       
      

    
        


    finally:        # який би збій не був в середені коду закриває відкритий файл в кінці.

        fh.close()  # Вудована функція закритя файлу який був відкритий вище. *fh.close(), Де fh - зміна в яку передали вікритий файл , *.close() метод закриття файлу.



path = Path ( "employee_list_Zavdania_2.txt" )

employee_list = [ ["Robert Stivenson,28", "Alex Denver,30", "Drake Mikelsson,19"] ,["Ro Stiv,48", "Alx Dver,50", "Dke Mison,49"]]


write_employees_to_file(employee_list, path) 