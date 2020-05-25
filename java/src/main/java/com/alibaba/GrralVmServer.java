package com.alibaba;

import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public class GrralVmServer {
//    public static class MyClass {
//        public int id = 42;
//        public String text = "42";
//        public int[] arr = new int[]{1, 42, 3};
//        public Callable<Integer> ret42 = () -> 42;
//    }

    public static void main(String[] args) throws Exception {
        int num = 0;
        try (Context context = Context.newBuilder().allowAllAccess(true).build()) {
//            context.eval("python", "print('Hello Python!')");
//            File file = new File("/tmp/func.txt");
//            InputStream inputStream = new BufferedInputStream(new FileInputStream(file));
//            int len = inputStream.available();
//            byte[] data = new byte[len];
//            inputStream.read(data);
//            context.getPolyglotBindings().putMember("wrapper", new MyClass());
//            inputStream.close();
            String source = "import polyglot\n" +
                    "import site\n" +
                    "import cloudpickle\n" +
                    "def another_inc(val):\n" +
                    "    return val + 1\n\n" +
                    "@polyglot.export_value\n" +
                    "def inc(val):\n" +
                    "    return another_inc(val)\n\n";
            Source script = Source.create("python", source);
            context.eval(script);
            Value incFunc = context.getPolyglotBindings().getMember("inc");
            incFunc.execute(num);
            long start = System.currentTimeMillis();
            long duration = 1000;
            while (System.currentTimeMillis() - start < duration) {
                Value result = incFunc.execute(num);
                num += 1;
            }
            System.out.format("Received %d messages in %d second(s)", num, duration);
        }
    }
}
