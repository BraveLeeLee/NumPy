import numpy as np

array = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 9)))

# 基本的索引
assert (array[0] == [1, 2, 3]).all()

# 基本的切片
assert (array[:1] == [[1, 2, 3]]).all()
assert (array[:, :1] == [[1], [4], [7]]).all()

print(array[2:0:-1, 1:3])
