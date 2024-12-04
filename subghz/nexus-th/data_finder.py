import sys, getopt
import re

inputfile=''

# va nous servir pour avoir le rendu lisible des données
def raw_data_to_human_readable(nexus_packet):
	
	count_bit = 0
	result = ''
	temp_result = ''
	for one_bit in nexus_packet:
		# print(one_bit)
		temp_result += one_bit
		count_bit += 1	
		match count_bit:
			case 8:				
				result += 'ID: ' + str(int(temp_result,2))
				temp_result = ''
				
			case 9:
				result += ' - Battery: ' + str(int(temp_result,2))
				temp_result = ''
			# toujours à 0
			case 10:
				temp_result = ''
			
			case 12:
				result += ' - Channel: ' + str(int(temp_result,2))
				temp_result = ''
			case 24:
				#la température est mise à l'échelle par 10 est en celcius
				result += ' - Temperature: ' + str(int(temp_result,2) / 10)
				temp_result = ''
			#toujour quatre 1
			case 28:
				temp_result = ''
			case 36:
				result += ' - Humidity: ' + str(int(temp_result,2))
				temp_result = ''
	
	print(result)


def main(argv):
   global inputfile
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('data_finder.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('data_finder.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
   
if __name__ == "__main__":
   main(sys.argv[1:])
   
   
   content_file = ''
   
   count_line = 0
   
   with open(inputfile, "r") as fichier:
     for line in fichier:
      if count_line > 4:
       content_file += re.sub('RAW_Data: ','',line)
       
      else:
       count_line += 1
	
   
   content_file = re.sub(r'( -\d+ )',r'\1\n', content_file)
   
   f = open("temp.txt", "w")
   f.write(content_file)
   f.close()   
   
   list_of_nexus_th_data = []
   
   
   count_bit = 0
   ready_to_nexus_packet = False
   current_packet_nexus = []
   
   with open('temp.txt', "r") as fichier:
    for line in fichier:
      line = line.split(' ')
      nexus_time = int(line[1])
	  
	  # on cherche le début du packet de nexus TH
      if int(nexus_time) < -3500 and int(nexus_time) > -4200: 
          #print(line[1])
       ready_to_nexus_packet = True
      elif ready_to_nexus_packet == True and count_bit < 36:
       if nexus_time < -1900:
        current_packet_nexus.append("1")
       else:
        current_packet_nexus.append("0")
       count_bit += 1
      elif count_bit == 36:
       raw_data_to_human_readable(current_packet_nexus)
       list_of_nexus_th_data.append( current_packet_nexus )
       count_bit = 0
       ready_to_nexus_packet = False
	   