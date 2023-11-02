# Prática TDD

Desafio técnico para os alunos da disciplina "Desenvolvimento Web 3" e "Qualidade e Teste de Software"


[O que eu devo fazer ?](https://youtu.be/ywayPV7Y648)

No ambiente Linux:

```console
git clone https://github.com/orlandosaraivajr/Pratica_TDD_1.git
cd Pratica_TDD_1/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd biblioteca/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py runserver
```

No ambiente Windows:

```console
git clone https://github.com/orlandosaraivajr/Pratica_TDD_1.git
cd Pratica_TDD_1/
virtualenv venv
cd venv
cd scripts
activate.bat
cd ..
cd ..
pip install -r requirements.txt
cd biblioteca/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py runserver

```

### Requisitos da Sprint 1

O projeto apresenta um cadastro de livros. Na rota raiz (/), se apresenta dois botões, conforme imagem abaixo:
<img src="img/rota_raiz.png">

Ao acessar a rota cadastro (/cadastro), é possível cadastrar o livro, que armazena as seguintes informações:

- Título
- Editora

<img src="img/rota_cadastro.png">

Ao acessar a rota listar (/listar), é possível verificar os livros cadastrados:

<img src="img/rota_listar.png">

Todos os testes unitários estão passando, e o sistema funciona como previsto para a primeira sprint.

![image](https://github.com/tbgbarros/Pratica_TDD_1---ThiagoBarros/assets/111811766/2deb7917-7569-49e9-b816-268a115ae227)


### Requisitos para a Sprint 2

Aqui começa seu desafio. Você deve implementar as seguintes melhorias:

#### Novos campos
O cliente deseja armazenar os novos campos referente a livros:

:heavy_check_mark:[x] Autor
+:heavy_check_mark:[x] ISBN
+:heavy_check_mark:[x] Número de Páginas
+:heavy_check_mark:[x] Ano em que a obra foi escrita

#### Validação dos campos

O cliente deseja validar os campos com as seguintes regras:

+ :heavy_check_mark:[x] Título:  Validar a string para cadastro com pelo menos 3 caracteres. Atualmente, espera-se ter pelo menos 10 caracteres.

+ :heavy_check_mark:[x] Editora: Validar a string para cadastro com pelo menos 3 caracteres.
Atualmente, espera-se ter pelo menos 10 caracteres.

+ :heavy_check_mark:[x] Autor: Validar a string para cadastro com pelo menos 10 caracteres.

+ :heavy_check_mark:[x] ISBN: Validar a string para cadastro com exatos 13 caracteres e todos numéricos.

+ :heavy_check_mark:[x] Número de Páginas: Validar a string para cadastro entre 1 e 3 caracteres e todos numéricos.

+ :heavy_check_mark:[x] Ano: : Validar a string para cadastro com exatos 4 caracteres e todos numéricos. 

 + :heavy_check_mark:[x] Além disso, na sprint 1, os campos Título e editora são obrigatórios. Nesta sprint, os novos campos serão obrigatórios também.

#### Ajustes nos testes

 :heavy_check_mark:[x] O código fonte passará por atualizações para acomodar estes novos requisitos. Com isso, você deve ajudar os testes existentes e, caso julgue pertinente, criar novos testes.

:heavy_check_mark:[x] Você recebeu a sprint 1 com uma cobertura de teste acima de 90%.

![image](https://github.com/tbgbarros/Pratica_TDD_1---ThiagoBarros/assets/111811766/33c13144-2734-45c3-a3a9-a3f662d9b4d7)
