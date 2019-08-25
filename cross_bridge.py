def get_time(a, b, c, d):
    return a+b+c+d+min(a,b,c,d)

class GetTime{
    public static int main(String args[]){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        return a+b+c+d+Math.min(a,Math.min(b,Math.min(c,d)));
    }
}