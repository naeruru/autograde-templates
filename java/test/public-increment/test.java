package p0;

import java.io.FileWriter;
import java.io.IOException;

class Test {
    public static void main(String[] args) {
        Counter c = new Counter();
        c.increment();

        try {
            FileWriter outFile = new FileWriter("output");
            outFile.write(String.valueOf(c.getCount()));
            outFile.close();

            // generate answer file ahead of time
            // FileWriter answerFile = new FileWriter("answer");
            // answerFile.write(String.valueOf(c.getCount()));
            // answerFile.close();
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}