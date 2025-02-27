## 学习心得

### 浅拷贝与深拷贝

1. 对象

   首先，针对的是可变对象(list, set)，而对于不可变对象不存在对应的问题，对于不可变对象，不存在对应的问题，如：

   ```python
   a = 1
   b = a
   b += 1
   print(b) # 2
   print(a) # 1
   ```

   这也可以解释在创建一维列表中为什么可以直接使用

   ```python
   alist = [0]*5 # 将整数(int)重复5次，是5个不同的对象
   ```

2. 操作

   对于可变对象，浅拷贝保存的是对对象的引用，所以操作的是同一个对象

   ```python
   a = [1]
   b = a
   b.append(2)
   print(b) #[1, 2]
   print(a) #[1, 2]
   ```

3. 直观展示

   ![image-20250224153217414](https://raw.githubusercontent.com/stur007/img/main/img/202502241542761.png)

   在操作过程中，我们只是给他起了一个“别名”，操作的是同一对象。

4. 典型例子

   ```python
   maze = [[0]*m for _ in range(n)] #对外面一层列表注意深浅拷贝
   ```

   ### 正则表达式 (regex expression)
   
   ```python
   import re
   re.split(r' ')
   re.match(r' ')
   ```
   
   
