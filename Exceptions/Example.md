# Handling Exceptions

This code was meant to ask the user for a month number and print out the month's short name that corresponds to that number!

```
public static void main(String[] args) {
    String[] months = {"Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
    Scanner scanner = new Scanner(System.in);
    try {
        int month = scanner.nextInt();
        System.out.print(months[month]);
    } catch (IndexOutOfBoundsException exception) {
        System.out.print("Index is out of bounds");
    } catch (InputMismatchException exception) {
        System.out.print("Input mismatch");
    }

}
```
**Q-1**. What will be the output if the user enters **3** ?

**Ans**: **Apr**

**Q-1**. What will be the output if the user enters **99** ?

**Ans**: **Index is out of bounds**

**Q-1**. What will be the output if the user enters **abc** ?

**Ans**: **Input mismatch**
