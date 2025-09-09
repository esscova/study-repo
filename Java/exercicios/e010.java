/**
 * 
 * OBJETIVO: Treinar operador ternario 
 * DESCRICAO: Crie um programa que determine se um ano (hardcode) é bissexto (divisível por 4, mas não por 100, exceto se por 400). Use ternário para atribuir "Sim" ou "Não".
 * 
 **/

public class e010{
	public static void main (String[] args){
		// variaveis
		int ano = 2025;
		String res;

		// processamento
		res = ((ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0))? "Sim" : "Não";

		// escrita
		System.out.println(ano + " é bissexto? " + res);
	}
}