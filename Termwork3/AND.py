w1 = 0
w2 = 0
def step(x):
    return 0 if w1*x[0] + w2*x[1] <= t else 1

def cal_new_weights(error):
    global w1, w2
    w1  = w1 + (a*x1_list[i]*error)
    w2  = w2 + (a*x2_list[i]*error)
    print('w1{0}, w2{0}'.format(w1, w2) )

def compare_y(y1, y2):
    if y1 != y2:
        return abs(y1-y2)
    else:
        return 0

y_list = [0,0,0,1]
actual_y = []

while(y_list != actual_y):
    actual_y = []
    x1_list = [0,0,1,1]
    x2_list = [0,1,0,1]
    a = 0.2
    t = 1
    for i in range(4):
        actual_y.append(step([x1_list[i],x2_list[i]]))
        error = compare_y(y_list[i], actual_y[i])
        cal_new_weights(error)
    print(actual_y)
