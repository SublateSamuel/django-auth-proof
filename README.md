# Sistema de Autenticação no Django

Este repositório apresenta uma prova de conceito para a implementação de um sistema de autenticação completo em Django, demonstrando a personalização do modelo de usuário através da extensão da classe `AbstractUser`. O objetivo é fornecer um exemplo concreto de como construir um sistema de autenticação que não só atenda às necessidades básicas de segurança mas também ofereça flexibilidade para adaptações futuras, tudo isso utilizando as poderosas ferramentas e classes fornecidas pelo Django.

## Technologies Used

- **Linguagem**: Python3.12
- **Framework**: Django
- **Administrador**: Poetry
- **Proxy Reverso**: Nginx
- **Banco de Dados**: Postgres
- **Containerization**: Docker, Docker Compose

## Propósito

O propósito deste projeto é ilustrar um método eficaz para estender a classe `AbstractUser` do Django, criando assim um modelo de usuário personalizado que se integra perfeitamente ao sistema de autenticação padrão do Django. Este repositório é ideal para desenvolvedores que buscam implementar ou entender como criar um sistema de autenticação customizado no Django, aproveitando ao máximo as funcionalidades que a framework oferece.

## Funcionalidades Principais

- **Registro de Usuários**: Permite que novos usuários criem uma conta, fornecendo um processo de registro integrado e personalizado.
- **Edição da Conta**: Os usuários podem atualizar suas informações de perfil, permitindo a personalização e gestão de suas contas.
- **Login**: Implementa um sistema de login seguro, utilizando as classes e métodos de autenticação padrão do Django.
- **Logout**: Oferece aos usuários a opção de se desconectarem de forma segura, encerrando a sessão atual.

## Como Utilizar

Para começar a usar este projeto, siga estes passos:

### 1. **Clone o repositório**

```bash
git clone https://github.com/SublateSamuel/django-auth-proof.git
```

### **2. Conceda permissões de execução para o scrit**

Navegue até o diretório do projeto e conceda permissões de execução ao script **`build-and-up.sh`**.

```bash
cd django-auth-proof
sudo chmod a+x ./bin/build-and-up.sh
```

### **3. Rodar o script**

Navegue até o diretório do projeto e execute o script **`build-and-up.sh`** para construir e iniciar os serviços.

```bash
cd ./bin
./build-and-up.sh
```

O script cuidará de todas as configurações necessárias, garantindo que todos os serviços estejam funcionando conforme o esperado.

### **4. Acessando a aplicação**

Após a conclusão da execução do script, a aplicação estará disponível para acesso através do navegador utilizando o endereço configurado (por exemplo, **`http://localhost:9999`**).
