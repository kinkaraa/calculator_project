print("===============================")
print("KALKULATOR MINI")
print("===============================")

while True:
    try: 
        a = float(input("MASUKKAN ANGKA PERTAMA: "))
        operation = input("MAU OPERASI APA? (: / x / + / - ): ")
        b = float(input("MASUKKAN ANGKA KEDUA: "))
   
        if operation == ":":
            c = a / b 
            print("%.1f / %.1f = %.1f" % (a, b, c))
        elif operation.lower() == "x":
            c = a * b
            print("%.1f * %.1f = %.1f" % (a, b, c))
        elif operation == "+":
            c = a + b
            print("%.1f + %.1f = %.1f" % (a, b, c))
        elif operation == "-":
            c = a - b
            print("%.1f - %.1f = %.1f" % (a, b, c))
        
        else:
            continue 
    
    except ValueError:
        print("INPUT HARUS ANGKA!")
        continue  
    except ZeroDivisionError:
        print("PEMBAGIAN DENGAN NOL TIDAK DAPAT DILAKUKAN!")
        continue  
        
    again = input("APAKAH ANDA INGIN MELAKUKAN OPERASI LAGI? (yes/no): ")
    if again.lower() != 'yes':
        print("OPERASI SELESAI")
        break
