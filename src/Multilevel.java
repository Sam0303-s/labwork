class X3{
    private final int a;
    public int b;
    protected int c;
    X3(){
        a = 50;
        b = 80;
        c = 60;
    }
    void disp(){
        System.out.println("I am in x:  ");

        System.out.println("a is private var a:  " + a);
        System.out.println("b is public var b:  " + b);
        System.out.println("c is protected var c:  " + c);
    }
}
class Y extends X3{
    void print(){
        System.out.println("b is public var:  " + b);
        System.out.println("c is protected var:  " + c);
    }
}
class Z3 extends Y{
    void show(){
        System.out.println("I am in z  :");
        System.out.println("b is public var:  " + b);
        System.out.println("c is protected var:  " + c);
    }
}
public class Multilevel{
    public static void main(String[] args){
        X3 x1 = new X3();
        x1.disp();
        System.out.println("\n");
        Y y1 = new Y();
        y1.print();
        System.out.println("\n");
        Z3 z1 = new Z3();
        z1.show();
    }
}