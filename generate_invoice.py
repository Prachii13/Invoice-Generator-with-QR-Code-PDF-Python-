from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import qrcode

def create_invoice(customer, items, qr_data, filename='invoice.pdf'):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, 800, "🧾 INVOICE")

    # Customer Details
    c.setFont("Helvetica", 12)
    c.drawString(50, 770, f"Customer: {customer['name']}")
    c.drawString(50, 755, f"Email: {customer['email']}")
    c.drawString(50, 740, f"Address: {customer['address']}")

    # Table Headers
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 700, "Item")
    c.drawString(300, 700, "Qty")
    c.drawString(400, 700, "Price")

    y = 680
    total = 0
    c.setFont("Helvetica", 12)

    for item in items:
        c.drawString(50, y, item['name'])
        c.drawString(300, y, str(item['qty']))
        c.drawString(400, y, f"₹{item['price']}")
        total += item['qty'] * item['price']
        y -= 20

    # Total
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 20, f"Total Amount: ₹{total}")

    # QR Code
    qr_img = qrcode.make(qr_data)
    qr_img.save("qr_temp.png")
    c.drawImage("qr_temp.png", 400, y - 100, width=100, height=100)

    c.save()
    print(f"✅ Invoice saved as {filename}")

# Example Usage
if __name__ == "__main__":
    customer = {
        'name': "Prachi Singh",
        'email': "prachi@example.com",
        'address': "Bhopal, India"
    }

    items = [
        {'name': "Notebook", 'qty': 2, 'price': 150},
        {'name': "Pen Pack", 'qty': 1, 'price': 50},
        {'name': "Water Bottle", 'qty': 1, 'price': 200}
    ]

    qr_data = "Invoice ID: 7890 | Pay at: upi://pay?pa=abc@upi"
    create_invoice(customer, items, qr_data)
