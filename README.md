# Cliente servidor con cifrador homomórfico

## Prerequisitos

- Hacer ejecutables los archivos .sh
   ```Terminal
    sudo chmod +x start_servidor.sh
   ```
   ```Terminal
   sudo chmod +x start_cliente.sh
   ```
   ```Terminal
   sudo chmod +x stop_containers.sh
   ```

## Iniciar cliente servidor

1. Levantar primero el servidor
   ```Terminal
   ./start_servidor.sh
   ```

2. Levantar el cliente
    ```Terminal
    uso: ./start_cliente [-h] [--phe]
    
    Flags para activar o los tipos de cifradores
    
    opciones:
      -h, --help  show this help message and exit
      --phe       Activa el cifrador homomorfico parcial
    ```

## Uso cliente servidor

Una vez levantado el cliente y el servidor, desde el cliente podes enviar operaciones encriptadas para que el servidor las resuelva sin necesidad de desencriptarlas. La nomenclatura que decidimos usar es agregar una letra `e` antes de los número que queremos encriptar. Por ejemplo:



El archivo `stop_containers.sh` no es necesario correrlo si los programas terminan "felizmente". Pero en caso de que
haya un
error o el programa termine inesperadamente es recomendable correrlo.

Una vez que paraste los contenedores podés limpiar todas las imágenes (cuidado que borra todas las imágenes docker del
sistema)

```Terminal
docker system prune -a
```
