#Write a Python program to display the examination schedule. (extract the date from exam start date: 11,12,2014).

#exam_starts = (11,12,2014)
#print( "The examination will start from : %i / %i / %i"%exam_starts)





#exam = (11,12,2014)
#d = exam[0]
#m = exam[1]
#y = exam[2]

#print("Exam date is : ",d,"/",m,"/",y,)

print('/'.join([str(x) for x in (11, 12, 2014)]))