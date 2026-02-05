# 🌌 Star Wars API – Desafio Técnico

## 📖 Visão Geral

Saudações, Padawans!

Este projeto consiste na construção de uma **API RESTful** baseada no universo de *Star Wars*. A aplicação consome dados públicos da **SWAPI (Star Wars API)** e os disponibiliza de forma organizada, filtrável e escalável, permitindo que usuários explorem informações detalhadas sobre:

* 👤 Personagens
* 🌍 Planetas
* 🚀 Naves
* 🎬 Filmes

A API está **publicada em ambiente de nuvem (Google Cloud Platform)** e pode ser acessada em:

👉 **[https://starwars-api-31263480827.us-central1.run.app/docs](https://starwars-api-31263480827.us-central1.run.app/docs)**

---

## 🎯 Objetivo do Projeto

Construir e disponibilizar uma plataforma backend capaz de:

* Capturar dados da SWAPI
* Normalizar e organizar informações
* Expor endpoints claros e performáticos
* Permitir filtros, ordenações e correlações entre dados
* Demonstrar boas práticas de engenharia de software e computação em nuvem

---

## 🧩 Tecnologias Utilizadas

### Backend

* **Python 3.11**
* **FastAPI** — framework web assíncrono
* **Uvicorn + Gunicorn** — servidor ASGI
* **SQLAlchemy** — ORM
* **Requests / HTTPX** — consumo da SWAPI

### Cloud & Infraestrutura

* **Google Cloud Platform (GCP)**
* **Cloud Run** — containers gerenciados
* **Cloud Build** — build e deploy
* **Docker**

> ⚠️ **Observação importante sobre autenticação**
> A aplicação foi projetada com **estrutura para autenticação JWT**, porém o mecanismo foi **desativado em produção** para garantir **estabilidade no deploy em Cloud Run** dentro do prazo do desafio.
> Todo o código de autenticação permanece versionado no repositório e pode ser facilmente reativado em ambientes futuros (staging/dev).

---

## 🏗️ Arquitetura da Solução

```text
Cliente
   │
   ▼
Cloud Run (FastAPI + Gunicorn)
   │
   ├── Domains
   │     ├── people
   │     ├── planets
   │     ├── starships
   │     └── films
   │
   ├── Services
   │     └── Integração com SWAPI
   │
   └── Database (camada abstrata / ORM)
```

A aplicação segue o princípio de **separação de responsabilidades por domínio**, facilitando manutenção, testes e evolução contínua.

---

## 📂 Estrutura do Projeto

```bash
app/
├── main.py                # Inicialização da aplicação FastAPI
├── domains/
│   ├── people/
│   │   ├── router.py
│   │   └── service.py
│   ├── planets/
│   ├── starships/
│   └── films/
├── database/
│   ├── database.py
│   └── models.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🔗 Endpoints Disponíveis

Todos os endpoints podem ser explorados via Swagger:

👉 `/docs`

---
### 🎯 Abordagem orientada a perguntas

Um dos diferenciais do projeto foi **estruturar os endpoints para responder perguntas reais que um usuário faria**, abstraindo a complexidade da SWAPI.

Exemplos de perguntas atendidas pela API:

- *Quais personagens existem no universo Star Wars?*
- *Quais personagens aparecem em determinado filme?*
- *Quais planetas possuem determinado clima?*
- *Quais filmes fazem parte da saga e quais personagens participam deles?*

### 👤 Personagens (`/people`)

- `GET /people` — lista personagens
- `GET /people?name=luke` — filtro por nome
- `GET /people?gender=male` — filtro por gênero
- `GET /people?birth_date=41.9BBY` — filtro por ano de nascimento

**Diferencial:**
- Normalização de dados vindos da SWAPI
- Filtros combináveis
- Resolução de relacionamentos (planeta de origem, filmes)

### 🌍 Planetas (`/planets`)

- `GET /planets` — lista planetas
- `GET /planets?climate=arid` — filtro por clima
- `GET /planets?terrain=desert` — filtro por terreno
- `GET /planets?terrain=desert` — compara dois ou mais planetas através de seus ids

**Diferencial:**
- Facilita perguntas como *“quais planetas são desérticos?”*

### 🚀 Naves (`/starships`)

- `GET /starships` — lista naves
- `GET /starships?starship_class=Star Destroyer` — filtro por classe
- `GET /starships?manufacturer=Corellian` — filtro por fabricante

**Diferencial:**
- Conversão de valores textuais da SWAPI para tipos comparáveis
- Permite ordenação e comparação entre naves

### 🎬 Filmes (`/films`)

- `GET /films` — lista filmes
- `GET /films/episode-order` — lista a ordem de filmes
- `GET /films/{id}` — detalhes de um filme
- `GET /films/{id}/characters` — personagens presentes no filme
- `GET /films/{id}/starships` — naves presentes no filme
- `GET /films/{id}/planets` — planetas presentes no filme

**Diferencial:**
- Endpoint correlacionado que responde diretamente à pergunta:
  *“Quais personagens participam deste filme?”*

---

## 🔍 Funcionalidades Implementadas

✔ Consumo da SWAPI
✔ Filtros por query params
✔ Organização por domínios
✔ Correlação entre entidades
✔ Deploy em nuvem (GCP)
✔ Documentação automática (Swagger)

---

## 🚧 Principais Dificuldades Encontradas

### 🔹 Integração com Google Cloud Platform

* Configuração do **Cloud Run com containers Docker**
* Ajustes de **porta, memória, timeout e workers ASGI**
* Diagnóstico de falhas de inicialização utilizando **Cloud Logging**
* Garantia de compatibilidade entre **FastAPI, Uvicorn, Gunicorn e Cloud Run**

### 🔹 Integração de Login e Autenticação em Ambiente Cloud

* Implementação inicial de **autenticação JWT**
* Desafios de alinhar autenticação com o ciclo de vida do container
* Decisão técnica de **priorizar estabilidade e entrega do serviço**
* Planejamento para reativação da autenticação por ambiente (dev/staging/prod)

Esses desafios reforçaram a importância de **decisões técnicas pragmáticas** em ambientes reais de nuvem.

---

## 🚀 Deploy

A aplicação foi empacotada em **Docker** e implantada via **Cloud Run**:

```bash
gcloud run deploy starwars-api \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```

---

## 🔐 Autenticação (Planejada)

* JWT com `python-jose`
* Proteção de rotas via `Depends`
* Tokens Bearer

> Atualmente **desativada em produção**, mas pronta para reativação futura.

---

## 📈 Ideias de Evolução e Melhorias futuras

### 🌟 Foco em Experiência do Usuário

* Evolução da API com foco em **engajamento contínuo**

### 🧙 Sistema de Progresso Gamificado

* Evolução de classes baseada em interações do usuário:

  * **Padawan → Cavaleiro Jedi → Mestre Jedi**
* Progressão baseada em:

  * Quantidade de interações
  * Consultas realizadas
  * Participação em quizzes

### 📝 Fluxo de Formulários e Quizzes

* Questionários interativos sobre o universo Star Wars
* Avaliação de conhecimento
* Integração com o sistema de progressão
* Rankings e conquistas

---

## 🧠 Critérios Atendidos

✔ Uso de Python
✔ Integração com SWAPI
✔ Deploy em GCP
✔ Boas práticas de código
✔ Estrutura escalável
✔ Clareza arquitetural
✔ Visão de produto e experiência do usuário
✔ Carregamento da api em cache para melhor desempenho app\integrations\swapi\client.py(https://github.com/leonardo-vinicius/star_wars_project/blob/main/app/integrations/swapi/client.py)

---

## 👨‍💻 Autor

Projeto desenvolvido como **desafio técnico**, com foco em **backend, cloud computing, arquitetura e experiência do usuário**.

---

⭐ *Este projeto demonstra não apenas a implementação técnica, mas também a capacidade de adaptação, tomada de decisão em ambientes cloud e visão de produto.*

> *"Fazer ou não fazer, tentativa não há."* — **Mestre Yoda**