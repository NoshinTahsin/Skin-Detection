from PIL import Image

pixArrSkin = [[ [ 0 for col in range(256)] for col in range(256)] for row in range(256)]
pixArrNonSkin = [[ [ 0 for col in range(256)] for col in range(256)] for row in range(256)]
pixArrRatio = [[ [ 0.0 for col in range(256)] for col in range(256)] for row in range(256)]

def getRatio():
    r=0
    g=0
    b=0
    f = open("skinDataset.txt", "r+")
    wholeFile = f.readlines()
    for line in wholeFile:
        line = line.split()
        r = int(line[0])
        #print("r")
        #print(r)
        g = int(line[1])
        #print("g")
        #print(g)
        b = int(line[2])
        #print("b")
        #print(b)
        if line[3]=='2':
            pixArrNonSkin[r][g][b]+=1
            #print(pixArrNonSkin[r][g][b])
        else:
            pixArrSkin[r][g][b]+=1
            #print(pixArrSkin[r][g][b])

    fratio = open('ratio.txt', 'w+')

    for i in range (0,256):
        for j in range (0,256):
            for k in range (0,256):
                if pixArrNonSkin[i][j][k]!=0:
                    pixArrRatio[i][j][k]=float(pixArrSkin[i][j][k]/pixArrNonSkin[i][j][k])
                    #print(i)
                    #print(j)
                    #print(k)
                elif pixArrNonSkin[i][j][k]==0 and pixArrSkin[i][j][k]==0:
                    pixArrRatio[i][j][k]=0.0
                else:
                    pixArrRatio[i][j][k]=.89

                #print(pixArrRatio[i][j][k])
                fratio.write(str(i)+ " "+ str(j)+ " "+ str(k)+ " "+ str(pixArrRatio[i][j][k])+ "\n")
                #print(str(i)+ " "+ str(j)+ " "+ str(k)+ " "+ str(pixArrRatio[i][j][k])+ "\n")


    return

def convertIntoMask():
    inputImage = Image.open("moyda.jpg")
    newMask = inputImage.load()
    width, height = inputImage.size
    for x in range(width):
        for y in range(height):
            rgb=newMask[x,y]
            #print("p")
            #print(p)
            if pixArrRatio[rgb[0]-1][rgb[1]-1][rgb[2]-1]<=0.30:
                newMask[x,y] = (255, 255, 255)

    inputImage.save("newmask.bmp", "BMP")
    return





def main():
    getRatio()
    convertIntoMask()


if __name__=='__main__':
    main()
