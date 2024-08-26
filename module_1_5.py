immutable_var = (1,'b','_',True)
#immutable_var[0] = 300 (нельзя изменить элемент в кортеже т.к кортеж не поддерживает обращение по элементам
#кортеж - используется в качестве хранилища, например, для какого-то списка, который мы ни коим образом не хотим трогать, то есть нам нужно чтобы он оставался неизменным.
print('Immutable tuple:',immutable_var)
print(type(immutable_var))
mutable_list = ([(1,'b','_',True)],2)*(2)
print('mutable_list:',mutable_list)
#mutable_list =
#mutable_list.remove (0)
mutable_list[0][0] =3
print('mutable_list:',mutable_list)
