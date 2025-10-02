from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def enviar_factura_email(correo_cliente, cliente_nombre, pdf_bytes):
    msg = MIMEMultipart()
    msg['Subject'] = f'Factura - {cliente_nombre}'
    msg['From'] = 'tu_correo@example.com'   # 👉 cambia por tu correo real
    msg['To'] = correo_cliente

    # Cuerpo del correo
    msg.attach(MIMEText(f'Hola {cliente_nombre}, adjunto tu factura.', 'plain'))

    # PDF adjunto desde bytes
    adj = MIMEApplication(pdf_bytes, _subtype='pdf')
    adj.add_header('Content-Disposition', 'attachment', filename='factura.pdf')
    msg.attach(adj)

    # Enviar correo (usando Gmail como ejemplo)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('alvaromanjarrez0906@gmail.com', 'tu_password')  # ⚠️ Usa clave de aplicación, no tu password normal
        server.send_message(msg)
