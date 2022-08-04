def search_way_to_point(start, final, maps, step=0):
       current_point=[]
       current_point.append(start)
       next_point=[]
       last_way = []
       while final not in current_point:
           for i in current_point:
               x,y = i[0], i[1]
               if 0 <=x+1<=len(maps[0])-1:
                    if maps[y][x+1] == 0 and ([x+1,y] not in last_way) and ([x+1,y] not in current_point):
                        next_point.append([x+1,y])
               if 0 <= x - 1 <= len(maps[0]) - 1:
                   if maps[y][x - 1] == 0 and ([x - 1, y] not in last_way) and ([x - 1, y] not in current_point):
                      next_point.append([x - 1, y])
               if 0<=y+1<=len(maps)-1 and [x,y+1] not in last_way:
                   if maps[y + 1][x] == 0 and ([x, y + 1] not in last_way) and ([x, y + 1] not in current_point):
                      next_point.append([x, y+1])
               if 0 <= y-1 <= len(maps)-1 and [x,y-1] not in last_way:
                   if maps[y-1][x] == 0 and ([x, y-1] not in last_way) and ([x, y-1] not in current_point):
                       next_point.append([x, y-1])
           if len(next_point) == 0:
               return -1
           step+=1
           last_way.extend(current_point)
           current_point = next_point
           next_point = []
       return step

final_point = [4, 3]
start_point = [0, 1]
place_map = [
    [0,    0,  'x', 0,  0, 0],
    [0,    0,   0, 'x', 0, 0],
    [0,    0,  'x', 0,  0, 0],
    ['x', 0, 'x', 0,  0, 0],
    [0,    0,   0,  0,  0, 0]
]

num_step = search_way_to_point(start_point, final_point, place_map)
if num_step == -1:
    print('Путь до точки отсутсвует')
else:
    print('Путь до точки {} шагов'.format(num_step))




