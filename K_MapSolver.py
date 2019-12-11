#Name     : Mohnish Agrawal
#Roll nos : 2018053
#Section  : A
#Group no.: 5
#Date     : 15th October 2018 

import copy

#a function of maximum 4 variables as input and gives the corresponding minimized function(s) as the output.
def minFunc(numVar, stringIn):
	if(stringIn[stringIn.find("d")+1:stringIn.find("d")+2]==" "):
		stringIn=stringIn[:stringIn.find("d")+1]+stringIn[stringIn.find("d")+2:]
	dont_care=0
	string1=stringIn[1:stringIn.find('d')-2]
	string2=stringIn[stringIn.find('d')+1:]
	if string2[-1]!='-':
		dont_care=string2[1:len(string2)-1]
		stringIn1=string1.split(",")+dont_care.split(",")
	else:
		stringIn1=string1.split(",")
	if(string1==""):
		return "0"
	sort_string=sorted(list(map(int,stringIn1)))
	stringIn1=list(map(str,sort_string))
	b=[]
	if(numVar==3):
		stro="0"
	elif(numVar==4):
		stro="00"
	elif(numVar==2):
		stro=""
	for i in range(len(stringIn1)):
		int1=int(stringIn1[i])
		str1=""
		if(int1==0):
			b.append("00"+stro)
		else: 
			while int1>0:
				d=int1%2
				str1=str(d)+str1
				int1//=2
			if(numVar==4):
				b.append(str("%04d"%int(str1)))
			elif(numVar==3):
				b.append(str("%03d"%int(str1)))
			elif(numVar==2):
				b.append(str("%02d"%int(str1)))
	for i in range(len(b)):
		c=int(b[i])
	

	min=minimize_terms(b)
	min2=minimize_terms(min)
	min4=minimize_terms(min2)
	min3=minimize_terms(min4)
	unique_min=[]
	for c in min3:
		if c not in unique_min:
			unique_min.append(c)
	sort2=chart(return_check_list(unique_min))
	string_without_dont_care2=string_without_dont_care(stringIn)
	essen=essen_prime_imp(unique_min,string_without_dont_care2)
	essen3=[]
	for c in essen:
		if c not in essen3:
			essen3.append(c)
	final1=final_list(essen3,unique_min,sort2)
	final2=search_minterms_notcovered(final1,essen3,string_without_dont_care2)
	stringOut=convert(essen,final2,numVar)
	return stringOut

#matches the different minterm values in gray code form which are distanced from each other by 1  
def minimize_terms(b):
	
	cycle=0
	ind2=0
	essen_prime_imp=[]
	min_terms=[]
	for i in range(len(b)):
		a=b[i]
		d=0
		for j in range(i+1,len(b)):
			for c in range(len(a)):
				if a[c]!=b[j][c]:
					ind2=c
					cycle+=1
			if(cycle==1):
				min_terms.append(a[:ind2]+"-"+a[ind2+1:])
				d+=1
			cycle=0
		for k in range(i):
			for c in range(len(a)):
				if a[c]!=b[k][c]:
					ind2=c
					cycle+=1
			if(cycle==1):
				min_terms.append(a[:ind2]+"-"+a[ind2+1:])
				d+=1
			cycle=0

		if(d==0):
			min_terms.append(a)
	return min_terms

#return a string of minterms without don't care minterms
def string_without_dont_care(stringIn):
	return stringIn[1:stringIn.find("d")-2].split(",")

#To return a list of all prime implicants
def essen_prime_imp(prime_imp,mod_string):
	essen_prime_im=[]
	imp=return_check_list(prime_imp)
	for i in range(len(mod_string)):
		c=mod_string[i]
		value=0
		for i in range(len(imp)):
			if c==imp[i][imp[i].find(" ")+1:]:
				value+=1
				d=imp[i]
		if(value==1):
			essen_prime_im.append(d)
	for c in range(len(essen_prime_im)):
		for d in range(len(chart(imp))):
			if essen_prime_im[c][:essen_prime_im[c].find(" ")]==chart(imp)[d][:essen_prime_im[c].find(" ")]:
				essen_prime_im[c]=chart(imp)[d]
	return essen_prime_im

#To replace a particular character with another at a particular index
def repl_str_ind(str1,index,replace):
	return (str1[:index]+replace+str1[index+1:])

#A function which helps return_check_list function
def returns_CheckList_for_2(val2,im,a,check_list):
	for i in range(2):
		val2=0
		b=a.replace("-",str(i))
		for j in range(len(b)):
			val2+=2**(len(b)-1-j)*int(b[j])
		check_list.append(im+" "+str(val2))
	val2=0
	c=repl_str_ind(a,a.find("-"),"0")
	b=repl_str_ind(c,c.find("-"),"1")
	for j in range(len(b)):
		val2+=2**(len(b)-1-j)*int(b[j])
	check_list.append(im+" "+str(val2))
	val2=0
	c=repl_str_ind(a,a.find("-"),"1")
	b=repl_str_ind(c,c.find("-"),"0")
	for j in range(len(b)):
		val2+=2**(len(b)-1-j)*int(b[j])
	check_list.append(im+" "+str(val2))

#Returns a list of strings, showing how many decimal values can a particular boolean value represent
def return_check_list(prime_imp):
	check_list=[]
	for i in range(len(prime_imp)):
		a=prime_imp[i]
		im=prime_imp[i]
		if(a.count("-")==0):
			val2=0
			for j in range(len(a)):
				val2+=2**(len(a)-1-j)*int(a[j])
			check_list.append(im+" "+str(val2))
		if(a.count("-")==1):
			for i in range(2):
				val2=0
				b=a.replace("-",str(i))
				for j in range(len(b)):
					val2+=2**(len(b)-1-j)*int(b[j])
				check_list.append(im+" "+str(val2))
		if(a.count("-")==2):
			val2=0
			returns_CheckList_for_2(val2,im,a,check_list)
		if(a.count("-")==3):
			val2=0
			for i in range(2):
				d=a.replace("-",str(i),1)
				returns_CheckList_for_2(val2,im,d,check_list)
		if(a.count("-")==4):
			for k in range(2):
				l=a.replace("-",str(k),1)
				val2=0
				for i in range(2):
					d=l.replace("-",str(i),1)
					returns_CheckList_for_2(val2,im,d,check_list)
	return check_list

#matches the values of different minterms to its prime implicant
def chart(check_list):
	final_list=[]
	for i in range(len(check_list)):
		c=check_list[i]
		d=c.find(" ")
		c=c[:c.find(" ")]
		nos=""
		for j in range(len(check_list)):
			if(c==check_list[j][:d]):
				nos=nos+check_list[j][d+1:]+","
		if(nos[-1]==","):
			nos=repl_str_ind(nos,len(nos)-1,"")
		final_list.append(c+" "+nos)
	sort3=[]
	sort3.append(final_list[0])
	for i in range(len(final_list)):
		if final_list[i] not in sort3:
			sort3.append(final_list[i])
	final_list=sort3
	return final_list

#returns a list of prime implicants which excludes the essential prime implicants
def final_list(essen_prime_im,unique_min,chart):
	final_chart=[]
	for i in range(len(essen_prime_im)):
		if(len(unique_min)>0):
			c=essen_prime_im[i]
			c=c[:c.find(" ")]
			unique_min.remove(c)
		else:
			break

	for i in range(len(chart)):
		d=chart[i]
		for j in range(len(unique_min)):
			if d[:d.find(" ")] in unique_min[j]:
				final_chart.append(d)
	return final_chart

#returns a list of prime implicants which cover the minterms that are not covered by the essential prime implicant
def search_minterms_notcovered(final_list,essen,string_without_dont_care):
	essen2=[]
	value=0
	for j in range(len(final_list)):
		minterms=final_list[j]
		minterms=minterms[minterms.find(" ")+1:].split(",")
		for i in range(len(minterms)):
			minterms[i]=int(minterms[i])
		for k in range(len(minterms)):
			if str(minterms[k]) in string_without_dont_care:
				for l in range(len(essen)):
					if str(minterms[k]) not in essen[l][essen[l].find(" ")+1:].split(","):
						value+=1
				if value==len(essen):
					essen2.append(final_list[j][:4]+" "+str(minterms[k]))
				value=0
	unique_min=[]
	for c in range(len(essen2)):
		str2=essen2[c]
		val=str2.find(" ")
		str2=str2[:val]
		for t in range(c+1,len(essen2)):
			if str2==essen2[t][:val]:
				unique_min.append(essen2[c]+","+essen2[t][val+1:])
			else:
				unique_min.append(essen2[c])
		for t2 in range(0,c):
			if str2==essen2[t2][:val]:
				unique_min.append(essen2[c]+","+essen2[t2][val+1:])
			else:
				unique_min.append(essen2[c])
	unique_min2=[]
	for c in unique_min:
		if c not in unique_min2:
			unique_min2.append(c)
	unique_min3=copy.deepcopy(unique_min2)
	for q in range(len(unique_min2)):
		ind=unique_min2[q]
		ind=ind.find(" ")
		str3=list(map(int,unique_min2[q][ind+1:].split(",")))
		for i in range(q+1,len(unique_min2)):
			str4=list(map(int,unique_min2[i][ind+1:].split(",")))
			val=0
			for j in str3:
				if j in str4:
					val+=1
			if(val==len(str3) and len(str3)==len(str4) and unique_min2[q][:ind]!=unique_min2[i][:ind]):
				if(unique_min2[q][:ind].count("-")>unique_min2[i][:ind].count("-")):
					unique_min3.remove(unique_min2[i])
				else:
					unique_min3.remove(unique_min2[q])
				break
			if(val==len(str3)):
				unique_min3.remove(unique_min2[q])
				break
	unique_min4=copy.deepcopy(unique_min3)
	for q in range(len(unique_min3)):
		ind=unique_min3[q]
		ind=ind.find(" ")
		str3=list(map(int,unique_min3[q][ind+1:].split(",")))
		val=0
		index=unique_min4.index(unique_min3[q])
		for j in range(len(str3)):
			val2=0
			for i in range(q+1,len(unique_min3)):
				str4=list(map(int,unique_min3[i][ind+1:].split(",")))
				if str3[j] in str4:
					val+=1
					val2+=1
					break
			for k in range(index):
				str4=list(map(int,unique_min4[k][ind+1:].split(",")))
				if str3[j] in str4:
					val+=1
					break
		if val==len(str3):
			unique_min4.remove(unique_min3[q])
	return unique_min4
	
#converts the final implicants list into corresponding variables
def convert(essen,nonessen_prime_im,numVar):
	str1=""
	for i in range(len(essen)):
		alp=essen[i][:essen[i].find(" ")]
		str2=""
		for j in range(len(alp)):
			if(alp[j]=="1"):
				str2+=chr(119+j)
			if(alp[j]=="0"):
				str2+=chr(119+j)+"'"
		if(str2==""):
			str2="1"
		str1+=str2+"+"
	for i in range(len(nonessen_prime_im)):
		alp=nonessen_prime_im[i][:nonessen_prime_im[i].find(" ")]
		str2=""
		for j in range(len(alp)):
			if(alp[j]=="1"):
				str2+=chr(119+j)
			if(alp[j]=="0"):
				str2+=chr(119+j)+"'"
		if(str2==""):
			str2="1"
		str1+=str2+"+"
	str1=str1[:len(str1)-1]

	str1=str1.split("+")
	str3=[]
	for c in str1:
		if c not in str3:
			str3.append(c)
	str3=sorted(str3)
	str1="+".join(str3)
	return str1

kmap = int(input())
number1 = tuple(map(int,input().split()))
if(len(number1) == 1):
	number1 = "("+str(number1[0])+")"
if(len(number1) == 0):
	number1 = "()"
print("If dont care present, enter dont care values with space in between, else enter no")
dontCare = input()
if(dontCare.lower() == "no"):
	dontCare = "-"
else:
	dontCare = tuple(map(int,dontCare.split()))
	if(len(dontCare) == 1):
		dontCare = "("+str(dontCare[0])+")"
	elif(len(dontCare) == 0):
		dontCare = "-"
inputString = str(number1)+" d "+str(dontCare)
print(inputString)
print(minFunc(kmap,inputString))