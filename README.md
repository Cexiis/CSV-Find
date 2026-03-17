# 🔍 CSV Find - Scanner CSV em Lote

## 📌 Descrição

O **CSV Find** é uma aplicação desktop desenvolvida em Python com interface gráfica (GUI) que permite realizar buscas em lote dentro de arquivos `.csv`.

O programa percorre automaticamente uma pasta (e suas subpastas), procurando por termos específicos informados pelo usuário, retornando rapidamente onde cada item foi encontrado.

---

## 🚀 Funcionalidades

* 🔎 Busca em múltiplos arquivos `.csv`
* 📂 Varredura recursiva em pastas e subpastas
* 🧾 Busca por múltiplos termos (um por linha)
* ⚡ Execução em thread (não trava a interface)
* 📍 Exibe:

  * Nome do arquivo
  * Linha onde foi encontrado
  * Caminho completo
* ❌ Indica itens não encontrados
* 🎨 Interface moderna com CustomTkinter

---

## 🖥️ Interface

* Campo para inserir múltiplos termos (ex: seriais)
* Seleção de pasta raiz
* Botão para iniciar busca
* Área de log com resultados em tempo real
* Status da execução

---

## 🛠️ Tecnologias utilizadas

* Python 3.x
* customtkinter
* tkinter
* threading
* csv
* os

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/CSV-Find.git
```

2. Acesse a pasta do projeto:

```bash
cd CSV-Find
```

3. Instale as dependências:

```bash
pip install customtkinter
```

---

## ▶️ Como usar

1. Execute o programa:

```bash
python nome_do_arquivo.py
```

2. Insira os itens que deseja buscar (um por linha)

Exemplo:

```
ABC123
XYZ789
TESTE001
```

3. Clique em **Selecionar Pasta** e escolha o diretório onde estão os arquivos `.csv`

4. Clique em **INICIAR BUSCA**

---

## 📊 Exemplo de saída

```
--- Buscando por: ABC123 ---
✅ ACHOU: ABC123
📄 arquivo.csv (Linha 25)
📍 C:\dados\arquivo.csv

❌ NÃO ENCONTRADO: XYZ789
```

---

## ⚠️ Observações

* Apenas arquivos `.csv` são analisados
* Arquivos com erro de leitura são ignorados automaticamente
* A busca não diferencia maiúsculas/minúsculas

---

## 💡 Possíveis melhorias futuras

* Exportar resultados para arquivo `.txt` ou `.csv`
* Filtros avançados de busca
* Barra de progresso
* Suporte a outros formatos (Excel, TXT)
* Empacotamento como executável (.exe)

---

## 👨‍💻 Autor

Desenvolvido por **Caio César**

---

## 📄 Licença

Este projeto pode ser utilizado livremente para fins de estudo e melhoria.
