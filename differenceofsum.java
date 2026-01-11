public class differenceofsum {
    public static int differenceofSum(int n, int m){
        int div = 0;
        int notdiv = 0;
        for(int i=1; i<= m; i++){
            if(i%n == 0){
                div += i;
            }else{
                notdiv += i;
            }
        }
        return notdiv - div;
    }    
public static void main(String[] args){
    System.out.println(differenceofSum(4,20));
}
}
