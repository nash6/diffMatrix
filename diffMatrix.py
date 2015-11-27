#diffMatrix.py
#for 6000 written by lyc 2015.7
#mod by lyc 2015.9
import sys
#print 'lyc&6000'

def openFile(filename):
	with open(filename, 'r') as f:
		file = f.readlines()
	vector = []
	for i,line in enumerate(file):
		list = line.strip().split('\t')
		#print i, list
		vector.append(list)
	return vector;

def genDiffMatrixByRow(vector):
	n = len(vector)
	if n <= 0:
		return 'vector is invalid'

	#init Matrix
	m = len(vector[0])
	
	diffMatrix = []
	print diffMatrix
	#travel
	for i in range(1,len(vector)-1):
		iline = []
		for j in range(i+1,len(vector)):
			
			s = set()
			if vector[i][:-1] == vector[j][:-1]:
				iline.append(s)
			else:
				for k in range(1, m-1):
					if vector[i][k] != vector[j][k]:
						s.add(vector[0][k])
				if len(s) == 0:
					print 'line',i ,'and',j,'have no diff while D is NOT equal!'
					return -1
				else:
					iline.append(s)
		diffMatrix.append(iline)
	return diffMatrix

def genDiffMatrix(vector):
	n = len(vector)
	if n <= 0:
		return 'vector is invalid'

	#init Matrix
	m = len(vector[0])
	
	diffMatrix = []
	#travel
	#print 'travel start'
	for i in range(1,len(vector)-1):
		for j in range(i+1,len(vector)):
			s = set()
			#print vector[0][-1]
			if vector[i][-1] == vector[j][-1]:
				#print i,j
				diffMatrix.append(s)
			else:
				#print 'else:',i,j
				for k in range(1, m-1):
					if vector[i][k] != vector[j][k]:
						s.add(vector[0][k])
				if len(s) == 0:
					print 'line',i ,'and',j,'have no diff while D is NOT equal!'
					return -1
				else:
					diffMatrix.append(s)
	#print 'travel over'
	return diffMatrix


def decare(diffMatrix):
	diffMatrix = list(diffMatrix)

	l = [x for x in diffMatrix if len(x) != 0]
	
	tmp = 1
	for each in l:
		tmp *= len(each)

	print 'fucking:',tmp

	from itertools import product
	return product(*l)

def simply(multi):
	print 'simply start'
	result = []
	i = 0
	for each in multi:
		#print i
		#i+= 1

		tmp = (set(each))		
		if tmp not in result:
			result.append(tmp)

	print 'simplt over'
	return result


def subSet(multi):
	for iindex, i in enumerate(multi):
		for jindex, j in enumerate(multi):
			if iindex == jindex:
				break
			if i.issubset(j):
				del multi[jindex]
			elif j.issubset(i):
				del multi[iindex]
	
	return multi

def newDiffMatrix(vector):
	n = len(vector)
	if n <= 0:
		return 'vector is invalid'

	#init Matrix
	m = len(vector[0])

	diffMatrix = []


	for i in range(1,len(vector)-1):
		for j in range(i+1,len(vector)):
			if vector[i][-1] != vector[j][-1]:
				tmpLine = [0] * (m-1)
				flag = 0
				for k in range(1, m-1):
					if vector[i][k] != vector[j][k]:
						tmpLine[k] = 1
						flag += 1
				if flag == 0:
					print 'line',i ,'and',j,'have no diff while D is NOT equal!'
					return -1
				else:
					tmpLine[0] = flag
					diffMatrix.append(tmpLine)

	return diffMatrix

def isInclude(a,b):
	if a[0] < b[0]:
		return -1
	for i in range(len(a)):
		if a[i] == 0 and b[i] == 1:
			return -1;
	return 1
	
def newSimply(diffMatrix):

	diffMatrix.sort(lambda x,y:cmp(x[0],y[0]))


	i = 0;
	j = 1;
	while(i < len(diffMatrix)):
		j = i + 1
		while(j < len(diffMatrix)):
			if diffMatrix[i] == diffMatrix[j]:
				del diffMatrix[j]
			else:
				if isInclude(diffMatrix[j],diffMatrix[i]) == 1:
					del diffMatrix[j]			
				else:
					j += 1		
		i += 1
			


	return diffMatrix

def newGen(diffMatrix):
	result = []

	firstLine = diffMatrix[0]
	for iindex, i in enumerate(firstLine):
		if iindex == 0:
			continue
		if i == 1:
			tmpL = [0] * len(firstLine)
			tmpL[0] = 1
			tmpL[iindex] = 1
			result.append(tmpL)

	del diffMatrix[0]
	
	while(len(diffMatrix) > 0):
		
		tmpLine = diffMatrix[0]
		count = tmpLine[0]
		
		whereisone = []
		for iindex, i in enumerate(tmpLine):
			if iindex == 0:
				continue
			if i == 1:
				whereisone.append(iindex)


		tmpR = []
		for x in result:
			for i in whereisone:
				tmpx = list(x)
				if tmpx[i] == 0:
					tmpx[0] += 1				
				tmpx[i] = 1
				tmpR.append(tmpx)

		print len(diffMatrix)
		result = newSimply(tmpR)

		del diffMatrix[0]

	return result

def visual(v, r):
	tlist = v[0]

	result = []
	result.append(['No.', 'Sum', 'Result'])
	for i, line in enumerate(r):
		tmp = []
		tmp.append(i + 1)
		for j, cube in enumerate(line):
			if j == 0:
				tmp.append(cube)
				#f.write("%s\t" % cube)
			else:
				if cube != 0:
					tmp.append(tlist[j])
					#f.write("%s " % tlist[j])
		result.append(tmp)
		#f.write("\n")
	#print result
	return result

	

def print2file(result, path):
	f = open(path,'w')
	
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

def main(argv):
	arg = argv[1]
	#arg = 'data.txt'
	vector = openFile(arg)
	print 'Open file complete.'


	'''
	diffMatrix = genDiffMatrix(vector)
	print 'Diff Matrix Gen complete.'

	diffMatrix = subSet(diffMatrix)
	print 'before deac'
	#for each in diffMatrix:
	#	print each
	#deca = decare(diffMatrix)
	
	#simp = simply(deca)

	#multi = subSet(simp)
	multi = newSim(diffMatrix)
	multi = subSet(hehe)
	'''
	

	'''
	multi = [
	[1,0,1,0,0,0,0,0],
	[1,0,0,0,1,0,0,0],
	[2,0,0,1,0,0,1,0],
	[2,1,0,0,0,0,0,1],
	[2,0,0,0,0,0,1,1]
			]
	'''
	
	multi = newDiffMatrix(vector)

	multi = newSimply(multi)

	print 'Begin:'

	multi = newGen(multi)

	multi = newSimply(multi)
	print multi
	multi = visual(vector, multi)
	print multi
	print2file(multi, 'output.txt')
	print '============='
	print 'Done'
	
	'''
	file = open("output.txt",'w')
	for each in multi:
		file.write("%s\n" % each)
	
	file.close()
	'''


	
if __name__ == '__main__':
    main(sys.argv)

