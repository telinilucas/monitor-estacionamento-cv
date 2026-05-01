# 🚗 Monitor Inteligente de Vagas de Estacionamento

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Linguagem](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-orange)

Este projeto foi desenvolvido como requisito de avaliação acadêmica, com o objetivo de aplicar técnicas de **Visão Computacional Clássica (Sem Inteligência Artificial)** para resolver um problema cotidiano de infraestrutura. 

## 🎥 Demonstração da Aplicação

> **Nota:** Aaixo estão as demonstrações visuais do sistema em funcionamento.

* [**CLIQUE AQUI PARA ASSISTIR AO VÍDEO DO SISTEMA RODANDO (YouTube)**](https://youtu.be/fmU6xT8bF4o)

**Captura de Tela do Sistema:**


---

## 🧠 Técnicas de Visão Computacional Utilizadas

Cumprindo rigorosamente a restrição de **não utilizar modelos de Inteligência Artificial** (como YOLO ou Redes Neurais), este projeto opera através de um pipeline de processamento de imagem puro para analisar a densidade estrutural dentro de Regiões de Interesse (ROIs). 

As seguintes técnicas foram aplicadas frame a frame:

1. **Conversão Grayscale (`cv2.cvtColor`):** Remoção dos canais de cor para otimizar o processamento matemático da matriz de pixels, focando apenas na intensidade luminosa.
2. **Gaussian Blur (`cv2.GaussianBlur`):** Filtro de suavização aplicado para mitigar ruídos visuais de alta frequência presentes na textura do asfalto, reduzindo falsos positivos.
3. **Canny Edge Detection (`cv2.Canny`):** **(O núcleo lógico do projeto)**. Em vez de uma simples binarização por luz, o detector de Canny calcula o gradiente da imagem para encontrar apenas as arestas estruturais fortes (contornos dos veículos, portas, vidros e rodas). O asfalto vazio é ignorado e convertido em preto absoluto.
4. **Dilatação Morfológica (`cv2.dilate`):** Aplicação de um kernel matemático sobre as arestas encontradas pelo Canny para engrossar as linhas e conectá-las, transformando o contorno de um carro em uma massa densa de pixels brancos.
5. **Cálculo de Densidade (`cv2.countNonZero`):** O sistema isola as coordenadas das vagas desenhadas pelo usuário e conta a quantidade de pixels estruturais (brancos). Se o valor ultrapassar o *threshold* calibrado, a vaga é classificada como **Ocupada**.

---

## ⚙️ Tecnologias Utilizadas

* **Python 3**
* **OpenCV (`opencv-python`)** - Processamento das imagens e algoritmos matemáticos.
* **NumPy** - Manipulação dos arrays matriciais (kernels morfológicos).

---

## 🚀 Como instalar e executar

**1. Clone o repositório:**
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd SEU_REPOSITORIO