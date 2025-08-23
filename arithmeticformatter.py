def arithmetic_arranger(problems,show=False):
    if len(problems)>5:
        return 'Error: Too many problems.'
    string=""
    firstline=""
    secondline=""
    thirdline=""
    fourline=""
    for x in problems:
        string=string+x+" "
    parts=string.split()
    #check operator
    for operator in range(1,len(parts),3):
        if parts[operator]!='+' and parts[operator]!='-':
            return "Error: Operator must be '+' or '-'."
    #check numbers
    for i in range(0,len(parts),3):
        if len(parts[i])>4 or len(parts[i+2])>4:
            return 'Error: Numbers cannot be more than four digits.'
        if not parts[i].isdigit() or not parts[i+2].isdigit():
            return 'Error: Numbers must only contain digits.'

        maxn=max(len(parts[i]),len(parts[i+2]))
        help=str(parts[i]).rjust(maxn+2)
        if parts[i+1]=="+":
            score=int(parts[i])+int(parts[i+2])
            fourline=fourline+str(score).rjust(maxn+2)+"    "
        else:
            score = int(parts[i]) - int(parts[i + 2])
            fourline = fourline + str(score).rjust(maxn + 2) + "    "
        firstline=firstline+help+"    "
        help=str(parts[i+1])+str(parts[i+2]).rjust(maxn+1)
        secondline=secondline+help+"    "
        thirdline=thirdline+'-'*(maxn+2)+"    "
    firstline=firstline[:-4]
    secondline = secondline[:-4]
    thirdline = thirdline[:-4]
    fourline=fourline[:-4]

    result=firstline+'\n'+secondline+'\n'+thirdline
    if show==True:
        result=result+'\n'+fourline
    return result



if __name__ == '__main__':
    result=arithmetic_arranger(["1 + 2", "1 - 9380"])
    print(result)
