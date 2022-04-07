from typing import List

x: List[str] = []

# update x
#x[0] = "Long"

name: List[str] = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name[0:2]) #se khong in ra vi tri 2

#update  pahn tu 
name[2] = 1996
name[len(name) - 2] = "them vao vi tri chua biet"
print(name)

#them phan tu vao cuoi list
name.append("D")
print(name)

#xoa di phan tu thu 2 trong danh sach 
del name[1]
print(name)

# them phan tu
mylist = ["A", "B", "C"]
mylist.extend(["D", "E"])

print(mylist)
#>> ["A", "B", "C", "D", "E"]

