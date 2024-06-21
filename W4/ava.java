

import java.util.HashMap;

public class HashMapOperations {
    public static void main(String[] args) {
        // Create a new HashMap
        HashMap<String, Integer> hashMap = new HashMap<>();

        // Adding elements to the HashMap
        hashMap.put("John", 25);
        hashMap.put("Jane", 30);
        hashMap.put("Doe", 35);
        System.out.println("Initial HashMap: " + hashMap);

        // Changing an existing value
        hashMap.put("John", 26);
        System.out.println("After changing John's age: " + hashMap);

        // Removing an element
        hashMap.remove("Doe");
        System.out.println("After removing Doe: " + hashMap);

        // Checking if a key exists
        String keyToCheck = "Jane";
        if (hashMap.containsKey(keyToCheck)) {
            System.out.println(keyToCheck + " is present in the HashMap");
        } else {
            System.out.println(keyToCheck + " is not present in the HashMap");
        }

        // Retrieving a value
        String keyToRetrieve = "John";
        int johnsAge = hashMap.get(keyToRetrieve);
        System.out.println("Age of " + keyToRetrieve + ": " + johnsAge);
    }
}



