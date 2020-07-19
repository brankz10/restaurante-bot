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
- tchau

## intent:order
- Eu quero um [BigMc](dish)
- Gostaria de dois [Quarteirões](dish)
- Por favor, gostaria um [Mc Chicken](dish)
- Me veja 1 [Big Mac](dish)
- Quero um [BigMc](dish)
- quero [coca cola](drink)
- quero um [bigmc]{"entity": "dish", "value": "Big Mac"}
- quero uma [coca cola]{"entity": "drink", "value": "COCA COLA"}
- quero um [coca cola]{"entity": "drink", "value": "COCA COLA"}
- Quero uma [coca]{"entity": "drink", "value": "COCA COLA"} cola bem gelada

## intent:request_bill
- gostaria da conta
- poderia me trazer a conta
- quero pagar
- pode mandar a conta
- quero fechar a conta
- quero a conta

## intent:affirm
- confirmado
- isso mesmo
- sim
- está certo
- está correto
- sim sim
- sim!

## intent:deny
- errado
- não, obrigado
- não está certo
- negado
- negativo
- não confirmo
- não é isso
- Não
- nao

## intent:thankyou
- muito obrigado
- valeu
- valeeu
- obg
- brigado
- obrigado

## intent:just_that
- só isso mesmo
- por enquanto é isso

## synonym:Big Mac
- bigmc
- BigMc
- BigMec
- Big Mc
- BigMac

## synonym:COCA COLA
- coca cola
- coca-cola
- coca

## regex:greet
- [o]+[i]+e?\s
