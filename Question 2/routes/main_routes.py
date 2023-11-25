from flask import Blueprint, render_template, url_for, flash

from models.Signup import Signup as SignupForm
from util.PdfBuilder import build_pdf

main_bp = Blueprint('main', __name__)


@main_bp.route('/favicon.ico')
def favicon():
    return url_for('static', filename='static/favicon.ico')


@main_bp.route('/', methods=['GET'])
def show_form():
    form = SignupForm()
    return render_template('index.html', form=form)


@main_bp.route('/generate-pdf', methods=['POST'])
def process_form():
    form = SignupForm()
    if form.validate_on_submit():
        try:
            pdf_binary_data = build_pdf(form)
            return render_template('pdf.html', base64_pdf=pdf_binary_data)
        except Exception as e:
            flash(f'Error generating or encoding PDF', 'error')
            return render_template('index.html', form=form)
    else:
        return render_template('index.html', form=form)
