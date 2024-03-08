class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N//2):
            currN = N-i*2
            d1 = [i,i]
            d2 = [i,N-1-i]
            d3 = [N-1-i,N-1-i]
            d4 = [N-1-i,i]
            
            for j in range(currN-1):
                
                d=[d1,d2,d3,d4]
                for k in range(3):
                    px,py = d[3]
                    cx,cy = d[k]
                    matrix[px][py], matrix[cx][cy] = matrix[cx][cy], matrix[px][py]
                d1[1] += 1
                d2[0] += 1
                d3[1] -= 1
                d4[0] -= 1