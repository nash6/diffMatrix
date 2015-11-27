#diffMatrix.py
#for 6000 written by lyc 2015.7
#mod by lyc 2015.9
import sys
#print 'lyc&6000'



def main(argv):

	filename = 'output.txt'
	with open(filename, 'r') as f:
		tfile = f.readlines()


	vector = []
	for i,line in enumerate(tfile):
		tlist = line[1:-2].strip().split(', ')
		#print i, list
		vector.append(tlist)
	
	
	

	with open('data.txt', 'r') as f:
		tfile2 = f.readline()
	
	tlist = tfile2.strip().split('\t')	
	#tlist = tlist[1:-1]

	
	


	result = []
	result.append(['No.', 'Sum', 'Result'])
	for i, line in enumerate(vector):
		tmp = []
		tmp.append(i + 1)
		for j, cube in enumerate(line):
			if j == 0:
				tmp.append(cube)
				#f.write("%s\t" % cube)
			else:
				if cube != '0':
					tmp.append(tlist[j])
					#f.write("%s " % tlist[j])
		result.append(tmp)
		#f.write("\n")
	#print result

	f = open("Newoutput.txt",'w')
	
	for head in result[0]:
		f.write("%s\t" % head)
	print >> f 
	for each in result[1:]:
		for index, item in enumerate(each):
			if index in (0, 1):
				f.write("%s\t" % item)
			else:
				f.write("%s " % item)
		f.write("\n")
	f.close()

if __name__ == '__main__':
    main(sys.argv)

