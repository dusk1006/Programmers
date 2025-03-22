import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hour = sc.nextInt();
        int minute = sc.nextInt();


        if (minute >= 45) {
            System.out.println((hour)+ " " +(minute-45));
        }else if (hour == 0 && minute < 45) {
            System.out.println((23)+ " " +(60-(45-minute)));
        } else{
            System.out.println((hour-1)+ " " +(60-(45-minute)));
        }
    }

}