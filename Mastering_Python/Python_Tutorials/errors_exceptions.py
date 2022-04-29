try: 
    f = open('simple.txt', 'r')
    f.write("Test Write to simple text!")
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")