from List_Class import ListObject
def main():
    list_obj = ListObject('1,2,3,4', ',')
    print (list_obj.getListObj())
    
    print (list_obj.getLastElem())
    
    print (list_obj.reverseListFunc())
    
if __name__ == "__main__":
    main()