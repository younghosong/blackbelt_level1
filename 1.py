import datetime
def even_print(even_numbers,cnt):
   st=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th']
   for i in even_numbers.keys():
      print("%s result ---->    "%st[cnt],end="   ")
      for even_result in even_numbers[i].split(","):
         if int(even_result)%2==0:
            print(even_result,end=" ")
      cnt+=1
      print("\n================================")

def main():
   print(datetime.datetime.now())
   cnt=0
   numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
   for i in range(0,len(numbers)):
      even_print(numbers[i],cnt)
      cnt+=1

if __name__=="__main__":
   main()


