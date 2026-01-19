# PATTERN 1: Hash Map for O(1) Lookups
def hash_map_pattern(nums, target):
    """Two Sum, Contains Duplicate"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# PATTERN 2: Sorting for Anagrams
def anagram_pattern(strs):
    """Group Anagrams, Valid Anagram"""
    anagrams = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))  # Key insight: sorted strings match for anagrams
        anagrams.setdefault(sorted_s, []).append(s)
    return list(anagrams.values())

# PATTERN 3: Frequency Counting
def frequency_pattern(nums, k):
    """Top K Frequent Elements"""
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # Bucket sort approach
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)
    
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]

# PATTERN 4: Prefix & Suffix Products
def prefix_suffix_pattern(nums):
    """Product of Array Except Self"""
    n = len(nums)
    answer = [1] * n
    
    # Prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    # Suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer

# PATTERN 5: Set for O(1) Membership
def set_pattern(nums):
    """Longest Consecutive Sequence"""
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Only start counting from beginning of sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest = max(longest, current_streak)
    
    return longest

# PATTERN 6: Matrix/Grid Validation
def matrix_pattern(board):
    """Valid Sudoku"""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            
            box_index = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                return False
            
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_index].add(val)
    
    return True