# Sistema de Estacionamento

Este é um projeto inicial de um sistema de estacionamento, desenvolvido utilizando o framework Django. O sistema permite gerenciar vagas de estacionamento e acessar funcionalidades diferenciadas para clientes VIP e comuns.

## Funcionalidades
- **Login de Clientes:** Clientes comuns e VIP possuem credenciais diferentes, e o sistema redireciona para páginas específicas dependendo do tipo de cliente.
- **Gerenciamento de Vagas:** O sistema inicia com 10 vagas, com os seguintes estados:
  - Vaga 1: Ocupada
  - Vaga 2: Ocupada
  - Vaga 4: Reservada
  - Outras vagas: Livres

## Pré-requisitos
- Python
- Django (instalado via pip)

## Configuração e Execução
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Roberto-Utagawa/parking_manager.git>
   cd ./parking_manager
   ```

2. **Instale as dependências do Django:**
   ```bash
   pip install django
   ```

3. **Inicialize o servidor localmente:**
   ```bash
   python3 manage.py runserver
   ```

4. **Acesse o sistema:**
   Abra o navegador e acesse `http://127.0.0.1:8000`.

## Credenciais de Acesso
- **Cliente Comum:**
  - Login: `00000000000` | Senha: `pedro`
  - Login: `22222222222` | Senha: `felipe`
  - Login: `33333333333` | Senha: `augusto`

- **Cliente VIP:**
  - Login: `11111111111` | Senha: `joao`

### Comportamento Pós-Login
- **Clientes VIP:** São redirecionados diretamente para a homepage VIP.
- **Clientes Comuns:** São redirecionados para a homepage comum.



