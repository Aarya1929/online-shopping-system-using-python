import mysql.connector
import matplotlib.pyplot as plt
import pyttsx3
import random
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
z=random.randint(0,1)
engine.setProperty('voice', voices[int(z)].id)
def speak(audio):
engine.say(audio) 
engine.runAndWait() 
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Nitin@2003",
database='mall1'
)
cursor=mydb.cursor()
def electronics():
def addnewitem():
view()
cursor.execute(f"select itemname from electronics")
a=cursor.fetchall()
b=[]
for i in a:
b.append(i[0])
print("\n")
name=input("Enter Item Name:-")
quantity=int(input('Enter Quantity:-'))
price=int(input('Enter Price:-'))
if name in b:
print("Item already present!!\n")
speak("Item already present!!\n")
else:
cursor.execute(f"insert into electronics(itemname,quantity,price) 
values('{name}',{quantity},{price})")
mydb.commit()
def view():
cursor.execute(f"select * from electronics")
a=cursor.fetchall()
print("Itemid Itemname Quantity Price:-\n")
for i in a:
print(i)
def delete():
view()
print("\n")
id=int(input("Enter itemid to delete the item:-\n"))
cursor.execute(f"select itemid from electronics")
a=cursor.fetchall()
b=[]
for i in a:
b.append(i[0])
if id in b:
cursor.execute(f"delete from electronics where itemid={id}")
mydb.commit()
print("Successfully deleted!!\n")
speak("Successfully deleted!!\n")
else:
print("Invalid id!!\n") 
speak("Invalid id!!\n") 
def modify():
view()
print("\n")
id=int(input("Enter itemid to update the item:-\n"))
cursor.execute(f"select itemid from electronics")
a=cursor.fetchall()
b=[]
for i in a:
b.append(i[0])
if id in b:
name=input("Enter new item name:-")
quantity=int(input('Enter new quantity:-'))
price=int(input('Enter new price:-'))
cursor.execute(f"update electronics set 
itemname='{name}',quantity={quantity},price={price} where itemid={id}")
mydb.commit()
print("\n")
print("Successfully updated!!\n")
speak("Successfully updated!!\n")
else:
print("Invalid id!!\n") 
speak("Invalid id!!\n") 
def buy():
view()
price=0
cursor.execute(f"select itemid,price from electronics")
c=cursor.fetchall()
d={}
for i in c:
d[i[0]]=i[1]
cursor.execute(f"select itemid,itemname from electronics")
e=cursor.fetchall()
f={}
for i in e:
f[i[0]]=i[1]
cursor.execute(f"select itemid,quantity from electronics")
u=cursor.fetchall()
g={}
for i in u:
g[i[0]]=i[1] 
bill=[] 
while True:
print("\n")
id=int(input("Enter itemid to purchase the item:-\n"))
cursor.execute(f"select itemid from electronics")
a=cursor.fetchall()
b=[]
cursor.execute(f"select itemid,quantity from electronics")
q=cursor.fetchall()
x={}
for i in q:
x[i[0]]=i[1]
for i in a:
b.append(i[0])
if id in b:
if g[id]==0:
print("Item not available currently!!\n")
speak("Item not available currently!!\n")
print("Sorry for the inconvenience!!\n")
speak("Sorry for the inconvenience!!\n")
break
else:
pass
amount=0
quantity=int(input('Enter quantity you want to purchase:-'))
price+=(quantity*d[id])
amount+=(quantity*d[id])
cursor.execute(f"update electronics set quantity= quantity-
{quantity} where itemid={id}")
mydb.commit()
print("\n")
print("Successfully Purchased!!\n")
speak("Successfully Purchased!!\n")
bill.append((id,f[id],quantity,amount))
speak("Do you want to purchase again? ")
c=input("Do you want to purchase again? Type(y/Y) to continue:-
\n").lower()
if c=="y":
continue
else:
break
else:
print("Invalid id!!\n")
speak("Invalid id!!\n") 
print("\n")
print('Your Total Bill 💴💴') 
print("\n")
print("Itemid Itemname Quantity Price:-\n") 
t=[]
p=[]
for l in bill:
print(l)
t.append(l[2])
p.append(l[1])
plt.pie(t,labels=p)
plt.title("Item vs Quantity:-\n")
plt.show() 
print("\n")
print("Total amount:-",price)
print("\n")
while True:
z=input('Press (p/P) to pay the Bill ').lower()
if z=='p':
print('Bill Paid Successfully!!')
speak('Bill Paid Successfully!!')
print("\n")
print('Thanks for visiting 🙏🙏')
print("\n")
speak('Thanks for visiting')
break
else:
continue
def stock():
cursor.execute(f"select itemname,quantity from electronics")
i=cursor.fetchall()
r=[]
w=[]
for j in i:
r.append(j[1])
w.append(j[0])
plt.bar(w,r)
plt.xlabel("Itemname:-\n")
plt.ylabel("Quantity:-\n")
plt.title("Item vs Quantity:-\n") 
plt.show() 
def sales1():
cursor.execute(f"select itemname,quantity from electronics")
i=cursor.fetchall()
o=[]
r=[]
k=[]
for j in i:
k.append(j[0])
for j in i:
r.append(j[1])
for h in range(len(r)):
o.append(6000-r[h])
while True: 
speak("Enter your choice") 
u=input("Enter 1-Piechart 2-Bargraph 3-Linegraph:-\n") 
if u=="1":
plt.pie(o,labels=k,autopct="%2.2f%%")
plt.title("Item vs % of units sold") 
plt.show()
break
elif u=="2":
plt.bar(k,o)
plt.xlabel("Itemname:-\n")
plt.ylabel("No.of units sold:-\n")
plt.title("Item vs No. of units sold:") 
plt.show()
break
elif u=="3":
plt.plot(k,o)
plt.xlabel("Itemname:-\n")
plt.ylabel("No.of units sold:-\n")
plt.title("Item vs No. of units sold:") 
plt.show()
break
else:
print("Invalid input!!\n") 
speak("Invalid input!!\n") 
continue
return o
print("Welocome To Gada Electronics 😊😊") 
print("\n")
speak("Welocome To Gada Electronics") 
while True:
speak("Enter your choice")
n=int(input("""Enter your choice
1 - To view items 2 - To purchase item 
3 - To add item 4 - To modify item 
5 - To check sales 6 - To check stocks 7 - To delete item:-
\n""")) 
print("\n")
if n==1:
view()
elif n==2:
buy()
elif n==3:
addnewitem()
elif n==4:
modify()
elif n==5:
sales1()
elif n==6:
stock()
elif n==7:
delete() 
elif n not in[1,2,3,4,5,6,7] :
print("Invalid input!!")
speak("Invalid input!!") 
speak("Do you want to continue?")
print("\n")
u=input("Do you want to continue? (y/Y or n/N):-\n").lower()
if u=="y":
continue
else:
print("\n")
print("Thankyou for visiting 🙏🙏\n") 
speak("Thankyou for visiting!!\n") 
break
def clothes():
def addnewitem():
view()
cursor.execute(f"select itemname from clothes")
a=cursor.fetchall()
b=[]
for i in a:
b.append(i[0])
print("\n")
name=input("Enter Item Name:-")
quantity=int(input('Enter Quantity:-'))
price=int(input('Enter Price:-'))
if name in b:
print("Item already present!!\n")
speak("Item already present!!\n")
else:
cursor.execute(f"insert into clothes(itemname,quantity,price) 
values('{name}',{quantity},{price})")
mydb.commit()
def view():
cursor.execute(f"select * from clothes")
a=cursor.fetchall()
print("Itemid Itemname Quantity Price\n")
for i in a:
print(i)
def delete():
view()
print("\n")
id=int(input("Enter itemid to delete the item:-\n"))
cursor.execute(f"select itemid from clothes")
a=cursor.fetchall()
b=[]
for i in a:
b.append(i[0])
if id in b:
cursor.execute(f"delete from clothes where itemid={id} ")
mydb.commit()
print("\n")
print("Successfully deleted!!\n")
speak("Successfully deleted!!\n")
else:
print("Invalid id!!\n") 
speak("Invalid id!!\n") 
def modify():
view()
print("\n")
id=int(input("Enter itemid to update the item:-\n"))
cursor.execute(f"select itemid from clothes")
a=cursor.fetchall()
b=[]
for i in a:
b.append(i[0]) 
if id in b:
name=input("Enter new item name:-")
quantity=int(input('Enter new Quantity:-'))
price=int(input('Enter new Price:-'))
cursor.execute(f"update clothes set 
itemname='{name}',quantity={quantity},price={price} where itemid={id}")
mydb.commit()
print("\n")
print("Successfully updated!!\n")
speak("Successfully updated!!\n")
else:
print("Invalid id!!\n") 
speak("Invalid id!!\n") 
def buy():
view()
price=0
cursor.execute(f"select itemid,price from clothes")
c=cursor.fetchall()
d={}
for i in c:
d[i[0]]=i[1]
cursor.execute(f"select itemid,itemname from clothes")
e=cursor.fetchall()
f={}
for i in e:
f[i[0]]=i[1]
cursor.execute(f"select itemid,quantity from clothes")
u=cursor.fetchall()
g={}
for i in u:
g[i[0]]=i[1] 
bill=[] 
while True:
print("\n")
id=int(input("Enter itemid to purchase the item:-\n"))
cursor.execute(f"select itemid from clothes")
a=cursor.fetchall()
b=[]
cursor.execute(f"select itemid,quantity from clothes")
q=cursor.fetchall()
x={}
for i in q:
x[i[0]]=i[1]
for i in a:
b.append(i[0])
if id in b:
if g[id]==0:
print("Item not available currently!!\n")
speak("Item not available currently!!\n")
print("Sorry for the inconvenience!!\n")
speak("Sorry for the inconvenience!!\n")
break
else:
pass
amount=0
quantity=int(input('Enter quantity you want to purchase:-'))
price+=(quantity*d[id])
amount+=(quantity*d[id])
cursor.execute(f"update clothes set quantity = quantity-
{quantity} where itemid={id}")
mydb.commit()
print("Successfully Purchased!!\n")
speak("Successfully Purchased!!\n")
bill.append((id,f[id],quantity,amount))
speak("Do you want to purchase again? ")
c=input("Do you want to purchase again? Type(y/Y or n/N) to 
continue:-\n").lower()
if c=="y":
continue
else:
break
else:
print("Invalid id!!\n")
speak("Invalid id!!\n") 
print('Your Total Bill 💴💴')
print("\n")
print("Itemid Itemname Quantity Price:-\n") 
t=[]
p=[] 
for l in bill:
print(l)
t.append(l[2])
p.append(l[1])
plt.pie(t,labels=p)
plt.title("Item vs Quantity:-\n")
plt.show() 
print("Total amount:-",price)
print("\n")
while True:
z=input('Press (p/P) to pay the Bill ').lower()
if z=='p':
print('Bill Paid Successfully!!')
print("\n")
speak('Bill Paid Successfully!!')
print('Thanks for visiting 🙏🙏')
speak('Thanks for visiting')
break
else:
continue
def stock():
cursor.execute(f"select itemname,quantity from clothes")
i=cursor.fetchall()
r=[]
w=[]
for j in i:
r.append(j[1])
w.append(j[0])
plt.bar(w,r)
plt.xlabel("Itemname:-\n")
plt.ylabel("Quantity:-\n")
plt.title("Item vs Quantity:-\n") 
plt.show() 
def sales2():
cursor.execute(f"select itemname,quantity from clothes")
i=cursor.fetchall()
w=[]
r=[]
k=[]
for j in i:
k.append(j[0])
for j in i:
r.append(j[1])
for h in range(len(r)):
w.append(6000-r[h])
while True: 
speak("Enter your choice")
u=input("Enter 1-Piechart 2-Bargraph 3-Linegraph:-\n") 
if u=="1":
plt.pie(w,labels=k,autopct="%2.2f%%")
plt.title("Item vs % of units sold") 
plt.show()
break
elif u=="2":
plt.bar(k,w)
plt.xlabel("Itemname:-\n")
plt.ylabel("No. of units sold:-\n")
plt.title("Item vs No. of units sold") 
plt.show()
break
elif u=="3":
plt.plot(k,w)
plt.xlabel("Itemname:-\n")
plt.ylabel("No. of units sold:-\n")
plt.title("Item vs No. of units sold") 
plt.show()
break
else:
print("Invalid input!!\n") 
speak("Invalid input!!") 
continue
return w
print("Welocome To Vastra Bhandar 😊😊\n") 
speak("Welocome To Vastra Bhandar:-\n") 
while True:
speak("Enter your choice")
n=int(input("""Enter your choice
1 - To view items 2 - To purchase item 
3 - To add item 4 - To modify item 
5 - To check sales 6 - To check stocks 7 - To delete item\n"""))
if n==1:
view()
elif n==2:
buy()
elif n==3:
addnewitem()
elif n==4:
modify()
elif n==5:
sales2()
elif n==6:
stock()
elif n==7:
delete() 
elif n not in[1,2,3,4,5,6,7] :
print("Invalid input!!")
speak("Invalid input!!")
speak("Do you want to continue?") 
u=input("Do you want to continue? (y/Y or n/N):-\n").lower()
if u=="y":
continue
else:
print("\n")
print("Thankyou for visiting 🙏🙏\n") 
speak("Thankyou for visiting:-\n") 
break
def Mallsales():
def sales1():
cursor.execute(f"select itemname,quantity from electronics")
i=cursor.fetchall()
o=[]
r=[]
k=[]
for j in i:
k.append(j[0])
for j in i:
r.append(j[1])
for h in range(len(r)):
o.append(6000-r[h])
return o
def sales2():
cursor.execute(f"select itemname,quantity from clothes")
i=cursor.fetchall()
w=[]
r=[]
k=[]
for j in i:
k.append(j[0])
for j in i:
r.append(j[1])
for h in range(len(r)):
w.append(6000-r[h]) 
return w
a=sales2()
b=sales1() 
q=0
n=0
for j in a:
q+=j
for j in b:
n+=j
plt.pie([n,q],labels=["electronics","clothes"],autopct="%2.2f%%",explod
e=[0.1,0])
plt.title("% of items sold:-\n")
plt.show()
print("\n")
print(" ********** Welcome to 
Phoenix Market City **********\n")
speak("Welcome to Phoenix Market City:-\n")
while True:
speak("Enter your choice")
n=int(input("""Enter your choice
1-Electronics 2-Clothes 3-Sales:-\n""")) 
if n==1:
electronics()
elif n==2:
clothes()
elif n==3:
Mallsales()
speak("Do you want to shop again?") 
u=input("Do you want to shop again? (y/Y or n/N):-\n").lower()
if u=="y":
continue
else:
print("\n")
print("Thankyou for visiting 🙏🙏\n") 
speak("Thankyou for visiting:-\n") 
break