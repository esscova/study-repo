/**
 * OBJETIVO: Prática com Switch
 * DESCRICAO: Determine o número de dias no mes com base no valor de uma variavel
 **/

public class e012{
	public static void main (String[] args){
		// variaveis
		String mes = "Agosto";
		int dias;


		// processamento
		dias = switch(mes){
			case "Janeiro", "Março", "Maio", "Julho", "Agosto", "Outubro", "Dezembro" -> 31;
			case "Abril", "Junho", "Setembro", "Novembro" -> 30;
			case "Fevereiro" -> 28;
			default -> {
				System.out.println("Mês desconhecido");
				yield -1;
			}
		};

		// escrita
		if (dias != -1){
			System.out.println("O mês de " + mes + " tem " + dias + " dias.");
		}

	}
}