while True:      # les phrases qui sont devant le hashtag sont juste des commentaires , while = tanque ca est vrai :
    print("veuillez entrer un nombre entier positif entre [1;9999] :")  # ecrire("message")
    nbr = int(input())                                                  # lire : int pour entrer un nombre entier positif, et input() pour demander a l'utilisateur d'entrer le nombre

    if nbr > 0 and (nbr <10000) :       # la on a limiter a 4 chiffre, si nbr support la condition on continue, sinon echec (voir la fin du code)
        Q = nbr // 10                   # Q pour le quotion, // = div dans l'algorithme
        R = nbr % 10                    # R pour le reste  ,  % = mod dans l'algorithme
        print("le chiffre des unites est:", R)

        if Q > 0 :
            nbr = Q
            Q = nbr // 10
            R = nbr % 10
            print("le chiffre des dizaines est:", R)

            if Q > 0 :
                nbr = Q
                Q = nbr // 10
                R = nbr % 10
                print("le chiffre des centaines est:", R)

                if Q > 0 :
                    nbr = Q
                    Q = nbr // 10
                    R = nbr % 10
                    print("le chiffre des milliers est:", R)
                    print("Fin de programme")
        break # ca veut dire stop, et relence le programme si ce cas est choisis

    else :
        print("echec !")
