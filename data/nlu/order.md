## intent:greet
- olá
- ola
- eaeee
- eaew
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
- Olá

## intent:goodbye
- até mais
- adeus
- beijo
- beijos
- abraço
- tchau

## intent:order
- Eu quero um [BigMc]{"entity": "dish", "value": "BIG MAC"}
- Eu quero um [cheeseburger]{"entity": "dish", "value": "CHEESEBURGER"}
- Gostaria de dois [Quarteirões]{"entity": "dish", "value": "QUARTERAO"}
- Por favor, gostaria um [Mc Chicken]{"entity": "dish", "value": "MC CHICKEN"}
- Me veja 1 [BIG MAC](dish)
- Quero um [BigMc]{"entity": "dish", "value": "BIG MAC"}
- quero [coca cola]{"entity": "dish", "value": "COCA COLA"}
- quero um [bigmc]{"entity": "dish", "value": "BIG MAC"}
- quero uma [coca cola]{"entity": "dish", "value": "COCA COLA"}
- quero um [coca cola]{"entity": "dish", "value": "COCA COLA"}
- Quero uma [coca cola]{"entity": "dish", "value": "COCA COLA"} [bem gelada](note)
- Quero um [duplo salada]{"entity": "dish", "value": "DUPLO SALADA"} e uma [fanta laranja]{"entity": "dish", "value": "FANTA LARANJA"} [sem gelo](note)
- quero um [cheeseburger]{"entity": "dish", "value": "CHEESEBURGER"}
- já sei, quero um [cheddar mcmelt]{"entity": "dish", "value": "CHEDDAR MCMELT"}
- quero um [coca]{"entity": "dish", "value": "COCA COLA"} [sem gelo](note) também
- quero um [mc chicken]{"entity": "dish", "value": "MC CHICKEN"}
- oi, quero um [duplo quarterão]{"entity": "dish", "value": "DUPLO QUARTERAO"}

## intent:inform
- um apenas
- dois

## intent:request_bill
- gostaria da conta
- poderia me trazer a conta
- quero pagar
- pode mandar a conta
- quero fechar a conta
- quero a conta
- por favor, eu já quero pagar

## intent:affirm
- confirmado
- isso mesmo
- sim
- está certo
- está correto
- sim sim
- sim!
- ss
- s

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
- n
- Não não

## intent:thankyou
- muito obrigado
- valeu
- valeeu
- obg
- brigado
- obrigado
- muito obrigado!!!

## intent:just_that
- só isso mesmo
- por enquanto é isso
- apenas isso

## intent:note
- quero [sem maionese](note)
- sim, [com muito cheddar](note)
- quero ela [com uma rodela de limão](note)
- sim, quero [sem queijo](note)
- quero que [tire o picles](note)

## synonym:BIG MAC
- BigMc
- bigmc
- BigMec
- Big Mc
- BigMac

## synonym:CHEDDAR MCMELT
- cheddar mcmelt

## synonym:CHEESEBURGER
- cheeseburger

## synonym:COCA COLA
- coca cola
- coca
- coca-cola

## synonym:DUPLO SALADA
- duplo salada

## synonym:FANTA LARANJA
- fanta laranja

## synonym:MC CHICKEN
- Mc Chicken
- mc chicken

## synonym:QUARTERAO
- Quarteirões

## regex:greet
- [o]+[i]+e?\s

## regex:laugh
- [ha][ha]+
- kk+

## lookup:dish
  data/lookup_tables/dish.txt
