def dick(dick1,dick2,dick3):
    dick4={}
    for d in (dick1,dick2,dick3):
        dick4.update(d)
    return (dick4)
dick1={1:2,2:4,3:6}
dick2={4:8,5:10,6:12}
dick3={7:14,8:16,9:18}
print(dick(dick1,dick2,dick3))
