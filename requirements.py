import sys
import fileinput


class requirement(object):
    """description of class"""

    global all_word,lbl_result
    all_word = {}
    lbl_result ={}
#--------------------------------------read txt ---------------------------------------

    def read_file(self):
        so = " "
        
        with open("F:\Project\dict\dict_file\dict.txt") as f:
            for line in f:
             if line != so :
                 (key, val) = line.rsplit(":")
                 all_word[key] = val
        f.close()

        return all_word

#--------------------------------------add enw word---------------------------------------
    def write_in_file(self,key,val):
        file = open("F:\Project\dict\dict_file\dict.txt","a")   
        i = 1
        for mainn_key in all_word :

            if (mainn_key == key) :
                file.close()

                i = 0

                return "can not add .file exist!!!!!!"
        if (i == 1):

            word ="\n" + key + ":" + val 

            file.write(word)

            file.close()

            return word
        
                

#--------------------------------------search---------------------------------------
    def search_in_file(self,search_key_func):

        go_val = all_word[search_key_func]
        return go_val 
#--------------------------------------Edit---------------------------------------
   
    def Update_file(self,u_key,v_key):

        node =""
        x = 1
        update_key = u_key
        update_val = v_key

        for main_key in all_word :

            if main_key == update_key :

                x = 0

                node = all_word[main_key]

                update_val = update_val+"\n"
   
                all_word[main_key]  = update_val

                # replace all occurrences of 'sit' with 'SIT' and insert a line after the 5th
                for i, line in enumerate(fileinput.input('F:\Project\dict\dict_file\dict.txt', inplace=1)):
                    sys.stdout.write(line.replace(node, update_val))  # replace 'sit' and write                 

        if x == 1 :
            updated = "your word mean do not updated"
            return updated

