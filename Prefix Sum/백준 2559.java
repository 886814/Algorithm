import java.util.*;

public class Main {
    static int n,k;
    static int[] a;
    static int[] s;
    static int ans = Integer.MIN_VALUE;
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();

        a = new int[n];
        s = new int[n+1];

        for (int i=0;i<n;i++){
            a[i] = sc.nextInt();
        }

        for (int i=1; i<=n; i++) {
            s[i] = s[i-1] + a[i-1];
        }

        for (int i=k; i<=n; i++){
            ans = Math.max(ans, s[i] - s[i-k]);
        }
        System.out.println((ans));
    }

}
