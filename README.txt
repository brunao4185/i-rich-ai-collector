I Rich AI - Coletor de Trades (Render Deployment)

1. Suba este repositório no seu GitHub
2. No Render.com, crie um "New Web Service" conectado a este repositório
3. Use as seguintes configurações:
   - Build command: pip install -r requirements.txt
   - Start command: python collector.py
   - Port: 5000
4. Use o endpoint: https://<nome-do-render>.onrender.com/webhook
5. Envie os alertas JSON do TradingView para esse endpoint
