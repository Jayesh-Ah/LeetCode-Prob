class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        freshcount = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshcount += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        minutes = 0

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(0,1), (0,-1), (-1,0), (1,0)]:
                    nx, ny = x + dx, y + dy
                    if rows > nx >= 0 and cols > ny >= 0 and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        freshcount -= 1
                        queue.append((nx, ny))

            if queue:
                minutes += 1
        return minutes if freshcount == 0 else -1
                