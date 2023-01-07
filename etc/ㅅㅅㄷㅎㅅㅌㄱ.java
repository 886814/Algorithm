import java.io.IOException;
import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i=1; i<=t;i++) {
            StringTokenizer str = new StringTokenizer(br.readLine(), " ");
            int n = Integer.parseInt(str.nextToken());
            boolean d = true;
            String x = str.nextToken();
            String y = str.nextToken();
            Set<String> xy = new HashSet<>();
            xy.add(x);
            xy.add(y);
            for (int s=n; s>=1; s--){
                Set<String> set = new HashSet<>();
                for (char c : String.valueOf(s).toCharArray()) {
                    set.add(String.valueOf(c));
                }
                if (set.containsAll(xy)&&xy.containsAll(set)){
                    System.out.println("#"+ i + " " + s);
                    d = false;
                    break;
                }
            }
            if (d){
                System.out.println("#"+ i + "-1");
            }
        }
    }
}
