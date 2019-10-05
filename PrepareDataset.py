from PIL import Image


def readPixel(opath,mpath):

    imMask = Image.open(opath)
    imOrigin=Image.open(mpath)

    rgb_imMask = imMask.convert('RGB')
    rgb_imOrigin = imOrigin.convert('RGB')

    width = rgb_imMask.size[0]
    height = rgb_imMask.size[1]

    row = 1
    col = 1
    pix = 0

    rowdata = ""
    test=235

    f= open("skinDataset.txt","w+")



    while row < height + 1:
        print("")
        print("Row number: " + str(row))
        while col < width + 1:
            r1, g1, b1 = rgb_imMask.getpixel((col - 1, row - 1))
            r2, g2, b2 = rgb_imOrigin.getpixel((col - 1, row - 1))

            if r1<=test and g1<=test and g2<=test :
            #1 for skin, 2 for non-skin
                rowdata += str(r1) + " " + str(g1) + " " + str(b1) + " "+str(1)
                #pixArrSkin[r1-1][g1-1][b1-1]=pixArrSkin[r1-1][g1-1][b1-1]+1

            else:
                rowdata += str(r2) + " " + str(g2) + " " + str(b2) + " "+str(2)
                #pixArrNonSkin[r2-1][g2-1][b2-1]=pixArrNonSkin[r2-1][g2-1][b2-1]+1

            f.write(rowdata+'\n')

            col = col + 1

            pix = pix + 1

            print(rowdata)

            rowdata = ""

        row = row + 1

        col = 1

    f.close()

    return

def main():

    for i in range(0, 555):
        serialNo = '{num:04d}'.format(num=i)
        mpath = "Mask/" + str(serialNo) + ".bmp"
        opath = "ibtd/" + str(serialNo) + ".jpg"

        readPixel(opath,mpath)

    #getRatio()
    #convertIntoMask()


if __name__=='__main__':
    main()
