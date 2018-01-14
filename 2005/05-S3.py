# Input data
n = int(input())
matrices = []
sizes = []
for i in range(n):
    matrices.append([])
    r, c = map(int, input().split())
    sizes.append([r, c])
    for _ in range(r):
        matrices[i].append(list(map(int, input().split())))


# Function to calculate the sensor product
def product(a, b, size_a, size_b):
    size_c = [size_a[0]*size_b[0], size_a[1]*size_b[1]]
    c = [[0 for _ in range(size_c[1])] for _ in range(size_c[0])]

    for i in range(size_a[0]):
        for j in range(size_a[1]):
            for k in range(size_b[0]):
                for t in range(size_b[1]):
                    c[i * size_b[0] + k][j * size_b[1] + t] = a[i][j] * b[k][t]

    return c, size_c

# Build the final matrix
ans, ans_size = product(matrices.pop(0), matrices.pop(0), sizes.pop(0), sizes.pop(0))
while len(matrices) > 0:
    ans, ans_size = product(ans, matrices.pop(0), ans_size, sizes.pop(0))

# Determine the extreme values the problem asked
row_sum = []
column_sum = []
max_val = []
min_val = []
for i in ans:
    row_sum.append(sum(i))
    max_val.append(max(i))
    min_val.append(min(i))
for i in range(ans_size[1]):
    sumt = 0
    for j in range(ans_size[0]):
        sumt += ans[j][i]
    column_sum.append(sumt)
print(max(max_val))
print(min(min_val))
print(max(row_sum))
print(min(row_sum))
print(max(column_sum))
print(min(column_sum))
