# Autenticação e Segurança

⬆️ [Voltar para o Readme principal ](../../README.md)

## Sumário

- [Autenticação](#autenticação)
- [Segurança](#segurança)

## Autenticação

- O arquivo `auth.py` contém as funções para autenticar e gerar tokens JWT
  - `verify_token`: Verifica se o token é válido e retorna o payload do token
  - `create_token`: Gera um token JWT com base no ID do usuário
- O token é gerado com base no ID do usuário
- O token é válido por um período de tempo definido — Inicialmente definido para expirar em 1 hora.

## Segurança

- O arquivo `security.py` contém as funções para gerar e verificar hash de senhas
  - `hash_password`: Gera um hash bcrypt para uma senha
  - `verify_password`: Verifica se a senha informada é igual ao hash armazenado

