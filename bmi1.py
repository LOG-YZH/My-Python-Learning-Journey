def fun_bmi(person,weight,height):
    print(person+'的身高：'+ str(height)+'m,体重为：'+str(weight),'kg')
    bmi=weight/(height*height)
    if bmi<=18.5:
        print('你的bmi为：'+ str(bmi) + '体重过轻')
    elif bmi>=18.5 and bmi<24.9:
        print('你的bmi为：'+ str(bmi) + '正常范围')
    elif bmi>=24.9 and bmi<29.9:
        print('你的bmi为：'+ str(bmi) + '体重过重')
    else:
        print('你的bmi为：'+ str(bmi) + '肥胖')

