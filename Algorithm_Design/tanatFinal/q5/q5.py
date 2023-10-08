rows, cols = map(int, input().split())
image = []

# Read the image data into a 2D list
for i in range(rows):
    image.append(list(map(int, input().split())))


def is_valid(i, j):
    # Check if the pixel at (i, j) is a valid cloud pixel
    return 0 <= i < rows and 0 <= j < cols and image[i][j] == 1


def dfs(i, j):
    # DFS function to explore connected cloud pixels and count their size
    if not is_valid(i, j):
        return 0

    # Mark the current pixel as visited
    image[i][j] = -1

    size = 1

    # Explore neighboring pixels in all four directions
    size += dfs(i - 1, j)  # Up
    size += dfs(i + 1, j)  # Down
    size += dfs(i, j - 1)  # Left
    size += dfs(i, j + 1)  # Right

    return size


largest_cloud_size = 0

# Iterate through all pixels to find the largest cloud
for i in range(rows):
    for j in range(cols):
        if is_valid(i, j):
            cloud_size = dfs(i, j)
            largest_cloud_size = max(largest_cloud_size, cloud_size)

# Print the size of the largest cloud
print(largest_cloud_size)
