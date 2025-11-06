class Basics {
    private static void basics1(){
        String newSentence = "I have a good coder teacher named Henry";
        int age = 15;
        int birth = 2015;
        String sentence = "My name is AI nice to meet you"; 
        // print(Yee)
        System.out.println(sentence);
        System.out.println(newSentence);
        if(age>=16){
            System.out.println("I can drive now because I am " + age);
        }
        else if(age == 15){
            System.out.println("I can't drive without my parent but i can drive");
        }
        else if(age==14){
            System.out.println("I can't drive at all but next year I can");
        }
        else{
            System.out.println("I can't drive AT ALL.");
        }
        System.out.println("THAT'S A WROOP");
    }
    public static void main(String[] args) {
        String[] pokemon = {"Diggersby", "Wartortle", "Victreebel", "Snorlax","Throh" };

        // int number = 0;
        // System.out.println(pokemon[number]);
        // number+=1;
        // System.out.println(pokemon[number]);
        // number+=1;
        // System.out.println(pokemon[number]);
        // number+=1;
        // System.out.println(pokemon[number]);
        // number+=1;
        // System.out.println(pokemon[number]);

        for(int number = 0; number < pokemon.length; number+=1){
            System.out.println(pokemon[number]);
        }
    }
}