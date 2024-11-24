
# 🤖⚽ Simulação de Trajetória de Bola e Robô

Este projeto em Python simula e analisa a trajetória de uma bola e um robô em um plano, considerando sua interação. Ele realiza cálculos de interceptação, distância, velocidade e aceleração, além de gerar gráficos para visualização das trajetórias.

## ⚙️ Funcionalidades

- Leitura de dados de trajetória de um arquivo CSV.
- Cálculo da distância entre o robô e a bola.
- Determinação do ponto de interceptação baseado na velocidade do robô.
- Geração de gráficos para:
  - Trajetórias da bola e do robô.
  - Posições e velocidades em função do tempo.
  - Aceleração de ambos os objetos.
  - Distância relativa entre a bola e o robô.

## 🔩 Requisitos

Certifique-se de ter o Python 3.8+ instalado. Além disso, você precisará instalar as seguintes bibliotecas:

- `numpy`
- `matplotlib`

Instale-as usando o seguinte comando:

```bash
pip install numpy matplotlib
```

## ⌨️ Uso

1. Clone este repositório:
    ```bash
    git clone https://github.com/seuusuario/simulacao-trajetoria.git
    cd simulacao-trajetoria
    ```

2. Certifique-se de ter o arquivo `trajetoria.csv` no mesmo diretório. O arquivo deve conter os dados de tempo e coordenadas em formato delimitado por ponto e vírgula (`;`).

3. Execute o script:
    ```bash
    python simulacao_trajetoria.py
    ```

4. Insira as coordenadas iniciais do robô quando solicitado.

5. O script exibirá os cálculos e gráficos.

## 💻 Arquivo `trajetoria.csv`

O arquivo de entrada deve seguir o formato:

```
tempo;x;y
0.0;1.0;2.0
0.5;1.5;2.5
...
```

## 📈 Exemplos de Gráficos

- **Trajetórias da Bola e do Robô**: Visualiza as trajetórias no plano XY.
- **Velocidade e Aceleração**: Mostra as variações ao longo do tempo.
- **Distância Relativa**: Mede a distância entre o robô e a bola durante o movimento.

## 👥 Parceria

Código feito em parceria com o Nathan ⮧ <br>
[![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/Neromakii
) 

---

**Nota:** Este projeto é uma criação educacional para fins de inspiração e aprendizado.
