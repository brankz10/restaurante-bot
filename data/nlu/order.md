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
- Quero uma [coca cola]{"entity": "dish", "value": "COCA COLA"} [bem gelada](observation)
- Quero um [duplo salada]{"entity": "dish", "value": "DUPLO SALADA"} e uma [fanta laranja]{"entity": "dish", "value": "FANTA LARANJA"} [sem gelo](observation)
- quero um [cheeseburger]{"entity": "dish", "value": "CHEESEBURGER"}
- já sei, quero um [cheddar mcmelt]{"entity": "dish", "value": "CHEDDAR MCMELT"}
- um apenas
- quero um [coca]{"entity": "dish", "value": "COCA COLA"} [sem gelo](observation) também
- quero um [mc chicken]{"entity": "dish", "value": "MC CHICKEN"}

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

## intent:observation
- quero [sem maionese](observation)
- sim, [com muito cheddar](observation)
- quero ela [com](observation) uma rodela de limão
- sim, quero [sem queijo](observation)

## intent:chitchat
- foi um prazer te conhecer

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

## synonym:QUARTERAO
- Quarteirões

## regex:greet
- [o]+[i]+e?\s
