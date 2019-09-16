FileWrite = open('newfile.txt','w')
FileInput = open('qbdata.txt','r')

for i in FileInput.readlines():
    i = i.strip('\n') 
    count1 = 0
    name = ''
    score = ''
    
    for j in i[::-1]:
        if j == ' ':
            break
        score += j

    if int(score[-1:]) >= 6 or len(score)>=5:
        for l in i:
            if l == ' ' :
                count1 += 1
            elif count1 == 2:
                break
            name += l
        FileWrite.write(name)
        FileWrite.write(score[::-1])
        FileWrite.write('\n')

FileWrite.close()
FileInput.close()
        
