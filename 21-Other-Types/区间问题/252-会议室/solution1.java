// 题目：
// 给定一个会议时间安排的数组 intervals ，每个会议时间都会
// 包括开始和结束的时间 intervals[i] = [starti, endi] ，
// 请你判断一个人是否能够参加这里面的全部会议

class solution1 {
    public static boolean canAttendMeeting(int[][] intervals) {
        // 按照会议室的开始时间 做升序排序
        Arrays.sort(intervals, (v1, v2) -> v1[0] - v2[0]);
        
        for (int i = 1; i < intervals.length; i++) {
            // 如果 上一个结束的时间 大于 当前时间的开始，说明两个时间段有重叠
            if (intervals[i][0] < intervals[i - 1][1]) {
                return false;
            }
        }
        return true;
    }
    
    public static void main(String[] args) {
        // int[][] intervals = {{0,30},{5,10},{15,20}};
        
        // System.out.println(canAttendMeeting(intervals));
        System.out.println("1");
    }
}