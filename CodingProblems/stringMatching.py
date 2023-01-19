

def stringMatching(pattern, string):
    
    lp = len(pattern)
    ls = len(string)

    ip = 0
    ist = 0

    while ip < lp and ist < ls:

        elem = ""
        stringCond = (97 <= ord(pattern[ip]) <= 122) or (65 <= ord(pattern[ip]) <= 90)
        intCond = 48 <= ord(pattern[ip]) <= 57

        if stringCond:
            while (ip < lp) and (97 <= ord(pattern[ip]) <= 122) or (65 <= ord(pattern[ip]) <= 90):
                      elem += pattern[ip]
                      ip += 1
                      
        elif intCond:
            while ip < lp and 48 <= ord(pattern[ip]) <= 57:
                     elem += pattern[ip]
                     ip += 1
              
        print(elem, ip)
        
        if not elem.isnumeric():

              l = len(elem)
              if elem == string[ist:ist+l]:
                  ist += l
              else:
                  return False
                  
        else:
            
              if int(elem) <= ls - ist :
                  ist += int(elem)
              else:
                  return False
                

    if ip==lp:
        return True
    elif ip < lp and ist==ls:
        return False

string = "internationalization"
pattern = "i18n"

output = stringMatching(pattern, string)
print(output)



        
