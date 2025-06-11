<h1>Projeto de Instrução de Operações — Aralco 📝</h1>

<p>Este projeto tem como objetivo principal <b>facilitar e padronizar o processo de instrução de operadores de campo</b> (caminhão, colhedora, trator e líderes) no ambiente operacional da Aralco. A iniciativa visa aprimorar o registro, a análise e a rastreabilidade dos dados relacionados às instruções. 📊</p>

<p>O sistema oferece uma <b>interface web com autenticação</b>, permitindo o preenchimento e controle dos formulários de instrução. Ele conta com abas dedicadas a diferentes tipos de operação e um histórico completo dos registros. 🖥️</p>

<hr>

<h2>Desenvolvedores 🧑‍💻</h2>

<ul>
    <li><b>Backend:</b> Venicius dos Santos Souza — Responsável pela lógica de negócio, banco de dados e validações, utilizando <b>Django</b>. ⚙️</li>
    <li><b>Frontend:</b> Bryan Vinicius Asciellu — Responsável pelo design visual, interface do usuário (UI), responsividade e usabilidade dos formulários. ✨</li>
</ul>

<hr>

<h2>Tecnologias Utilizadas 🛠️</h2>

<p>O projeto foi desenvolvido com as seguintes tecnologias:</p>

<ul>
    <li><b>Linguagem:</b> Python 3.x 🐍</li>
    <li><b>Framework Web:</b> Django 4.1 🌐</li>
    <li><b>Banco de Dados:</b> PostgreSQL 🐘</li>
    <li><b>Frontend:</b> HTML5, CSS3, JavaScript 🎨</li>
    <li><b>Template Engine:</b> Django Templates</li>
    <li><b>Estilo Responsivo:</b> CSS puro (sem frameworks externos) 📱</li>
</ul>

<hr>

<h2>Dependências 📦</h2>

<p>As dependências do projeto são listadas no arquivo <code>requirements.txt</code>:</p>

<pre><code class="language-txt">asgiref==3.8.1
Django==4.1
psycopg2-binary==2.9.10
sqlparse==0.5.3
tzdata==2025.2
</code></pre>

<hr>

<h2>Funcionalidades ✅</h2>

<p>O sistema oferece as seguintes funcionalidades:</p>

<ul>
    <li><b>Cadastro de instruções</b> por tipo de equipamento (caminhão, colhedora, trator, líder). 🚛🚜 harvester 👨‍✈️</li>
    <li><b>Edição de registros</b> existentes. ✍️</li>
    <li><b>Histórico de instruções</b> com opções de filtros. 📚</li>
    <li><b>Validação de dados</b> tanto no frontend quanto no backend. ✅🔒</li>
    <li><b>Feedback visual</b> (sucesso ou erro) após o envio dos dados. 👍👎</li>
    <li><b>Preenchimento automático</b> do nome do instrutor por matrícula (via JSON). 📝</li>
    <li><b>Separação clara</b> entre as funções de frontend e backend. ➡️⬅️</li>
</ul>

<hr>

<h2>Como Rodar o Projeto 🚀</h2>

<p>Para executar o projeto localmente, siga os passos abaixo:</p>

<pre><code class="language-bash"># Crie o ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Crie o banco de dados (PostgreSQL) e configure no settings.py

# Migre o banco
python manage.py migrate

# Rode o servidor
python manage.py runserver
</code></pre>

<hr>

<h2>Licença 📄</h2>

<p>Este projeto é destinado a <b>uso interno acadêmico/profissional</b>. Caso deseje aplicá-lo em um ambiente de produção, recomenda-se realizar ajustes de segurança e infraestrutura. ⚠️</p>
