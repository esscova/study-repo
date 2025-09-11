/**
 * OBJETIVO: Utilizar a sintaxe SWITCH
 * DESCRICAO: Crie um programa que, com base no número fornecido determine e exiba o feedback correspondente
 **/

public class e011{
	public static void main (String[] args){
		// variaveis
		int nivel = 5;
		String feedback;

		// processamento
		feedback = switch(nivel){
			case 1 -> "Muito insatisfeito";
			case 2 -> "Insatisfeito";
			case 3 -> "Neutro";
			case 4 -> "Satisfeito";
			case 5 -> "Muito satisfeito";
			default -> "Opção inválida";	
		};

		// escrita
		System.out.println(feedback);

	}
}