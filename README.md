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
```Terminal
homomorphic_encryption_client
Conectado a localhost:5000
Escribir expresión ("exit" para terminar): 10+e10*2
Resultado del servidor: 40.0
Escribir expresión ("exit" para terminar): exit
```

```Terminal
homomorphic_encryption_server
Servidor escuchando en 0.0.0.0:5000
Conexión establecida con:  ('172.17.0.1', 44600)
Mensaje del cliente: [10.0, '+', <phe.paillier.EncryptedNumber object at 0x7f5aa51538e0>, '*', 2.0]
```


El archivo `stop_containers.sh` no es necesario correrlo si los programas terminan "felizmente". Pero en caso de que
haya un
error o el programa termine inesperadamente es recomendable correrlo.

Una vez que paraste los contenedores podés limpiar todas las imágenes (cuidado que borra todas las imágenes docker del
sistema)

```Terminal
docker system prune -a
```
