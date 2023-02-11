input_file = open ('grades.csv','r') #open source file
output_file = open ('grades(copy).csv','w') #create/overwrite output file
csv1 = input_file.read() #read content of source file

output_file.write(csv1) #source file content copy to output file
		
input_file.close()
output_file.close()
	
#sending email after copy is completed
from mail_noti import Email 		
print("Copy Completed! Email notification was sent!")
