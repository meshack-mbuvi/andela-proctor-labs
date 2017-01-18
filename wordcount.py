def words(string):
    """
    :Author: Mbuvi
    :http://mbuv.wordpress.com
    :Email: meshmbuvi@gmail.com
    :Argument: string
    :Return : dictionary

    This is a function that counts the frequency(number of occurrence) of
    words in a given sentence
    """
    new_list=[] #List to hold words in the sentence 
    string_dict={}#dictionary to hold the words and thier frequencies
    
    if type(string)==type(str()):
        #split the argument if it is a string
        new_list=string.split()
    elif type(string)==type(dict()):
        #Get the keys for words if the argument is a dictionary
        new_list=string.keys()
    elif type(string)==type([]):
        #Use the argument the way it is if it is a list
        new_list=string
        """
        Count the words now
        """
    for word in new_list:
        if word in string_dict:
            string_dict[word]+=1
        else:
            string_dict[word]=1
    return string_dict
    
            
print words("hellow hellow mesh 20")
print words("hellow")
print words({'Two':2,'of':1,'each':1})
print words(['a','b','c'])
