import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int max = Integer.parseInt(br.readLine());

        for (int i = 0; i < max; i++) {
            String[] input = br.readLine().split(" ");
            int price = Integer.parseInt(input[0]);
            int ea = Integer.parseInt(input[1]);

            int count = price + ea;
            bw.write(count + "\n");
        }

        bw.flush();
        bw.close();
    }
}
