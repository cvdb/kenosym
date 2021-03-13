def load_pay_table():
    # We play games 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 40
    pay_table = []

    # 20 numbers are drawn but use 21 here 
    # because ZERO also pays in some cases
    one = [0] * 21
    one[1] = 3
    pay_table.append(one)

    two = [0] * 21
    two[2] = 12
    pay_table.append(two)

    three = [0] * 21
    three[2] = 1
    three[3] = 44
    pay_table.append(three)

    four = [0] * 21
    four[2] = 1
    four[3] = 4
    four[4] = 120
    pay_table.append(four)

    five = [0] * 21
    five[3] = 2
    five[4] = 14
    five[5] = 640
    pay_table.append(five)

    six = [0] * 21
    six[3] = 1
    six[4] = 5
    six[5] = 80
    six[6] = 1800
    pay_table.append(six)

    seven = [0] * 21
    seven[3] = 1
    seven[4] = 3
    seven[5] = 12
    seven[6] = 125
    seven[7] = 5000
    pay_table.append(seven)

    eight = [0] * 21
    eight[4] = 2
    eight[5] = 7
    eight[6] = 60
    eight[7] = 675
    eight[8] = 25000
    pay_table.append(eight)

    nine = [0] * 21
    nine[4] = 1
    nine[5] = 5
    nine[6] = 20
    nine[7] = 210
    nine[8] = 2500
    nine[9] = 100000
    pay_table.append(nine)

    ten = [0] * 21
    ten[4] = 1
    ten[5] = 2
    ten[6] = 6
    ten[7] = 50
    ten[8] = 580
    ten[9] = 10000
    ten[10] = 1000000
    pay_table.append(ten)

    # 11,12,13,14
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)

    fifteen = [0] * 21
    fifteen[5] = 1
    fifteen[6] = 2
    fifteen[7] = 4
    fifteen[8] = 20
    fifteen[9] = 50
    fifteen[10] = 250
    fifteen[11] = 2000
    fifteen[12] = 12000
    fifteen[13] = 50000
    fifteen[14] = 100000
    fifteen[15] = 250000
    pay_table.append(fifteen)

    # 16,17,18,19
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)

    twenty = [0] * 21
    twenty[0] = 100
    twenty[1] = 10
    twenty[2] = 2
    twenty[8] = 2
    twenty[9] = 7
    twenty[10] = 20
    twenty[11] = 100
    twenty[12] = 450
    twenty[13] = 1200
    twenty[14] = 5000
    twenty[15] = 10000
    twenty[16] = 15000
    twenty[17] = 25000
    twenty[18] = 50000
    twenty[19] = 100000
    twenty[20] = 250000
    pay_table.append(twenty)

    # 21,22,23,24....39
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)
    pay_table.append([0] * 21)

    fourty = [0] * 21
    fourty[0] = 250000
    fourty[1] = 25000
    fourty[2] = 2200
    fourty[3] = 200
    fourty[4] = 35
    fourty[5] = 7
    fourty[6] = 2
    fourty[7] = 1
    fourty[13] = 1
    fourty[14] = 2
    fourty[15] = 7
    fourty[16] = 35
    fourty[17] = 200
    fourty[18] = 2200
    fourty[19] = 25000
    fourty[20] = 250000
    pay_table.append(fourty)

    return pay_table
