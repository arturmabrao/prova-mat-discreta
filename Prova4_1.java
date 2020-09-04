package prova4_1;

import java.util.Arrays;

public class Prova4_1 {

    final static int TAMANHO = 10;

    public static void main(String[] args) {

        int tabela[] = new int[TAMANHO];

        preencherTabela(tabela, stringToInt("ab"));
        preencherTabela(tabela, stringToInt("bc"));
        preencherTabela(tabela, stringToInt("cd"));
        preencherTabela(tabela, stringToInt("de"));
        preencherTabela(tabela, stringToInt("ef"));
        preencherTabela(tabela, stringToInt("fg"));
        preencherTabela(tabela, stringToInt("gh"));
        preencherTabela(tabela, stringToInt("hi"));
        preencherTabela(tabela, stringToInt("ij"));
        preencherTabela(tabela, stringToInt("ab"));
        preencherTabela(tabela, stringToInt("ji"));
        preencherTabela(tabela, stringToInt("dd"));

        System.out.println(Arrays.toString(tabela));
    }

    public static void preencherTabela(int[] tabela, int chave) {
        int posicao = chave % TAMANHO;
        if (tabela[posicao] == 0) {
            tabela[posicao] = chave;
        } else {
            int tam = TAMANHO;
            boolean reset = false;
            for (int i = posicao; i < tam; i++) {
                if (tabela[i] == 0) {
                    tabela[i] = chave;
                    break;
                } else if (i == TAMANHO - 1) {
                    i = -1;
                    tam = posicao;
                    reset = true;
                }

                if (i == posicao - 1 && reset) {
                    System.out.println("Tabela cheia, impossível incluir a chave: " + chave);
                }
            }
        }
    }

    public static int stringToInt(String str) {
        byte[] bytes = str.getBytes();
        int soma = 0;
        for (byte b : bytes) {
            StringBuilder bite = new StringBuilder();
            int val = b;
            for (int i = 0; i < 8; i++) {
                bite.append((val & 128) == 0 ? 0 : 1);
                val <<= 1;
            }
            soma += Integer.parseInt(bite.toString(), 2);
        }
        return soma;
    }

}
