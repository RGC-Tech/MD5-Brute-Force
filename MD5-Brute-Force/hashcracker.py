if __name__ == "__main__":
    def md5bruteforce(hashtextfile, dictionarytextfile):
        import hashlib
        if ".txt" in hashtextfile and ".txt" in dictionarytextfile:
            #Subroutine which returns the key
            def workout(diction, items, encoded):
                for key, value in diction.items():
                    if value == items:
                        return key


            #Declaring the lists which are going to be used
            dictionary = []
            hashes = []
            encoded = []
            curly_dictionary = {}
            correct_values = {}
            #Opening the hashes and the common passwords list
            dictionary_txt = open(dictionarytextfile,"r")
            hashes_txt = open(hashtextfile,"r")

            #Removing \n in the dictionary list
            dictionary_lines = dictionary_txt.readlines()
            dictionary = [password.replace("\n","") for password in dictionary_lines]

            #Removing \n in the hashes list
            hashes_lines = hashes_txt.readlines()
            hashes = [_hash.replace("\n","") for _hash in hashes_lines]

            #For loop that encodes each string from the password list
            for password in dictionary:
                encoded_password = hashlib.md5(password.encode())
                encoded.append(encoded_password.hexdigest())

            #Converting the list into a dictionary
            curly_dictionary = dict(zip(dictionary, encoded))

            #Checking if the dictionary passwords is in the hashes

            for items in hashes:
                if items in encoded:
                    correct_values[workout(curly_dictionary, items, encoded)] = items
            return correct_values
        else:
            logger.error("These files are not '.txt' You have supplied the following files",hashtextfile,dictionarytextfile)
            


