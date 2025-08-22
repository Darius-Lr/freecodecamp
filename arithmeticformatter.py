def arithmetic_arranger(problems,show=False):
    if len(problems)>5:
        return 'Error: Too many problems.'
    string=""
    firstline=""
    secondline=""
    thirdline=""

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
        firstline=firstline+help+"    "
        help=str(parts[i+1])+str(parts[i+2]).rjust(maxn+1)
        secondline=secondline+help+"    "
        thirdline=thirdline+'-'*(maxn+2)+"    "
    result=firstline+'\n'+secondline+'\n'+thirdline
    return result



if __name__ == '__main__':
    result=arithmetic_arranger(["1 + 2", "1 - 9380"])
    print(result)
    print("  1         1\n+ 2    - 9380\n---    ------")