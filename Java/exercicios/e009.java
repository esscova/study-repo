/**
 * 
 * OBJETIVO: informar se um número é positivo, negativo ou zero.
 * DESCRICAO:Escreva um programa que leia um número (hardcode por enquanto) e imprima se ele é positivo, negativo ou zero. 
 * 
 */

public class e009{
	public static void main (String[] args){
		// variaveis
		int num = -5;

		// processamento e escrita
		if (num>0){
			System.out.println("Positivo\n");
		} else if (num < 0){
			System.out.println("Negativo\n");
		} else {
			System.out.println("Zero\n");
		}
	}
}