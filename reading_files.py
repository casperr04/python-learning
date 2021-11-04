# r means read, a means append, r+ means read and write
employee_file = open("reading_files_text", "a")  # opens file, specifying directory and when we want to read
#  which_line = int(input("Which line you want to access? : "))  # asks user for which line to access
#  print(employee_file.readlines()[which_line])  # finds specified line and prints
employee_file.write("\nJome")
employee_file.close()  # closes file
