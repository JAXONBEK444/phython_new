# wedwed

def new_recurtion(a):
    if(a>0):
        natija = a + new_recurtion(a-5)
        print(natija)
    else:
        natija = 0
    return natija

print("\n\n natija kuring" )
new_recurtion(50)
    

# a(50) = 50 - 5 =45                //225 + 50 =275
# a(45) = 45 - 5 = 40              // 180 + 45 = 225
# a(40) = 40 - 5 = 35            // 140 + 40 = 180
# a(35) = 35 - 5 = 30           // 105 + 35 = 140
# a(30) = 30 - 5 = 25           // 75 + 30 = 105
# a(25) = 25 - 5 = 20           // 50 + 25 = 75
# a(20) = 20 - 5 = 15          // 30 + 20 = 50
# a(15) = 15 - 5 = 10         // 15 + 15 = 30 
# a(10) = 10 - 5 = 5         // 10 + 5 = 15 
# a(5) = 5                  //5        