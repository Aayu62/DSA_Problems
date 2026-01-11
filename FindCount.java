public class FindCount {

    public static int Findcount(int[] arr, int length, int num, int diff) {

        int count = 0;
        for (int i = 0; i < length; i++) {
            if (Math.abs(num - arr[i]) <= diff) {
                count++;
            }
        }

        if (count == 0) {
            return -1;
        }
        return count;
    }

    public static void main(String[] args) {
        int[] arr = {12, 3, 14, 56, 77, 13};
        int num = 13;
        int diff = 2;

        System.out.println(Findcount(arr, arr.length, num, diff));
    }
}