from user import user

user1 = user()

user1.set_screen_name('SuTTe')

print user1.get_screen_name()
"
f = open('user_data/history/history_user_1','r')

s=[]

for line in f:
    s.append(str(line))

f2 = open('user_data/opinions/opinion_user_1','w')
a =  user1.create_subject_list(s)
f2.write(str(a))
print a
"

f = open('user_data/traits/traits_user_1','r')

o = f.read()
trait_dict = eval(o)


