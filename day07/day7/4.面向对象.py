# 人狗大战
# 人-角色
    # 名称 等级 血量 攻击力 性别 职业
def Person(name,hp,ad,sex,job,level=1):   # 角色的模板
    person_dic = {'name':name,'level':level,'hp':hp,'ad':ad,'sex':sex,'job':job}
    def attack(dog):
        dog['hp'] -= person_dic['ad']
        print('%s攻击了%s,%s掉了%s点血'%(person_dic['name'],dog['name'],dog['name'],person_dic['ad']))
    person_dic['attack'] = attack
    return person_dic
alex = Person('alex',100,5,'不详','乞丐')   # 角色
wusir = Person('wusir',200,6,'女','嫂子')
print(alex)
print(wusir)
# 狗-角色
def Dog(name,kind,hp,ad):
    dog_dic = {'name':name,'kind':kind,'hp':hp,'ad':ad}
    def bite(person):
        person['hp'] -= dog_dic['ad']
        print('%s咬了%s,%s掉了%s点血' % (dog_dic['name'], person['name'], person['name'], dog_dic['ad']))
    dog_dic['bite'] = bite
    return dog_dic
dog1= Dog('旺财','teddy',2000,150)
print(dog1)
dog2 = Dog('二饼','哈士奇',10000,300)
print(dog2)
dog1['bite'](wusir)
alex['attack'](dog1)
