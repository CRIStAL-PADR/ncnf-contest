# ncnf-contest
Concours NcNf (Ni Chaud - Ni Froid) - concours d'optimisation thermique pour l'exploitation de bâtiment. 

Sujet:
------

Réaliser un modèle de bâtiment permettant via une simulation dynamique de faire des projections de température au niveau de différentes sondes et des apports énergétique lié au chauffage. 

Le modèle doit pouvoir être simulé à différent pas de temps.

Evaluation:
-----------

Chaque dataset d'un bâtiment correspondra à un "run", à chaque run, le modèle sera initialisé avec les d1 (données publique), et d2 (données privée). La norme entre la différence entre la projection et la valeur connue sera utilisé comme score_s1 de la méthode. 

Certains datasets correspondent à des bâtiment qui seront connu des participant, 
D'autres datasets correspondront à des données de bâtiment non connus avant le challenge. 

Les méthodes seront classée en fonction de leur score. 

Description fichiers de données:
--------------------------------

Chaque fichier du répertoire dataset correspond à un bâtiment réel. 
Les fichiers, au format csv ou json/records, contiendront les champs suivants:
Date, Te, Ti, Ph, 

Lorsqu'il y a plusieurs mesures pour un bâtiment on utilisera la notation suivante:
Te1, Te2, Te3 pour indiquer les différents capteurs d'une même zone. 

Lorsqu'il y a plusieurs zones dans le bâtiment on utilisera la notation:
Te1_1, Te1_2 indiquer les premiers capteurs des zones 1 et 2.





 
