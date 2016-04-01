import string
class Cezar():
    def __init__(self):
        self.ukr_lower=[]
        self.ukr_upper=[]
        self.eng_lower=[]
        self.eng_upper=[]
        for letter in range(256,10000):
            if 'а'<=chr(letter)<='я' :
                self.ukr_lower.append(chr(letter))
        self.ukr_lower.remove('э')
        self.ukr_lower.remove('ы')
        self.ukr_lower.remove('ъ')
        self.ukr_lower.insert(4,'ґ')
        self.ukr_lower.insert(10,'і')
        self.ukr_lower.insert(11,'ї')
        self.ukr_lower.insert(7,'є')

        for letter in self.ukr_lower:
            self.ukr_upper.append(letter.upper())
        
        for letter in range(0,256):
            if 'a'<=chr(letter)<='z' :
                self.eng_lower.append(chr(letter))

        for letter in self.eng_lower:
            self.eng_upper.append(letter.upper())

        self.str_ukr_lower = ''.join(self.ukr_lower)
        self.str_ukr_upper = ''.join(self.ukr_upper)
        self.str_eng_lower = ''.join(self.eng_lower)
        self.str_eng_upper = ''.join(self.eng_upper)
        

        
    def caesar(self, s, k, decode):
        k1 = k%len(self.str_ukr_lower)
        k2 = k%len(self.str_eng_lower)
        if decode:
            k1 = (len(self.str_ukr_lower) - k)%len(self.str_ukr_lower)
            k2 = (len(self.str_eng_lower) - k)%len(self.str_eng_lower)
        print( 'self.str_eng_lower[k2:]',self.str_eng_lower[k2:])
        print('self.str_eng_lower[:k2]',self.str_eng_lower[:k2])
        print(self.str_eng_lower[k2:] + self.str_eng_lower[:k2])
        return s.translate(
            str.maketrans(
                self.str_eng_lower + self.str_eng_upper + self.str_ukr_lower + self.str_ukr_upper,
                self.str_eng_lower[k2:] + self.str_eng_lower[:k2] +
                self.str_eng_upper[k2:] + self.str_eng_upper[:k2] +
                self.str_ukr_lower[k1:] + self.str_ukr_lower[:k1] +
                self.str_ukr_upper[k1:] + self.str_ukr_upper[:k1]
                )
            )
    
    def multicaesar(self, s):
        res=[]
        str_res=''
        for i in range(len(self.str_eng_lower + self.str_ukr_lower)):
            x=i+1
            if self.caesar(s, i, True) in res: continue
            else:
                res.append(self.caesar(s, i, True))
        x=0       
        for i in res:
            x+=1
            if x<10: str_res += "{0}. {1}      key = {2}      ".format(x, i, x-1)
            else: str_res += "{0}. {1}     key = {2}     ".format(x, i, x-1)
            if x%2==0: str_res+='\n'
        return str_res
    
def main():
    msg ='a'
    c=Cezar()
    print(c.caesar(msg,2,False))



if __name__ == '__main__':
    main()




##"{0}. {1} \n".format(x, 
##    msg ='АБCD'
##enc = caesar(msg, 2)
##print (enc)
##print (caesar(enc, 2, decode = True))
