// Answer code for testing purposes. Allows you to make use of the test/ folder.
// Anything outside of the starter/ and test/ folder is optional.

package p0;

public class Counter {
    
    int count;

    public Counter() {
        this.count = 0;
    }

    public int getCount() {
        return count;
    }

    public void increment() {
        count += 1;
    }

    public void decrement() {
        count -= 1;
    }

}