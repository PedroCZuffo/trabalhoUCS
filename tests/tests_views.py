from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from your_app.models import Historia, Pergunta, Botao, Resposta

class HistoriaCreateViewTests(APITestCase):
    def test_create_historia(self):
        url = reverse('historia-create')
        data = {
            "titulo": "Título da História",
            "image": "caminho/para/imagem.png",
            "perguntas": [
                {
                    "titulo": "Pergunta 1",
                    "texto": "Texto da pergunta 1",
                    "botoes": [
                        {
                            "texto": "Texto do botão 1"
                        },
                        {
                            "texto": "Texto do botão 2"
                        }
                    ]
                },
                {
                    "titulo": "Pergunta 2",
                    "texto": "Texto da pergunta 2",
                    "botoes": [
                        {
                            "texto": "Texto do botão 3"
                        }
                    ]
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Historia.objects.count(), 1)
        self.assertEqual(Pergunta.objects.count(), 2)
        self.assertEqual(Botao.objects.count(), 3)

class RespostaCreateViewTests(APITestCase):
    def setUp(self):
        self.historia = Historia.objects.create(titulo="História", image="imagem.png")
        self.pergunta1 = Pergunta.objects.create(titulo="Pergunta 1", texto="Texto da pergunta 1", historia=self.historia)
        self.pergunta2 = Pergunta.objects.create(titulo="Pergunta 2", texto="Texto da pergunta 2", historia=self.historia)

    def test_create_respostas(self):
        url = reverse('resposta-create')
        data = [
            {
                "texto": "Texto da resposta 1",
                "pergunta": self.pergunta1.id
            },
            {
                "texto": "Texto da resposta 2",
                "pergunta": self.pergunta2.id
            }
        ]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Resposta.objects.count(), 2)
        self.assertEqual(Resposta.objects.get(id=1).texto, "Texto da resposta 1")
        self.assertEqual(Resposta.objects.get(id=2).texto, "Texto da resposta 2")
