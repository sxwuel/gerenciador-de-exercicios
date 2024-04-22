# Gerenciador de Exercícios
Permite criar diretórios com arquivos padronizados com uma maior facilidade.  
Está configurado para exercícios da plataforma [Neps Academy](https://neps.academy/br)<br>
## Requisitos
> - Python 3 <br>
## Instalação
> Execute os seguintes comandos em terminal no diretório de seus exercícios
```bash
git clone https://github.com/sxwuel/gerenciador-de-exercicios
```
## Como usar
No terminal, navegue à pasta do gerenciador.
O gerenciador tem 2 comandos: criar e acessar.  
### criar
O comando criar vai solicitar a competição, modalidade, fase, nome do exercício e o ID neps.  
Logo após será criado um diretório para esse exercício e o arquivo **ir.bat** poderá ser executado movendo seu terminal ao diretório criado.  
```cmd
gerente.py criar
ir
```
### acessar
O comando acessar [id] edita o arquivo **ir.bat** para navegar até o diretório associado a esse id.  
```cmd
gerenciador.py acessar [id]
ir
```
