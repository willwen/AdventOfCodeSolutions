f = open('input.txt', 'r')
lines = f.readlines();
count = 0
errorLine = "";
try:
    for line in lines:
        errorLine = line;
        #print(line.split())
        #print(line.strip().split("  "))
        #for number in line:
            #print(number)
            #print(number.strip())
        numbers = [int(number) for number in line.split()]
        #pick the two lower numbers
        #numbers.sort()
        #numbers 0 and numbers 1 must be greater than numbers 2 to be a valid triangle
        if (numbers[0] + numbers[1] <= numbers[2]):
            continue
        elif (numbers[1] + numbers[2] <= numbers[0]):
            continue
        elif (numbers[0] + numbers[2] <= numbers[1]):
            continue
        else:
            count+=1

        
    print(count);
except:
    print(line)
    raise
