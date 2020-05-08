class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 按二维坐标系计算
        # y+1正前一步，x+1右拐，y-1后退一步，x-1左拐
        xy = ((0, 1), (1, 0), (0, -1), (-1, 0))
        di = x = y = 0
        dist = 0
        obs_dict = {}

        for obs in obstacles:
            obs_dict[tuple(obs)] = 0

        for cmd in commands:
            if cmd == -2:
                di = (di + 3) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for j in range(cmd):
                    dx, dy = xy[di]
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obs_dict:
                        break
                    x, y = next_x, next_y
                    dist = max(dist, x * x + y * y)

        return dist

