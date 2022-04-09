from typing import Dict

x: Dict[str, str] = {"Last Name":"Tran","First Name": "Long","Address" : "Quang Nam"}

print(x)
# Cập nhập giá trị cho khóa (key) 'Address'
x["Address"] = "HCM Vietnam"
print(x)

# Xóa một phần tử ứng với khóa 'John'
del x["Address"] 

print(x)