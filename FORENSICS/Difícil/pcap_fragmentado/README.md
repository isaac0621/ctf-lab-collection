# PCAP Fragmentado Challenge

## Descripción
Un archivo PCAP contiene paquetes de red fragmentados. Debes reconstruir los datos.

## Herramientas
- Wireshark - GUI para análisis de tráfico
- tcpdump - Herramienta de línea de comandos
- tshark - Versión línea de comandos de Wireshark

## Instrucciones
1. Abre el PCAP en Wireshark
2. Busca paquetes fragmentados
3. Reconstruye los fragmentos
4. Extrae el flag

## Solución
```bash
# Ver contenido
tcpdump -r packets.pcap

# Filtrar paquetes específicos
tshark -r packets.pcap -Y "ip.flags.mf==1"

# Reconstruir usando Wireshark:
# - Abre el archivo
# - Busca paquetes con flag MF (More Fragments)
# - Wireshark reconstruye automáticamente
# - Busca en payloads
```

## Flag
```
CTF{pcap_reassembled}
```

## Conceptos
- Network forensics
- IP fragmentation
- Packet reconstruction
- TCP/IP protocols
