public class LargeSmallSum {

    public static int largestSmallSum(int[] arr) {

        if (arr == null || arr.length <= 3) {
            return 0;
        }

        int evenLargest = Integer.MIN_VALUE;
        int evenSecondLargest = Integer.MIN_VALUE;

        int oddSmallest = Integer.MAX_VALUE;
        int oddSecondSmallest = Integer.MAX_VALUE;

        for (int i = 0; i < arr.length; i++) {

            if (i % 2 == 0) {
                if (arr[i] > evenLargest) {
                    evenSecondLargest = evenLargest;
                    evenLargest = arr[i];
                } else if (arr[i] > evenSecondLargest) {
                    evenSecondLargest = arr[i];
                }
            } else {
                if (arr[i] < oddSmallest) {
                    oddSecondSmallest = oddSmallest;
                    oddSmallest = arr[i];
                } else if (arr[i] < oddSecondSmallest) {
                    oddSecondSmallest = arr[i];
                }
            }
        }

        return evenSecondLargest + oddSecondSmallest;
    }
}


class Main {
    public static void main(String[] args) {

        int[] arr = {3, 2, 1, 7, 5, 4};

        int result = LargeSmallSum.largestSmallSum(arr);
        System.out.println(result);
    }
}

