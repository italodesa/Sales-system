# Sales system

<aside>
📌

**Objetivo**

Criar um sistema simples de venda de produtos, com cadastro e comercialização, separando permissões por perfil.

</aside>

## Tecnologias usadas

- Backend será desenvolvido em **Python**.

## Visão geral

O **Sales system** é um sistema interno para **gestão de produtos** e **registro de vendas**.

### Perfis de usuário

- **Admin**
    - Cadastra, edita e inativa produtos.
    - Criar usuarios
- **Vendedor**
    - Consulta o catálogo de produtos.
    - Registra vendas.

## Escopo (MVP)

### Funcionalidades principais

1. **Autenticação e perfis**
    - Login.
    - Controle de acesso por perfil (Admin e Vendedor).
2. **Produtos (Admin)**
    - Cadastrar produto.
    - Editar produto.
    - Criar usuarios
    - Listar e buscar produtos.
    - Inativar produto (em vez de excluir).
3. **Vendas (Vendedor)**
    - Registrar venda com itens e quantidades.
    - Calcular total.

### Fora do escopo (por enquanto)

- Integração com meios de pagamento.
- Controle de estoque avançado (entradas, inventário, etc.).
- Emissão de nota fiscal.
- Multi-loja ou multi-filial.

---

## Requisitos funcionais

### RF-01 — Login

- O sistema deve permitir que um usuário autentique com nome e senha.

### RF-02 — Permissões por perfil

- O sistema deve impedir que **Vendedor** cadastre ou edite produtos.

### RF-03 — Cadastro de produtos (Admin)

- O Admin deve poder cadastrar um produto com:
    - Nome
    - Preço
    - Status (Ativo ou Inativo)
    - quantidade

### RF-04 — Registro de vendas (Vendedor)

- O Vendedor deve poder criar uma venda contendo:
    - Data e hora
    - Itens (produto, quantidade, preço unitário no momento da venda)
    - Total calculado

---

## Requisitos não funcionais

- **RNF-01 (Auditoria):** registrar quem criou vendas.
- **RNF-02 (Usabilidade):** fluxo de venda deve ser rápido, com busca de produto.
- **RNF-03 (Desempenho):** listagens devem paginar.

---

## Regras de negócio

- **RB-01:** produto inativo não pode ser vendido.
- **RB-02:** preço unitário deve ser “congelado” na venda (não muda se o produto mudar depois).
- **RB-03:** uma venda deve ter pelo menos 1 item.
- **RB-04:** quantidade mínima por item é 1.

---

## Modelo de dados (proposta)

### Entidades

- **Usuário**
    - id
    - nome
    - senha
    - perfil (ADMIN, VENDEDOR)
- **Produto**
    - id
    - nome
    - preco
    - status (ATIVO, INATIVO)
- **Venda**
    - id
    - vendedorId (userId)
    - total
    - criadoEm
- **ItemVenda**
    - produtoId
    - nome
    - quantidade
    - preço
---

## Telas (MVP)

- Login
- Produtos
    - Listagem e busca
    - Cadastro/Edição (apenas Admin)
- Vendas
    - Nova venda (apenas Vendedor)

## Fluxos principais

### Fluxo: cadastrar produto (Admin)

1. Admin faz login.
2. Acessa Produtos.
3. Clica em “Novo produto”.
4. Preenche dados e salva.

### Fluxo: registrar venda (Vendedor)

1. Vendedor faz login.
2. Acessa Vendas → “Nova venda”.
3. Busca e adiciona produtos com quantidades.
4. Confere total.
5. Confirma a venda.

---

## Critérios de aceitação (resumo)

- Admin consegue cadastrar e editar produtos.
- Vendedor não consegue acessar telas/ações de cadastro de produtos.
- Vendedor consegue registrar uma venda com 1 ou mais itens.
- O total é calculado corretamente.