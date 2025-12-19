import random
import smtplib
from email.message import EmailMessage

saajad = []
soovid = []


def kogu_soovid():
    """Kogub kasutajalt õnnitluste tekstid"""
    try:
        arv = int(input("Mitu õnnitlusteksti soovid lisada? "))
        for i in range(arv):
            soov = input(f"Sisesta soov {i + 1}: ")
            soovid.append(soov)
    except ValueError:
        raise ValueError("Õnnitluste arv peab olema number!")


def kogu_saajad():
    """Kogub kasutajalt e-posti aadressid"""
    try:
        arv = int(input("Mitu saajat soovid lisada? "))
        for i in range(arv):
            email = input(f"kuttimrasmus@gmail.com {i + 1}: ")
            if "@" not in email:
                print("Hoiatus: see ei tundu olevat korrektne e-posti aadress.")
            saajad.append(email)
    except ValueError:
        raise ValueError("Saajate arv peab olema number!")


def genereeri_juhuslik_soov(soovide_list):
    if not soovide_list:
        raise ValueError("Õnnitlusi pole lisatud!")
    return random.choice(soovide_list)


def koosta_onnitlused(valitud_saajad=None):
    if valitud_saajad is None:
        valitud_saajad = saajad

    tulemused = []
    for saaja in valitud_saajad:
        soov = genereeri_juhuslik_soov(soovid)
        tulemused.append(f"{saaja}: {soov}")
    return tulemused


def saada_kiri(saaja, sisu):
    saatja_email = "kuttirasmus@gmail.com"
    rakenduse_parool = "rassu190"

    msg = EmailMessage()
    msg["From"] = saatja_email
    msg["To"] = saaja
    msg["Subject"] = "Jõulutervitus 🎄"
    msg.set_content(sisu)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(saatja_email, rakenduse_parool)
            server.send_message(msg)
        return True
    except (smtplib.SMTPException, OSError) as e:
        print(f"E-kirja saatmine ebaõnnestus: {e}")
        return False

