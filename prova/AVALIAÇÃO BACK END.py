def classificar_nota(nota):
    if nota >= 9.0:
        return "A - Excelente!"
    elif nota >= 7.0:
        return "B - Muito bom"
    elif nota >= 5.0:
        return "C - Aprovado"
    elif nota >= 3.0:
        return "D - Recuperação"
    else:
        return "F - Reprovado"

print("Classificador de notas - Avaliação Back-end\n")

try:
    nota = float(input("Digite a nota (0 a 10): "))
    
    if nota < 0 or nota > 10:
        print("Erro: a nota deve estar entre 0 e 10.")
    else:
        resultado = classificar_nota(nota)
        print(f"\nNota: {nota:.1f} → {resultado}")
        
except ValueError:
    print("Erro: por favor digite um número válido.")