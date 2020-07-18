## intent:greet
- olá
- bom dia
- boa tarde
- boa noite
- oi
- oie
- ooi
- oooi
- oii
- hello
- hi

## intent:goodbye
- até mais
- adeus
- beijo
- beijos
- abraço

## intent:order
- Eu quero um [BigMc](dishes)
- Gostaria de dois [Quarteirões](dishes)
- Por favor, gostaria um [Mc Chicken](dishes)
- Me veja 1 [Big Mac](dishes)
- Quero um [BigMc](dishes)
- quero [coca cola](drinks)

## intent:request_bill
- gostaria da conta
- poderia me trazer a conta
- quero pagar
- pode mandar a conta
- quero fechar a conta

## intent:affirm
- confirmado
- isso mesmo
- sim
- está certo
- está correto
- sim sim

## intent:deny
- errado
- não, obrigado
- não está certo
- negado
- negativo
- não confirmo
- não é isso
- Não

## intent:thankyou
- muito obrigado
- valeu
- valeeu
- obg
- brigado

## lookup:dishes.txt
  data/lookup_tables/dishes.txt

## lookup:drinks.txt
  data/lookup_tables/drinks.txt

## regex:greet
- [o]+[i]+e?\s

## synonym:Big Mac
- BigMc
- BigMec
- Big Mc
- BigMac