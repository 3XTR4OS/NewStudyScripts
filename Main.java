package com.company;
import java.util.Scanner;

class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        System.out.print("Введите ваш возвраст: ");
        int age = in.nextInt();

        if (age < 18)
            System.out.print("Вы не можете приобрести данные лекарства");
        else
            System.out.print("Вы достигли совершеннолетия и можете приобрести данные лекарства");
    }
}