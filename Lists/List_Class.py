class ListObject():
    def __init__(self, list_string, delimiter):
        self.list_string = list_string
        self.delimiter = delimiter
        self.__stringToList()
        
    def __stringToList(self):
        self.list_object = self.list_string.split(self.delimiter)
        if (len(self.list_object) == 1):
            exit("Please check your delimiter as it was not found in string")
        
    def getListObj(self):
        return self.list_object
    
    def getLastElem(self):
        return self.list_object[-1]
    
    def reverseListFunc(self):
        # reverse() function updates the list variable
        # assignment first would require making a copy as same memory
        # reverse() doesn't return the reversed list, its just an update
        reversed_list = self.list_object.copy()
        reversed_list.reverse()
        return reversed_list