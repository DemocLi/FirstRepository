from coversation import Cover


file1_path = 'E:/Python_Project/Num_conversion/数据源.txt'
with open(file1_path) as file_object:
    data = file_object.readlines()
    for datum in data:
        datum1 = int(datum)
        # 获取外部输入数据
        # 进行数据的转换处理
        if 0 <= datum1 <= 99999999:
            # 根据数据的长度进行分类处理
            # 数字长度为1的情况（0-9）
            if len(datum.rstrip()) == 1:
                Cover(datum1).write_file(Cover(datum1).num_unit(datum1))
            # 数字长度为2的情况（10-99）
            elif len(datum.rstrip()) == 2:
                Cover(datum1).write_file(Cover(datum1).num_ten(datum1))
            # 数字长度为3的情况（100-999）
            elif len(datum.rstrip()) == 3:
                Cover(datum1).write_file(Cover(datum1).num_hundred(datum1))
            # 数字长度为4的情况（1000-9999）
            elif len(datum.rstrip()) == 4:
                Cover(datum1).write_file(Cover(datum1).num_thousand(datum1))
            else:
                Cover(datum1).write_file(Cover(datum1).num_million(datum1))
        else:
            Cover(datum1).write_file('超出范围')
        # 输出转换的结果
