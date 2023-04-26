class Cover:
    # 使用字典表示小写数字与大写数字的对应关系
    def __init__(self, num):
        """初始化统计信息"""
        self.num = list(str(num))
        self.file2_path = 'E:/Python_Project/Num_conversion/输出结果.txt'
        self.dict1 = {0: '零', 1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍', 6: '陆', 7: '柒', 8: '捌', 9: '玖'}

    def write_file(self, result):
        with open(self.file2_path, 'a') as file_object_w:
            file_object_w.write(result + '\n')

    def num_unit(self, num):
        result = self.dict1[num]
        return result

    def num_ten(self, num):
        unit = num % 10
        ten = self.dict1[int(num / 10)]
        if unit != 0:
            result = ten + '拾' + Cover(num).num_unit(unit)
            return result
        else:
            result = ten + '拾'
            return result

    def num_hundred(self, num):
        unit = num % 10
        ten = num % 100
        ten1 = int(num % 100 / 10)
        hundred = self.dict1[int(num / 100)]
        if ten1 != 0:
            result = hundred + '佰' + Cover(num).num_ten(ten)
            return result
        elif ten1 == 0:
            if unit != 0:
                result = hundred + '佰零' + Cover(num).num_unit(unit)
                return result
            else:
                result = hundred + '佰'
                return result

    def num_thousand(self, num):
        unit = num % 10
        ten = num % 100
        ten1 = int(ten / 10)
        hundred = num % 1000
        hundred1 = int(hundred / 100)
        thousand = self.dict1[int(num / 1000)]
        if hundred1 != 0:
            result = thousand + '仟' + Cover(num).num_hundred(hundred)
            return result
        elif hundred1 == 0:
            if ten1 != 0:
                result = thousand + '仟零' + Cover(num).num_ten(ten)
                return result
            else:
                if unit != 0:
                    result = thousand + '仟零' + Cover(num).num_unit(unit)
                    return result
                else:
                    result = (thousand + '仟')
                    return result

    def num_million(self, num):
        result = Cover(num).num_million_up(num) + Cover(num).num_million_down(num)
        return result

    def num_million_up(self, num):
        million1 = int(num / 10000)
        if len(str(million1)) == 1:
            result = Cover(num).num_unit(million1) + '万'
            return result
        elif len(str(million1)) == 2:
            result = Cover(num).num_ten(million1) + '万'
            return result
        elif len(str(million1)) == 3:
            result = Cover(num).num_hundred(million1) + '万'
            return result
        elif len(str(million1)) == 4:
            result = Cover(num).num_thousand(million1) + '万'
            return result

    def num_million_down(self, num):
        million2 = num - int(num / 10000) * 10000
        thousand = int(million2 / 1000)
        hundred = int(million2 % 1000 / 100)
        ten = int(million2 % 100 / 10)
        unit = int(million2 % 10)
        if thousand != 0:
            result = Cover(num).num_thousand(million2)
            return result
        else:
            if hundred != 0:
                result = '零' + Cover(num).num_hundred(million2)
                return result
            else:
                if ten != 0:
                    result = '零' + Cover(num).num_ten(million2)
                    return result
                else:
                    if unit != 0:
                        result = '零' + Cover(num).num_unit(million2)
                        return result
                    else:
                        result = ''
                        return result
