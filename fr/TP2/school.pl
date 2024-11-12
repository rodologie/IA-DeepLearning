% Faits
eleve(dupont, jean, 2000-01-15).
eleve(martin, sophie, 1999-05-23).
eleve(durand, paul, 2001-07-30).

groupe_projet(dupont, groupe1).
groupe_projet(martin, groupe1).
groupe_projet(durand, groupe2).

note(dupont, math, 15).
note(dupont, physique, 12).
note(martin, math, 14).
note(martin, physique, 16).
note(durand, math, 10).
note(durand, physique, 11).

module(math, mathematiques).
module(physique, physique).

% Règles
eleves_groupe(Groupe, Eleves) :-
    findall(Eleve, groupe_projet(Eleve, Groupe), Eleves).


moyenne_notes(Eleve, Module, Moyenne) :-
    eleve(Eleve, _, _),
    findall(Note, note(Eleve, Module, Note), Notes),
    sum_list(Notes, Somme),
    length(Notes, Nombre),
    Nombre > 0,
    Moyenne is Somme / Nombre.


modules_suivis(Eleve, Modules) :-
    findall(Module, note(Eleve, Module, _), Modules).