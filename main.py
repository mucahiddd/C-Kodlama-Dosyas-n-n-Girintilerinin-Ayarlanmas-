import os

def code_cleaner(filename):
	try:
		temp_file = filename[0:(len(filename)-4)] + "_temp.txt"	#Adding the "_temp.txt" to filename
		main_file_ptr = open(filename,"r")	#Creating file pointer for the main code file
		temp_file_ptr = open(temp_file,"w")	#Creating file pointer for temp file
		count=0				#variable to keep count of the number of "{" or "}"
		for line in main_file_ptr:
			spaces = '  '*count		#Giving count number of tabs from next line onwards
			tab_count = line.count('  ')
			line = line.replace('  '*tab_count,'')
			print(tab_count)		
			if "{" in line:
				count+=1	#incrementing count whenever "{"
				#print count
			if "}" in line:
				count-=1		#Decrementing count whenever "}"
				spaces = '  '*count
				#print count

			temp_file_ptr.write(spaces)	#First writing spaces into every line
			temp_file_ptr.write(line)	#Then copy contents of every line from main code

		os.remove(filename)			#Deleting main code file
		os.rename(temp_file,filename)		#Renaming the temp file with main code file

		return count
	except IOError:		#If wrong file name gives
		print("no such file")



if __name__ == '__main__':


	code_cleaner("filetoread.txt")