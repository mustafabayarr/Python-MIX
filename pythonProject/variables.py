yaz = "Karabük Üniversitesi"
print(yaz)
print(yaz[3:7]) #abük

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
print(list)

matrix = [('Ali','Veli','Mehmet'),(25,20,30)] #tuple variables
matrix2 = [['Ali','Veli','Mehmet'],[25,20,30]] #list variables
print(matrix[0][2])
print(matrix2[0][0])
print(matrix2[1][:])

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  ) #read-only
print(tuple)

dict = {'name': 'john','code':6734, 'dept': 'sales'} #ilk değişkenler key leri oluyor. yazdırmak istediğimizde key lerle çağırıyoruz.
print(dict['name']) #john

dict2 = {'person':{'name': 'john','code':6734, 'dept': 'sales'}}
print(dict2['person']['name'])#john


