# WordPress + MiniShop en Docker

Proyecto de MiniShop=> Proyecto de Aula (MiniShop) listo para instalar.

## Prerrequisitos, tener instalado

- Docker  
- Docker Compose  
- Archivo `.env` configurado (copia de `.env.example`)

## Instrucciones

1. **Configura tus credenciales**  
   ```bash
   cp .env.example .env
   # Edita .env con tu DB_HOST, DB_NAME, DB_USER, DB_PASSWORD y opcional DB_PREFIX

2. **Levantamos el entorno**  

docker-compose up --build

3.  **Verificamso que el entrno esté corriendo** 

docker-compose ps

4. **Instalamos MiniShop** 
docker-compose exec wordpress wp plugin install woocommerce --activate --allow-root

5. **Actualizamos plugins MiniShop** 
docker-compose exec wordpress wp core update --allow-root
docker-compose exec wordpress wp plugin update --all --allow-root

6. **Abrimos el navegador** 

Ingresamos a: http://localhost:8000