import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        int size = 0;
        ArrayList<Double> arrayList = new ArrayList<>();
        double eps = 1488;
        Scanner inConsole = new Scanner(System.in);
        System.out.println("Введите: 1 - для ввода с консоли; 2 - для чтения файла");
        int num = inConsole.nextInt();
        while (!(num == 1 || num == 2))
        {
            System.out.println("Ошибка ввода!");
            System.out.println("Введите: 1 - для ввода с консоли; 2 - для чтения файла");
            num = inConsole.nextInt();
        }

        if(num == 1) {
            System.out.println("Укажите размерносить матрицы: ");
            size = inConsole.nextInt();

            if (size == 1)
                System.out.println("Размерность СЛАУ не может быть равна одному");
            else if (size == 2) {
                System.out.println("Формат ввода: 'a11 a12 b1'");
                System.out.println("Введите коффициенты через пробел:");
            } else {
                System.out.println("Формат ввода: 'a11 ... a1" + size + " b1'");
                System.out.println("Введите коффициенты через пробел:");
            }

            try {
                for (int i = 0; i < size * size + size; i++)
                    arrayList.add(inConsole.nextDouble());
            } catch (InputMismatchException e) {
                System.out.println("Ошибка ввода!  Проверьте, что дробные числа записаны через запятую");
                System.exit(0);
            }
        }
        if(num == 2) {
            try {
                FileInputStream path = new FileInputStream("res/input");
                DataInputStream inFile = new DataInputStream(path);
                BufferedReader br = new BufferedReader(new InputStreamReader(inFile));
                String data;

                while ((data = br.readLine()) != null) {
                    String[] tmp = data.split(" ");    //Split space
                    for (String s : tmp)
                        arrayList.add(Double.parseDouble(s));
                    size++;
                }
            } catch (NumberFormatException e) {
                System.out.println("Ошибка ввода!  Проверьте, что дробные числа записаны через точку");
                System.exit(0);
            }
            System.out.println("Размерность матрицы: ");
            System.out.println(size);
            System.out.println();
        }


        System.out.println("Введите требуемую погрешность eps (критерий по абсолютным отклонениям): ");
        try {
            eps = inConsole.nextDouble();
        } catch (Exception e) {
            System.out.println("Проверьте введенные данные, разделителем должна быть запятая");
            System.exit(0);
        }

        double[][] mtx = new double[size][size+1];
        int index = 0;
        for(int i = 0; i< size; i++)
            for(int j = 0; j <size+1;j++)
            {
                mtx[i][j] = mtx[i][j] = arrayList.get(index);
                index++;
            }

        System.out.println("Исходная матрица:");
        IterativeMethod.printMtx(mtx);
        System.out.println("----------------------------------");
        System.out.println("Проверка матрицы на диагональное преобладание:\n"
                + (IterativeMethod.checkIfDiagonalPredominant(mtx) ? "Матрица имеет диагональное преобладание" : "Диагональное преобладание отсутствует"));
        if(!IterativeMethod.checkIfDiagonalPredominant(mtx)) {
            mtx = IterativeMethod.tryToConvertToDiagonalPredominant(mtx);
            if(mtx == null) {
                System.out.println("Диагональное преобладание не может быть достигнуто, метод может расходиться.");
                System.exit(0);
            }
            System.out.println("Удалось достичь диагональное преобладание путем перестановок.\nНовая матрица:");
            IterativeMethod.printMtx(mtx);
        }

        System.out.println("----------------------------------");
        System.out.println("Получаем матрицу с коэффициентами c_ij, d_i: ");
        mtx = IterativeMethod.transformMatrixFromABToCD(mtx);
        IterativeMethod.printMtx(mtx);
        System.out.println("----------------------------------");
        IterativeMethod.doIterations(mtx, eps);

    }
}