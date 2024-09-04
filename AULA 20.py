# AULA 20 -  Projeto Final

Conformidade com Requisitos
Avaliação de Usabilidade
Verificação de Necessidades do Negócio

1. Conformidade com Requisitos:
    - Esse conceito diz respeito à garantia de que o software desenvolvido atende a todos os requisitos funcionais e não funcionais estabelecidos durante a fase de análise e definição de requisitos. Isso envolve uma verificação detalhada para garantir que todas as funcionalidades especificadas estejam implementadas corretamente e que o sistema atenda aos critérios de desempenho, segurança e usabilidade estabelecidos.
2. Avaliação de Usabilidade:
    - A usabilidade refere-se à facilidade com que os usuários podem interagir com o software para realizar suas tarefas de forma eficiente, eficaz e satisfatória. A avaliação de usabilidade envolve testar o software com usuários reais ou representativos para identificar problemas de usabilidade, como interfaces confusas, fluxos de trabalho complexos ou falta de feedback adequado. O objetivo é garantir que o software seja intuitivo e fácil de usar, aumentando a satisfação do usuário e a produtividade.
3. Verificação de Necessidades do Negócio:
    - Este conceito envolve garantir que o software atenda aos objetivos e necessidades de negócio do cliente. Isso inclui verificar se o software oferece as funcionalidades necessárias para apoiar os processos de negócio do cliente, se ele fornece os dados e relatórios necessários para tomada de decisões e se está alinhado com a estratégia global da organização. A verificação das necessidades de negócio é essencial para garantir que o software agregue valor real ao cliente e à organização.

Em resumo, a conformidade com requisitos garante que o software atenda aos requisitos estabelecidos, a avaliação de usabilidade garante uma experiência positiva para o usuário final e a verificação das necessidades do negócio garante que o software atenda aos objetivos e necessidades da organização cliente. Todos esses conceitos são essenciais para o sucesso de um projeto de desenvolvimento de software.

Para aplicar os conceitos de conformidade com requisitos, avaliação de usabilidade e verificação das necessidades do negócio em um projeto Python, você pode seguir várias abordagens e usar diferentes bibliotecas e frameworks disponíveis na comunidade Python. 

Segue algumas opções:

1. Conformidade com Requisitos:
    - Use testes unitários e de integração para garantir que o código Python implemente corretamente os requisitos funcionais e não funcionais. Você pode usar a biblioteca `unittest` da biblioteca padrão do Python ou optar por frameworks de teste mais avançados, como `pytest`, para escrever testes que verifiquem se o software está funcionando conforme esperado.
2. Avaliação de Usabilidade:
    - Integre testes de usabilidade no ciclo de desenvolvimento, realizando sessões de teste com usuários reais ou representativos. Você pode usar bibliotecas Python como `Selenium` ou `PyAutoGUI` para automatizar testes de interface do usuário (UI) e conduzir testes de usabilidade de forma mais eficiente. Além disso, ferramentas de análise de UX, como `Hotjar` ou `Google Analytics`, podem ser úteis para coletar dados de uso e feedback dos usuários.
3. Verificação de Necessidades do Negócio:
    - Mantenha uma comunicação próxima com os stakeholders do projeto para entender e validar continuamente as necessidades do negócio. Utilize métodos ágeis, como revisões de sprint e reuniões de planejamento, para garantir que o desenvolvimento do software esteja alinhado com os objetivos e requisitos do cliente. Bibliotecas como `Django` ou `Flask` podem ser usadas para desenvolver aplicativos web que suportem processos de negócio específicos.

Além disso, você pode considerar a utilização de ferramentas de gerenciamento de projetos, como `Jira` ou `Trello`, para rastrear requisitos, tarefas e feedback dos usuários ao longo do ciclo de desenvolvimento. Integrar essas ferramentas com o processo de desenvolvimento pode ajudar a garantir que todos os aspectos do projeto estejam alinhados com os conceitos de conformidade com requisitos, usabilidade e necessidades do negócio.

Em suma, trazer esses conceitos para o desenvolvimento em Python envolve a adoção de práticas de desenvolvimento ágil, a integração de testes automatizados e a colaboração próxima com os stakeholders do projeto para garantir que o software atenda às necessidades e expectativas do cliente e dos usuários finais.

Projeto:

- Crie um repositório no github com o nome projeto_final

deixe publico e aplique um README

- Acesse o JIRA

      insira nos quadros o projeto final:

Utilizar a interface TKinter

1 - Criar uma Janela de 500x500

2 - Crie 2 inputs para digitar 2 números 

3 - Crie 4 botões com as 1 operações da IMC

4 - Crie um label para mostrar o resultado

5 - Crie a função para calcular

[Calculadora ](https://www.notion.so/Calculadora-5b044e0912db4cd984aee27018f19d1c?pvs=21)

[grid layout - TKinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)

Suba o projeto para o Github e envie neste e-mail:

 

[baetrizalves71@gmail.com](mailto:baetrizalves71@gmail.com)

**Desejo a você muito sucesso na Jornada!**

Tenha em mente que estamos aqui para isso para resolver problemas, essa área possui muitas oportunidades. Mas uma das principais habilidades do desenvolvedor e correr atrás das resoluções, não se contente com o erro. 

Crie novos caminhos e mantenha-se em evolução.

Ajuste o linkedin e o Github de acordo com o seu objetivo.

Por mais que você possua uma carreira alinhada com outro contexto, seu Linkedin precisa estar de acordo com o seu objetivo, para não gerar ruídos no momento da contratação.

Não pare neste curso pois ,ele é introdutório, faça um curso técnico ou uma faculdade.

Tire certificações, para validar seu conhecimento.

Não pare no primeiro obstáculo! Sucesso!  

[Acesse Kahoot](https://kahoot.it/)






-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# GUI 
import tkinter as tk

janela  =  tk.Tk()
# janela.geometry('500x500')
janela.title('Isso é uma Janela')

def soma():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    soma  =  n1  + n2
    resultado.config(text=f'Resultado {int(soma)}')


def sub():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    sub  =  n1  - n2
    resultado.config(text=f'Resultado {int(sub)}')

def div():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    div  =  n1  // n2
    resultado.config(text=f'Resultado {div}')

def mult():
    n1 = float(input_entry1.get())
    n2 = float(input_entry2.get())
    mult  =  n1  * n2
    resultado.config(text=f'Resultado {mult}')


text_label =  tk.Label(janela, text='CALCULADORA', fg = 'black', bg='white')
text_label.grid(row = 0, column = 1)
# text_label.pack()


input_entry1 = tk.Entry(janela, width = 5)
input_entry1.grid(row = 2, column = 2 , padx = 10)
# input_entry1.pack()

input_entry2 = tk.Entry(janela, width = 5)
input_entry2.grid(row = 2, column = 4, padx = 10 )
# input_entry2.pack()


btn_soma  = tk.Button(janela, text= '+', command = soma, fg='white', bg='black')
btn_soma.grid(row = 3, column = 3, padx = 10, pady=10)
# btn_soma.pack()  

btn_sub  = tk.Button(janela, text= '-', command = sub, fg='white', bg='black')
btn_sub.grid(row = 3, column = 2, padx = 10, pady=10)
# btn_sub.pack()  

btn_div  = tk.Button(janela, text= '/', command = div, fg='white', bg='black')
btn_div.grid(row = 3, column = 4, padx = 10, pady=10)
# btn_div.pack()  

btn_mult  = tk.Button(janela, text= '*', command = mult, fg='white', bg='black')
btn_mult.grid(row = 3, column = 5, padx = 10, pady=10)
# btn_mult.pack()  

resultado =  tk.Label(janela, text='Resultado')
resultado.grid(row = 2, column = 6, padx = 5, pady=5)
# resultado.pack()

janela.mainloop()
