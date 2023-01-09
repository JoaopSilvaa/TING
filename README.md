
# Boas vindas ao TING!

# O que é o TING?

É um programa que simula um algoritmo de indexação de documentos similar ao do Google, sendo capaz de identificar ocorrências de termos em arquivos TXT.

Para isso, o programa desenvolvido contém dois módulos:

Módulo de gerenciamento de arquivos que permite anexar arquivos de texto (formato TXT) e;
Módulo de buscas que permite operar funções de busca sobre os arquivos anexados.

## Técnologias usadas

> Desenvolvido usando: Python.

## Executando a aplicação

1. Clone o repositório
- Utilize o comando: `git clone git@github.com:JoaopSilvaa/Tech-News.git`<br />
2. Acesse a pasta do projeto
- Acesse a pasta Tech-News com `cd Tech-News`;<br />
3. Crie uma nova branch a partir da main
 - Verifique se você está na branch `main`
   * Exemplo: `git branch`
 - Se não estiver, mude para a branch `main`
   * Exemplo: `git checkout main`
 - Crie a branch
    * Exemplo: `git checkout -b joaozinho-tech-news`<br />
4. Instale as dependências gerais do projeto 

  - O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  i. **criar o ambiente virtual**

  ```bash
python3 -m venv .venv
  ```

  ii. **ativar o ambiente virtual**

  ```bash
source .venv/bin/activate
  ```

  iii. **instalar as dependências no ambiente virtual**

  ```bash
python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.

<br><br>
Este projeto foi desenvolvido por [João Antônio](https://www.linkedin.com/in/joaoantoniosilvaa/) durante o curso de Desenvolvimento de Software na [Trybe](https://www.betrybe.com/) 
