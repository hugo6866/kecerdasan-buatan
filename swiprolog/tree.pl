% orangtua (nama orang tua, nama anak, nomor urut)
orangtua(tono,andi,1).
orangtua(tono,agus,2).
orangtua(andi,riri,3).
orangtua(agus,budi,4).
orangtua(susi,budi,5).
orangtua(agus,harto,6).
orangtua(budi,rizki,7).
orangtua(riri,rizki,8).
orangtua(rizki,rara,9).
orangtua(rani,rara,10).
orangtua(andi,rima,11).
orangtua(rima,rodi,12).
orangtua(susi,fariz,13).
orangtua(agus,fariz,14).
orangtua(fariz, lili,15).
orangtua(suci, lili,16).
orangtua(fariz, toni,17).
orangtua(suci, toni,18).
orangtua(rima,rafi,19).

% anak
anak(X,Y) :- orangtua(Y,X,_).

% pasangan
pasangan(X,Y) :- orangtua(X,Z,_), orangtua(Y,Z,_), X \== Y.

% kakak
kakak(X,Y) :- orangtua(Z,X,N), orangtua(Z,Y,M), N < M.

% adik 
adik(X,Y) :- kakak(Y,X).

% pria
pria(agus).
pria(budi).
pria(andi).
pria(rizki).
pria(harto).
pria(fariz).
pria(joko).

% wanita
wanita(riri).
wanita(susi).
wanita(rara).
wanita(rani).
	
% kakek
kakek(X, Z) :- pria(X), orangtua(X, Y, _), orangtua(Y, Z, _).

% nenek
nenek(X, Z) :- wanita(X), orangtua(X, Y, _), orangtua(Y, Z, _).

% buyut
buyut(X, Z) :- orangtua(X,Y,_), kakek(Y,Z).

% pakde
pakde(X, Z) :- pria(X),  kakak(X, Y), orangtua(Y, Z, _).

% bude
bude(X, Z) :- wanita(X),  kakak(X, Y), orangtua(Y, Z, _).

% paklik
paklik(X, Z) :- pria(X),  adik(X, Y), orangtua(Y, Z, _).

% bulik
bulik(X, Z) :- wanita(X),  adik(X, Y), orangtua(Y, Z, _).

% mertua
mertua(X,Y) :- pria(X), orangtua(X,Z,_), pasangan(Z, Y).

% keponakan
keponakan(X,Z) :- anak(X,Y), anak(Z,Y).

% kakak ipar
kakakipar(X,Y) :- pasangan(Y,Z), kakak(X,Z).

% adik ipar
adikipar(X,Y) :- pasangan(Y,Z), adik(X,Z).
