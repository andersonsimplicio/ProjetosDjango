# Repositório de Projetos Django

Este repositório é destinado a guardar diversos projetos desenvolvidos com o framework Django. Ele serve tanto para fins de teste quanto para a realização de trabalhos e experimentos com Django.

<p align="center">
  <img src="img/programer.gif" alt="Imagem Ilustrativa">
</p>

## Atualize todo os pacotes do pip

```
pip list --outdated | awk 'NR>2 {print $1}' | xargs -n1 pip install -U

```
ou execute:
```
   python update.py 

```

## Estrutura do Repositório

- `venv/`: Ambiente virtual Python utilizado para gerenciar as dependências dos projetos. 
- `manageruser/`: Criando um sistema de gerenciamento de usuários personalizado no Django.

### `space/`
- Criando um blog para visualizar fotos do espaço.
<div align="center">
    <img src="img/space.png" style="border-radius: 15px; border: 1px solid orange;" alt="Imagem do Blog" width="500">
</div>

### `newletter/`
- Testando a configuração de tailwind + Django
   <div align="center">
    <img src="newletter/core/static/assets/img/django-tailwind.png" style="border-radius: 15px; border: 1px solid orange;" alt="Imagem do Blog" width="500">
   </div>

### `receitas/`
- Testando a configuração de Vue 3 + Django
   <div align="center">
    <img src="img/receitas.png" style="border-radius: 15px; border: 1px solid orange;" alt="Imagem do Blog" width="500">
   </div>

### `receitas-drf/`
- Testando a configuração + Django + pytest + DjangoRestFrameWork
   <div align="center">
    <img src="img/receitas-drf.png" style="border-radius: 15px; border: 1px solid orange;" alt="Imagem do Blog" width="500">
    <div align="left">
    <p>Comando para Test<p/>
    <ul>
      <li><strong>pytest</strong> apps/receitas/tests/test_recipe_views.py</li>
      <li><strong>pytest</strong> apps/receitas/tests/receita_model_test.py</li>
      <li><strong>pytest</strong> apps/receitas/tests/receita_url_test.py</li>
      <li><strong>pytest</strong> apps/receitas/tests/test_recipe_base.py</li>
    <ul>
   </div>

   </div>


Cada projeto Django possui sua própria estrutura de diretórios e arquivos, incluindo pastas como `migrations`, `static`, `templates`, e outros componentes típicos de um projeto Django.

## Configuração Inicial

1. **Clone o repositório**:
   ```sh
   git clone https://github.com/andersonsimplicio/ProjetosDjango.git
   cd seu_repositorio

2. **Configurando a venv**
   - python -m venv venv
   - source venv/bin/activate
3. **Instalar dependências**
   - pip install -r requirements.txt  
