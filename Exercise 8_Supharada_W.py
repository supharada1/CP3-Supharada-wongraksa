usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "pppp" and passwordInput == "333555" :
    print("Login successful")
    print("***************** ")
    print("-------Menu------ ")
    print("1.น้ำเปล่า     x 10 (THB) ")
    print("2.ขนมปัง      x 15 (THB) ")
    print("3.ใส้้กรอก     x 25 (THB) ")
    userSelected = int(input(">>>"))
    if userSelected == 1 :
      จำนวน1 = int(input("เลือกจำนวนที่ต้องการ..."))
      ราคา1 = 10
      รวม1 = ราคา1 * จำนวน1
      print("Total     ",รวม1,"(THB)")
    elif userSelected ==2 :
        จำนวน2 = int(input("เลือกจำนวนที่ต้องการ..."))
        ราคา2 = 15
        รวม2 = ราคา2 * จำนวน2
        print("Total   ",รวม2,"(THB)")
    elif userSelected ==3 :
        จำนวน3 = int(input("เลือกจำนวนที่ต้องการ..."))
        ราคา3 = 25
        รวม3 = ราคา3 * จำนวน3
        print("Total   ",รวม3,"(THB)")
print("-------Thank you------")









