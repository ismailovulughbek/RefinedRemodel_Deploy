from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import logging
# from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = '7346257350:AAFSNX8MNN7EcH6q-l-fgVoTWLWi25O1me4'
TELEGRAM_CHAT_ID = '-1002881172748'

app = Flask(__name__)
CORS(app)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def services():
    return render_template('service.html')

@app.route('/project')
def projects():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



# INTRO SECTION MESSAGE FORM

@app.route('/intro_message', methods=['POST'])
def intro_message():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        phone = data.get('phone', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not phone or not message:
            return jsonify({'status': 'error', 'message': {'en':'Please fill in all fields!', 'es': '¡Por favor, rellena todos los campos!'}}), 400


        text = f"📬 *NEW MESSAGE!*\n\n👤 Name: {name}\n📧 Email: {email}\n📞 Phone: {phone}\n🏥 Message: {message}"
        payload = {
            'chat_id': -1002881172748,
            'text': text,
            'parse_mode': 'Markdown'
        }

        # url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"
        url = f"https://api.telegram.org/bot7346257350:AAFSNX8MNN7EcH6q-l-fgVoTWLWi25O1me4/sendMessage"
        response = requests.post(url, data=payload)

        if response.status_code != 200:
            return jsonify({'status': 'error', 'message': {'en':'Your message could not be sent!', 'es':'No se pudo enviar tu mensaje!'}}), 500

        return jsonify({'status': 'success', 'message':{'en': 'Your message was sent successfully!', 'es': '¡Tu mensaje fue enviado con éxito!'}})

    except Exception as e:
        return jsonify({'status': 'error', 'message': {'en': 'Internal server error!', 'es': '¡Error interno del servidor!'}}), 500




# HOME PAGE MESSAGE FORM

@app.route('/service_message', methods=['POST'])
def footer_message():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        phone = data.get('phone', '').strip()
        email = data.get('email', '').strip()
        service = data.get('service', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not phone or not service or not message:
            return jsonify({'status': 'error', 'message': 'Please fill in all fields!'}), 400


        text = f"📬 *NEW MESSAGE!*\n\n👤 Name: {name}\n📧 Email: {email}\n📞 Phone: {phone}\n📌 Service: {service}\n\n📝 Message: {message}"
        payload = {
            'chat_id': -1002881172748,
            'text': text,
            'parse_mode': 'Markdown'
        }

        # url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"
        url = f"https://api.telegram.org/bot7346257350:AAFSNX8MNN7EcH6q-l-fgVoTWLWi25O1me4/sendMessage"
        response = requests.post(url, data=payload)

        if response.status_code != 200:
            return jsonify({'status': 'error', 'message': {'en':'Your message could not be sent!', 'es':'No se pudo enviar tu mensaje!'}}), 500

        return jsonify({'status': 'success', 'message':{'en': 'Your message was sent successfully!', 'es': '¡Tu mensaje fue enviado con éxito!'}})

    except Exception as e:
        return jsonify({'status': 'error', 'message': {'en': 'Internal server error!', 'es': '¡Error interno del servidor!'}}), 500




# API CONTACT MESSAGE

@app.route('/contact_message', methods=['POST'])
def contact_message():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not phone or not subject or not message:
            return jsonify({'status': 'error', 'message': 'Please fill in all fields!'}), 400


        text = f"📬 *NEW MESSAGE!*\n\n👤 Name: {name}\n📧 Email: {email}\n📞 Phone: {phone}\n📌 Subject: {subject}\n\n📝 Message: {message}"
        payload = {
            'chat_id': -1002881172748,
            'text': text,
            'parse_mode': 'Markdown'
        }

        # url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"
        url = f"https://api.telegram.org/bot7346257350:AAFSNX8MNN7EcH6q-l-fgVoTWLWi25O1me4/sendMessage"
        response = requests.post(url, data=payload)

        if response.status_code != 200:
            return jsonify({'status': 'error', 'message': {'en':'Your message could not be sent!', 'es':'No se pudo enviar tu mensaje!'}}), 500

        return jsonify({'status': 'success', 'message':{'en': 'Your message was sent successfully!', 'es': '¡Tu mensaje fue enviado con éxito!'}})

    except Exception as e:
        return jsonify({'status': 'error', 'message': {'en': 'Internal server error!', 'es': '¡Error interno del servidor!'}}), 500


