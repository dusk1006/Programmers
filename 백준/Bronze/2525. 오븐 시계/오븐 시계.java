import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int cook = sc.nextInt();

        int total = hour * 60 + minute + cook;

        int resultHour = (total / 60) % 24;
        int resultMinute = total % 60;

        System.out.println(resultHour + " " + resultMinute);
    }
}