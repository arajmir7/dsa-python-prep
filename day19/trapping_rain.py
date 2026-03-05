def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total_water = 0

    while left < right:
        
        if height[left] <= height[right]:
            # Left side controls the water level
            left_max = max(left_max, height[left])
            total_water += left_max - height[left]
            left += 1

        else:
            # Right side controls the water level
            right_max = max(right_max, height[right])
            total_water += right_max - height[right]
            right -= 1

    return total_water


arr = [4,2,0,3,2,5]

print(trap(arr))