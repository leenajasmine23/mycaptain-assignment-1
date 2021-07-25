
import csv

def write_into_csv(into_list):
  with open('student_into.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    if csv_file.tell() ==0 :
      writer.writerow(["Name", "Age", "Contact number", "E-Mail ID"])
      
    writer.writerow(info_list)
    
if__name__== '__main__':
  condition = true
  student_num = 1
  
  while(condition):
    student_info = input("enter student information for student #{} in the following format(Name Age Contact_number Email_ID): ".format(student_num))
    
    # split
    student_info_list = student_info.split(' ')
    
    printf("\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nE-mail ID: {}"
           .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
    choice_check = input("Is the entered information correct: (yes\no): ")
    if choice_check == "yes":
      write_info_csv(student_info_list)
      condition_check =input("Enter (yes\no) if you want to enter information for another student: ")
      if condition_check == "yes":
        condition = true
        student_num = student_num + 1
      elif choice_check == "no":
       condition = false
      elif choice_check == "no":
        print("\nPlease re-enter the values!")
