// 构造器私有
// 含有一个该类的静态变量来保存这个唯一的实例
// 对外提供获取该实例对象的方式

class Singleton {
    private static Singleton instance = null;
    private Singleton(){
        System.out.println("获取实例");
    }
    public static Singleton getInstance() {
        if(instance == null){
            instance = new Singleton();
        }
        return instance;
    }
}


class HungerSingleton {
    private static Singleton instance = new HungerSingleton();
    private Singleton(){
        System.out.println("获取饿汉实例");
    }
    public static Singleton getInstance() {
        return instance;
    }
}

public class SingletonTest {
    
    public static void main(String[] args) {
        Singleton.getInstance();
    }
}