import numpy as np

# ndarray的创建
# 使用数组创建
array = np.array([[1, 2, 3], [4, 5, 6]])
array = np.asarray([[1, 2, 3], [4, 5, 6]])

# 使用生成器创建
array = np.arange(1, 10, 2, dtype=int)
array = np.arange(15)

# 创建元素全为0的数组
zero_array = np.zeros((2, 3))
# 根据已有数组的形状创建元素全为0的数组
zeros_like_array = np.zeros_like(array)

# 创建元素全为1的数组
one_array = np.ones((2, 3))
# 根据已有数组的形状创建元素全为1的数组
one_like_array = np.ones_like(array)

# 创建元素为空的数组
empty = np.empty((1, 2))
# 根据已有数组的形状创建元素全为空的数组
empty_like = np.empty_like(array)

# 创建单位矩阵
eye = np.eye(10, 9)
print(eye)
identity = np.identity(3)
print(identity)
