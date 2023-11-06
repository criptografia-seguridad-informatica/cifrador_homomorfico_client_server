1. Hacer ejecutables los archivos .sh
   ```Terminal
    sudo chmod +x start_server.sh
   ```
   ```Terminal
   sudo chmod +x start_client.sh
   ```
   ```Terminal
   sudo chmod +x stop_containers.sh
   ```
2. Levantar primero el servidor
   ```Terminal
   ./start_server.sh
   ```

3. Levantar el cliente
   ```Terminal
   ./start_client.sh
   ```

El archivo `stop_containers.sh` no es necesario correrlo si los programas terminan "felizmente". Pero en caso de que
haya un
error o el programa termine inesperadamente es recomendable correrlo.

Una vez que paraste los contenedores podés limpiar todas las imágenes (cuidado que borra todas las imágenes docker del
sistema)

```Terminal
docker system prune -a
```
