/* Faits : Déclaration des élèves et de leurs notes */
note(kevin, math, 85).
note(kevin, anglais, 90).
note(jane, math, 92).
note(jane, anglais, 88).
note(bob, math, 78).
note(bob, anglais, 85).


/* Règle : Calcul de la moyenne des notes d'un élève */
moyenne(Eleve, Moyenne) :-
  findall(Note, note(Eleve, _, Note), Notes),
  length(Notes, N),
  somme_liste(Notes, Sum),
  Moyenne is Sum / N.

/* Prédicat auxiliaire : Calcul de la somme d'une liste */
somme_liste([], 0).
somme_liste([X|Xs], Sum) :-
  somme_liste(Xs, Reste),
  Sum is X + Reste.

/* Règle : Affichage des élèves avec leur moyenne */
afficher_moyennes :-
  setof(Eleve, Matiere^Note^(note(Eleve, Matiere, Note)), Eleves),
  member(Eleve, Eleves),
  moyenne(Eleve, Moyenne),
  format('Élève: ~w, Moyenne: ~2f~n', [Eleve, Moyenne]),
  fail.

afficher_moyennes.

