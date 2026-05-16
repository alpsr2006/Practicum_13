def three_sum(nums):
    """
        Находит все уникальные тройки чисел, дающие в сумме 0.

        Алгоритм:
        1. Сортируем массив
        2. Фиксируем первый элемент (i)
        3. Двумя указателями (left, right) ищем пару для nums[i]
        4. Пропускаем дубликаты

        Args:
            nums: список целых чисел

        Returns:
            список уникальных троек [a,b,c] где a+b+c=0
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result


nums = list(map(int, input().strip('[]').split(',')))
print(three_sum(nums))