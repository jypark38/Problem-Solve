class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # 거북이와 토끼 초기 위치 설정
        slow = nums[0]
        fast = nums[0]

        # 토끼는 두 칸씩, 거북이는 한 칸씩 이동
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 토끼를 시작 지점으로 옮기고 두 칸씩, 거북이는 한 칸씩 이동
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # 중복된 숫자 반환
        return slow