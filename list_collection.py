1. append() 追加对象至列表最后，每次追加一个对象，否则报错

list = ["alex","seven","eric"]
list.append(123)
print(list)
['alex', 'seven', 'eric', 123]


* 2. insert() 在指定的索引号，插入指定元素

list = ["alex","seven","eric"]
list.insert(1,"abc")
print(list)
['alex', 'abc', 'seven', 'eric']


* 3. del 删除列表中的元素，支持切片

list = ["abc","alex","seven","eric"]
del list[0]
print(list)
del list[0:1]
print(list)
['alex', 'seven', 'eric']
['seven', 'eric']


** 4. pop() 弹出元素并返回元素本身，可将返回值赋值给其他变量

4.1 pop(INT) 弹出指定索引位置的元素并返回元素

list = ["alex","seven","eric"]
pop = list.pop(0)
print(list,"\n",pop)
['seven', 'eric'] 
 alex


4.2 pop() 当未指定索引时，默认弹出最后一个元素并返回元素

list = ["alex","seven","eric"]
pop = list.pop()
print(list,"\n",pop)
['alex', 'seven'] 
 eric


** 5. remove() 删除列表中的元素，如有重复元素，有限删除靠左边的

list = ["abc","alex","abc","seven","abc","eric"]
list.remove("abc")
print(list)
list.remove("abc")
print(list)
['alex', 'abc', 'seven', 'abc', 'eric']
['alex', 'seven', 'abc', 'eric']


* 6. index() 输出指定元素的索引号，从0开始

list = ["alex","seven","eric"]
v = list.index("eric")
print(v)


* 7. extend() 遍历指定的元素，并将指定的单个元素以迭代的形式追加至列表中，仅支持一个元素，否则报错

7.1 指定元素为字符串时

list = ["abc","alex","abc","seven","abc","eric"]
list.extend("不得了")
print(list)
['abc', 'alex', 'abc', 'seven', 'abc', 'eric', '不', '得', '了']


7.2 指定元素为列表或元祖时

list = ["abc","alex","seven","eric"]
list.extend([11,22])
print(list)
list.extend(("abc",45))
print(list)
['abc', 'alex', 'seven', 'eric', 11, 22]
['abc', 'alex', 'seven', 'eric', 11, 22, 'abc', 45]


7.3 指定元素为字典时

list = ["abc","alex","seven","eric"]
list.extend({"name":"alex","age":12})
print(list)
['abc', 'alex', 'seven', 'eric', 'name', 'age']


7.4 注意 当列表、元祖或字典中套用了列表、元祖或字典时，extend() 仅遍历并迭代追加一级元素

list = ["abc","alex","seven","eric"]
list.extend(["xyz",["opq",123],{"vuw":789}])
print(list)
['abc', 'alex', 'seven', 'eric', 'xyz', ['opq', 123], {'vuw': 789}]


8. in 判断包含关系

list = ["abc","alex","seven","eric"]
v = "alex" in list
print(v)
True


9. count() 统计列表内指定元素的数量

list = ["abc","def","abc","ghi"]
test = list.count("abc")
print(test)


10. clear() 清空列表

list = ["abc","def","abc","ghi"]
list.clear()
print(list)
[]
list.append(13)
print(list)
[13]


11. copy() 浅复制

list = ["alex","seven","eric"]
list1 = list.copy()
print(list1)
['alex', 'seven', 'eric']


12. reverse() 将列表的索引号反转

list = ["abc","alex","abc","seven","abc","eric"]
list.reverse()
print(list)
['eric', 'abc', 'seven', 'abc', 'alex', 'abc']


13. sort() 如果列表中的所有元素支持排序，则进行排序，否则报错

list = ["abc","alex","abc","seven","abc","eric"]
list.sort()
print(list)
list = [110,22,0,55,33,120,44]
list.sort()
print(list)
['abc', 'abc', 'abc', 'alex', 'eric', 'seven']
[0, 22, 33, 44, 55, 110, 120]


14. 多级嵌套时取值

list = ['abc', 'alex', 'seven', 'eric', 'xyz', ['opq', 123], {'vuw': 789}]
#取出123
v = list[5][1]
print(v)
123

list = ['abc', 'alex', 'seven', 'eric', 'xyz', ['opq', 123], {'vuw': 789}]
# 取出789
v = list[6].values()
print(v)
dict_values([789])