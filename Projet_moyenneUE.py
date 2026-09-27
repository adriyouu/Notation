def calculU1():
    
    somme_points = 0
    somme_coefficients = 0

    for i in range(101, 103):
        note = float(input(f"Quelle est votre moyenne R{i} pour UE1 ? "))
        coefficient = int(input(f"Quel est le coefficient associé à R{i} : "))

        somme_points += note * coefficient
        somme_coefficients += coefficient

    for i in range(11, 13):
        note = float(input(f"Quelle est votre moyenne SAE{i} ? "))
        coefficient = int(input(f"Quel est le coefficient associé à SAE{i} : "))

        somme_points += note * coefficient
        somme_coefficients += coefficient

    moyenneU1 = somme_points / somme_coefficients

    print("Votre moyenne pour UE1 est", moyenneU1)


   
    somme_pointsU2 = 0
    somme_coefficientsU2 = 0

    for i in range(101, 103):
        noteU2 = float(input(f"Quelle est votre moyenne R{i} pour UE2 ? "))
        coefficientU2 = int(input(f"Quel est le coefficient associé à R{i} : "))

        somme_pointsU2 += noteU2 * coefficientU2
        somme_coefficientsU2 += coefficientU2

    for i in range(11, 13):
        noteU2 = float(input(f"Quelle est votre moyenne SAE{i} ? "))
        coefficientU2 = int(input(f"Quel est le coefficient associé à SAE{i} : "))

        somme_pointsU2 += noteU2 * coefficientU2
        somme_coefficientsU2 += coefficientU2

    moyenneU2 = somme_pointsU2 / somme_coefficientsU2

    print("Votre moyenne pour UE2 est", moyenneU2)


   
    somme_pointsU3 = 0
    somme_coefficientsU3 = 0

    for i in range(101, 103):
        noteU3 = float(input(f"Quelle est votre moyenne R{i} pour UE3 ? "))
        coefficientU3 = int(input(f"Quel est le coefficient associé à R{i} : "))

        somme_pointsU3 += noteU3 * coefficientU3
        somme_coefficientsU3 += coefficientU3

    for i in range(11, 13):
        noteU3 = float(input(f"Quelle est votre moyenne SAE{i} ? "))
        coefficientU3 = int(input(f"Quel est le coefficient associé à SAE{i} : "))

        somme_pointsU3 += noteU3 * coefficientU3
        somme_coefficientsU3 += coefficientU3

    moyenneU3 = somme_pointsU3 / somme_coefficientsU3

    print("Votre moyenne pour UE3 est", moyenneU3)


    
    moyenneGlobal = (moyenneU1 + moyenneU2 + moyenneU3) / 3

    print("Votre moyenne globale est", moyenneGlobal)
    
    if moyenneGlobal >= 10:
        print("Vous passez en BUT 2")
        
         

calculU1()