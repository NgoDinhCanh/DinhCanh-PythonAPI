#Unique: Check xem item in string có phải là all unique character
str = 'abcd'
def unique(str):
    
    char_set={}
    
    for char in str:
        # print(char)
        if char in char_set:
            return False
        char_set[char] = True
    return True

def main():
    print(unique(str))
if __name__=='__main__':main()
