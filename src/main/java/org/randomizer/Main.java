package org.randomizer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        System.out.println("Welcome!");
        System.out.println("Generate Characters (g)");
        System.out.println("Exit program (e)");

        boolean run = true;
        while(run) {
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(System.in));

            String amount = reader.readLine();

            if (amount.equals("g")) {
                System.out.println("Character creation");
            } else if (amount.equals("e")) {
               run = false;
            } else {
                System.out.println("Invalid Input!");
            }

        }
    }
}