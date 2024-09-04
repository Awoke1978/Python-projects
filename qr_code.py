#basic_qr_code.py
import segno

qrcode=segno.make("banana bots",
                     micro=False,
                     version=1,
                     mask=2)
qrcode.save("banana bot micro qr.png",
            scale=10,
            unit="mm",
            border=3,
            light="lightblue",
            dark="green",
            quiet_zone="lightblue")