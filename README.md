#### Project Overview:

This project involves creating a simple chat application using Python and WebSockets. The goal is to establish real-time communication between multiple clients connected to a server. The chat application will allow users to send and receive messages instantly, showcasing the use of WebSockets for maintaining a persistent connection between the server and the clients.

#### Technology Stack:

-   Programming Language: python
    
-   Socket Library:  Socket (Python library), websockets (Python library),
    
-   Concurrency: Threading (to handle multiple client connections simultaneously)
    

#### System Requirements

-   Python 3.x installed on your system.
    
-   Basic understanding of Socket protocol , websockets and Python programming.
    

  

#### Detailed Implementation:

  

##### 1. Server-Side Implementation

  

-   Code File:  server.py
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXclbNga6tlAVlqGv_ELLoxB6H5vjic_dnaiX-vo0xpsrGIOn0jOuFecwWjcszAcbjr_my-z7oMPM-a6s8y2sSoPFwg73GVemA3m3XUW1QuNO8_ax5zCKrZPTamQPZyW3Jae_hSWmgugaWoQtm-_rsmbuCid?key=o80k732yts8IGZfP_LeX5A)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfEKdOdF4zM8k-JrxeE0cM95MuBZOaFXpUmgUaZNL6ikS-GU-QHak02w8QHkI6yknFQZ-lBd0p9IwpXr7Pv6VLABVw-lbCm7W_ahd_1Sz7urKmg72He7UPGAZ31iMSelcd63uVhm20h3kG_ysw_xfCLSB4?key=o80k732yts8IGZfP_LeX5A)

-   Purpose: Manages WebSocket connections, handles incoming messages, and broadcasts them to all connected clients, handling clients disconnection.
    

#####   
2. Client-Side Implementation

-   File:  client.py
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXft_zYRsntWxyAkdbn4UHYxWQ6FDuO4WE1rFPWIUta-rKLJFd--2iZB-Pcwxpl_F30eCV6sEuhoG4MZWEyl3NIEgWtUegVLjKdRDWqImzCRUIUrl7_xpieWOhhw0NCdBiXKBeYsI5uchpr3P8U6oJus7d0?key=o80k732yts8IGZfP_LeX5A)

  

-   Purpose: Connects to the Socket server, sends messages, and receives broadcasts from other clients.
    

  
  
  
  
  
  
  

#### Usage Instructions

1.  Run the Server:
    

-   Start the Socket server by running the server.py script.
    
-   Ensure the server is running before any clients attempt to connect.
    

Run server.py:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdo20CtLMzXi5878PADt5dhknHe7-Zf6ShOZh5qwBksultPlV3CegKA3paYfyt5GkXEhg3EGxHmjYiByJ6fLlYiYBlpnp-H7dINJ1tQpiRXTQNcLLxgMxo_I3YKRCsAPMIlRxD3fLSAGRzJdTYgQP0gNig?key=o80k732yts8IGZfP_LeX5A)

Client connected to the server:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdmws1XPROVq6h3HT5JkbI4EkpsXCCZ0jvjDEadFQXrx0N3Lad5JOxUzGIvUXsA-RDyiNFR9bxaUQGYUMzDYiOrhwWprIOVXzbAMTdbJC0MW_6ATJOnKweAebvYOkzUM1WECLxG7OwHq_BU8g2RZAwUtHP7?key=o80k732yts8IGZfP_LeX5A)

Message are received from client:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd7iubXBBUfexNT8Hd8-tx8AVYMFJUYGJ5OQPrNQe4JzGJpgCp6fMOATbrdgi4ddtFGJ50ARsqjPJyfo3xGwhEmrIYBFCHddfFQgX0gX-2Wpqf9_5odt3lbPebcjkdI7xg94eUwJIM-xQdUt1zNUVL03J05?key=o80k732yts8IGZfP_LeX5A)

  
  

2.  Run the Client(s):
    

  

-   Run the client.py script on multiple terminals to simulate multiple clients.
    
-   Each client will be able to send messages that will be broadcast to all other connected clients.
    
-     
    

Run client.py

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcLTQoh7tzi1zNWGzh92ZzKsKKewQlXziEFRcRDI9sfYz5cM1b160uP7yZ6FNl25Ix6mQnCKo9dhBbjk_nl5KWPQNDtl3qlTJm1tX4llNwdCGayUcqaY0ZLJs425EwD9RJZ6GPyBjM_B0It2n1so_FRBKE?key=o80k732yts8IGZfP_LeX5A)

  

Client 2 :receives the broadcasted message:

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdsE9IzSO1TJfU_eW5eEQ4LhjK-suzOM8BzBaldJI9XiEsW5F9uMSfHnQz2QnpH22CSDlycG5mssQfdjtU0nvP1k27uhnCAD-P-PwlSDbuARsFdN1Pd1rCnIzDAkdQE_8T12y8n2ehWQtqqG9-MOrIfESI?key=o80k732yts8IGZfP_LeX5A)

Client 3:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd3DLHYohVYDtWNBghaZ1zvWzBNbcHSDAzV7tFeDk52gdoDdjb2pI8Rdy1rZQ3ixBpIiXkzg0kHuXk9CV3ym_uiC_7I-wjKZgD9jmx3ayTphewrw_02XwxjEPV-FHaGBepR4m9DJOKRAE4s7wrtf6c5glE?key=o80k732yts8IGZfP_LeX5A)

  
  
  

#### Usage Instructions:

  
  

server.py

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdkr9PhDHX3hXP7-KXRq1uNXS1IopZKHYPRXh1pdLOOvo1GRkds_YkOE4MZclVYZKb49V5DEdwiSnz3Ay69Me6pRSOTWLAlLJtAlx6ZIxQiflnMKp9zDmdjDdrOxmqmdsZwEry4ZwEwl0a0xjM5Yjmm3Rjt?key=o80k732yts8IGZfP_LeX5A)

#### ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf74BbqY_k7mgEvvOBjjaOcXRqKAV5x09qfzk8YGN8Ca0Qb6kOWVgykW2U4wDJy7MfNFmX8C5jifIb0GzCOqmNphezn9lMoF2iSsMW-phHYqtjmHvgd-THQ_daWlP2FawI62K40miNT_RjNslAG_cZdMNE?key=o80k732yts8IGZfP_LeX5A)

  
  
  

Index.html

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcH77wOAdJuGBQuI0jjlvg0OMUMwcMAvORsnBHmzlDJQk0A4yjAEeOTY-a25WwjaqpIi9bedJxaw0ig1WtItjhBG4zNfPwgdhJWBdif3dpHldHPeCMMBdtMJx1911SZK5-34aeum-Y5k90zUxhfCloCOK6W?key=o80k732yts8IGZfP_LeX5A)

  

Broadcast Message

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdZkxXh6wGdOH5_L4r_bI4keEen35FsB7h3vTwFHsiFbLoJSzaCuiZLGNUiyqgw6BTov_V2AC9sE2XigjL7CiElWRbVL8_12HwRk3H0mVg4Ikfmhv26bPpRENgmfnbLoR1QuUBEwdNq3fEkYseTGjNeBZA?key=o80k732yts8IGZfP_LeX5A)

  
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeM3w5xXjFN1QkvvERCDxjK6F7Fp-AkDeAhjI41B6cGGbCN5G3pTWKPCOH0qtZ_NNxWaDHQtyUEH4LO4dMhLtCFwZWGWRhevvOpbssn3cBfUjEc5teFGxSsy5J0rAgZ83PVpQCYVfDPm6OhQ_rmgeiFudNV?key=o80k732yts8IGZfP_LeX5A)
