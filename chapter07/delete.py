#python中垃圾回收算法是采用　引用计数
a = 1
b = a
del a #并没有将a回收，减为0才回收