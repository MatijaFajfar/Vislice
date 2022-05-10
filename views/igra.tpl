<!DOCTYPE html>
<html>
<body>

  <h1>Vislice</h1>

Geslo: {{geslo}} <br/>
Nepravilni ugibi: {{nepravilni}} <br/>
  <img src="/img/{{obesenost}}.jpg" alt="obesanje"> <br/>
% if stanje != model.ZMAGA and stanje != model.PORAZ: 
<form action ="" method="post">
    <input name="crka"> <input type="submit" value="Ugibaj" 
<form/>
% elif stanje == model.ZMAGA:
   
   ZMAGA! :D Bi želeli igrati še enkrat?<br/>
   <form action="/igra/" method="post">
    <button type="submit">Nova igra?</button>
  </form>
% elif stanje == model.PORAZ:
    <br> PORAZ! :(<br/>
    Več sreče prihodnjič!<br/>
    Vaše geslo: <b>{{odgovor}}</b> <br/>
    Poskusite ponovno? <br/>
    <form action="/igra/" method="post">
    <button type="submit">Nova igra?</button>
  </form>
%end
</body>

</html>