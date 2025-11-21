import java.util.Scanner;

class Main{
    public static void main(String[] args){
        final int rangeMax = 100;
        final int rangeMin = 1;
        int number = (int)(Math.random() * rangeMax + rangeMin);
        // System.out.println(number);
        System.out.println("I'm thinking of a number between " + rangeMin + " and " + rangeMax );

        Scanner scan = new Scanner(System.in);
        int userInput = rangeMax + rangeMin;
        
        while(number != userInput){
            //type in another number
            userInput = scan.nextInt();
            
            //This grades your response
            if (number == userInput){
                System.out.println("Your correct! ");
            }
            else {
                if (userInput > number) {
                    System.out.println("Your number is too big ");
                }
                else {
                    System.out.println("Your number is too small ");
                }
                System.out.println("Try again");
            }
        }
    }
}