1. append() ׷�Ӷ������б����ÿ��׷��һ�����󣬷��򱨴�

list = ["alex","seven","eric"]
list.append(123)
print(list)
['alex', 'seven', 'eric', 123]


* 2. insert() ��ָ���������ţ�����ָ��Ԫ��

list = ["alex","seven","eric"]
list.insert(1,"abc")
print(list)
['alex', 'abc', 'seven', 'eric']


* 3. del ɾ���б��е�Ԫ�أ�֧����Ƭ

list = ["abc","alex","seven","eric"]
del list[0]
print(list)
del list[0:1]
print(list)
['alex', 'seven', 'eric']
['seven', 'eric']


** 4. pop() ����Ԫ�ز�����Ԫ�ر����ɽ�����ֵ��ֵ����������

4.1 pop(INT) ����ָ������λ�õ�Ԫ�ز�����Ԫ��

list = ["alex","seven","eric"]
pop = list.pop(0)
print(list,"\n",pop)
['seven', 'eric'] 
 alex


4.2 pop() ��δָ������ʱ��Ĭ�ϵ������һ��Ԫ�ز�����Ԫ��

list = ["alex","seven","eric"]
pop = list.pop()
print(list,"\n",pop)
['alex', 'seven'] 
 eric


** 5. remove() ɾ���б��е�Ԫ�أ������ظ�Ԫ�أ�����ɾ������ߵ�

list = ["abc","alex","abc","seven","abc","eric"]
list.remove("abc")
print(list)
list.remove("abc")
print(list)
['alex', 'abc', 'seven', 'abc', 'eric']
['alex', 'seven', 'abc', 'eric']


* 6. index() ���ָ��Ԫ�ص������ţ���0��ʼ

list = ["alex","seven","eric"]
v = list.index("eric")
print(v)


* 7. extend() ����ָ����Ԫ�أ�����ָ���ĵ���Ԫ���Ե�������ʽ׷�����б��У���֧��һ��Ԫ�أ����򱨴�

7.1 ָ��Ԫ��Ϊ�ַ���ʱ

list = ["abc","alex","abc","seven","abc","eric"]
list.extend("������")
print(list)
['abc', 'alex', 'abc', 'seven', 'abc', 'eric', '��', '��', '��']


7.2 ָ��Ԫ��Ϊ�б��Ԫ��ʱ

list = ["abc","alex","seven","eric"]
list.extend([11,22])
print(list)
list.extend(("abc",45))
print(list)
['abc', 'alex', 'seven', 'eric', 11, 22]
['abc', 'alex', 'seven', 'eric', 11, 22, 'abc', 45]


7.3 ָ��Ԫ��Ϊ�ֵ�ʱ

list = ["abc","alex","seven","eric"]
list.extend({"name":"alex","age":12})
print(list)
['abc', 'alex', 'seven', 'eric', 'name', 'age']


7.4 ע�� ���б�Ԫ����ֵ����������б�Ԫ����ֵ�ʱ��extend() ������������׷��һ��Ԫ��

list = ["abc","alex","seven","eric"]
list.extend(["xyz",["opq",123],{"vuw":789}])
print(list)
['abc', 'alex', 'seven', 'eric', 'xyz', ['opq', 123], {'vuw': 789}]


8. in �жϰ�����ϵ

list = ["abc","alex","seven","eric"]
v = "alex" in list
print(v)
True


9. count() ͳ���б���ָ��Ԫ�ص�����

list = ["abc","def","abc","ghi"]
test = list.count("abc")
print(test)


10. clear() ����б�

list = ["abc","def","abc","ghi"]
list.clear()
print(list)
[]
list.append(13)
print(list)
[13]


11. copy() ǳ����

list = ["alex","seven","eric"]
list1 = list.copy()
print(list1)
['alex', 'seven', 'eric']


12. reverse() ���б�������ŷ�ת

list = ["abc","alex","abc","seven","abc","eric"]
list.reverse()
print(list)
['eric', 'abc', 'seven', 'abc', 'alex', 'abc']


13. sort() ����б��е�����Ԫ��֧��������������򣬷��򱨴�

list = ["abc","alex","abc","seven","abc","eric"]
list.sort()
print(list)
list = [110,22,0,55,33,120,44]
list.sort()
print(list)
['abc', 'abc', 'abc', 'alex', 'eric', 'seven']
[0, 22, 33, 44, 55, 110, 120]


14. �༶Ƕ��ʱȡֵ

list = ['abc', 'alex', 'seven', 'eric', 'xyz', ['opq', 123], {'vuw': 789}]
#ȡ��123
v = list[5][1]
print(v)
123

list = ['abc', 'alex', 'seven', 'eric', 'xyz', ['opq', 123], {'vuw': 789}]
# ȡ��789
v = list[6].values()
print(v)
dict_values([789])