from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def enviar_factura_email(correo_cliente, cliente_nombre, pdf_buffer):
    msg = MIMEMultipart()
    msg['Subject'] = f'Factura - {cliente_nombre}'
    msg['From'] = 'tu_correo@example.com'
    msg['To'] = correo_cliente

    # Cuerpo del correo
    msg.attach(MIMEText(f'Hola {cliente_nombre}, adjunto tu factura.', 'plain'))

    # PDF adjunto
    pdf_buffer.seek(0)  # Asegurarse de que el buffer esté al inicio
    adj = MIMEApplication(pdf_buffer.read(), _subtype='pdf')
    adj.add_header('Content-Disposition', 'attachment', filename='factura.pdf')
    msg.attach(adj)

    # Enviar correo
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('alvaromanjarrez0906@gmail.com', 'tu_password')
        server.send_message(msg)