import java.util.*;

public class Main {
    static int n,m,a,start,now;
    static int[] parent;

    public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);
            n = sc.nextInt();
            m = sc.nextInt();
            parent = new int[n+1];
            // Array 초기화
            for (int i=0; i<=n; i++){
                parent[i] = i;
            }
            // 연결되있으면 union
            for (int i=1; i<=n; i++){
                for (int j=1; j<=n; j++) {
                    a = sc.nextInt();
                    if (a == 1) {
                        union(i,j);
                    }
                }
            }
            // 연결확인
            start = parent[sc.nextInt()];
            for (int i=1;i<m;i++){
                now = sc.nextInt();
                if (parent[now] != start){
                    System.out.println("NO");
                    return;
                }
            }
            System.out.println("YES");
        }

    static int find(int x){
        if (parent[x] == x){
            return x;
        }
        else{
            return parent[x] = find(parent[x]);
        }
    }
    static void union(int x, int y){
        x = find(x);
        y = find(y);
        if (x != y){
            if (x < y) {
                parent[y] = x;
            } else {
                parent[x] = y;
            }
        }
    }
}
